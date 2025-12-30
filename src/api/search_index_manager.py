from typing import Optional, Union

import glob
import csv
import json
import re
import os
import yaml
import asyncio

from azure.core.credentials import AzureKeyCredential
from azure.core.credentials_async import AsyncTokenCredential
from azure.search.documents.aio import SearchClient
from azure.search.documents.indexes.aio import SearchIndexClient
from azure.search.documents.models import VectorizedQuery, QueryType
from azure.search.documents.indexes.models import (
    SearchField,
    SearchFieldDataType,
    SimpleField,
    SearchIndex,
    VectorSearch,
    VectorSearchProfile,
    HnswAlgorithmConfiguration,
    SemanticConfiguration,
    SemanticField,
    SemanticPrioritizedFields,
    SemanticSearch,
)
from azure.ai.inference.aio import EmbeddingsClient
from openai import AsyncAzureOpenAI
from azure.core.exceptions import ResourceNotFoundError, HttpResponseError
from .util import ChatRequest


class SearchIndexManager:
    """
    The class for searching of context for user queries.

    :param endpoint: The search endpoint to be used.
    :param credential: The credential to be used for the search.
    :param index_name: The name of an index to get or to create.
    :param dimensions: The number of dimensions in the embedding. Set this parameter only if
                       embedding model accepts dimensions parameter.
    :param model: The embedding model to be used,
                  must be the same as one use to build the file with embeddings.
    :param embeddings_client: The embedding client.
    """
    
    MIN_DIFF_CHARACTERS_IN_LINE = 5
    MIN_LINE_LENGTH = 5
    METADATA_FIELDS = [
        ("title", "title", False),
        ("ms.date", "ms_date", False),
        ("customer-intent", "customer_intent", False),
        ("ms.topic", "ms_topic", False),
        ("ms.service", "ms_service", False),
        ("ms.collection", "ms_collection", True),
        ("description", "description", False),
        ("audience", "audience", False),
        ("ms.product", "ms_product", False),
    ]
    
    def __init__(
            self,
            endpoint: str,
            credential: Union[AsyncTokenCredential, AzureKeyCredential],
            index_name: str,
            dimensions: Optional[int],
            model: str,
            embeddings_client: Union[EmbeddingsClient, AsyncAzureOpenAI],
            semantic_config_name: str = "semantic-docs",
        ) -> None:
        """Constructor."""
        self._dimensions = dimensions
        self._index_name = index_name
        self._embeddings_client = embeddings_client
        self._endpoint = endpoint
        self._credential = credential
        self._index = None
        self._model = model
        self._client = None
        self._semantic_config_name = semantic_config_name

    def _get_client(self):
        """Get search client if it is absent."""
        if self._client is None:
            self._client = SearchClient(
                endpoint=self._endpoint, index_name=self._index.name, credential=self._credential)
        return self._client

    @staticmethod
    def _clean_markdown_images(text: str) -> str:
        """
        Remove or replace markdown image references that would cause LLM API errors.
        
        Images with relative paths can't be processed by the LLM API, so we:
        1. Remove inline images: ![alt](path)
        2. Remove reference-style images: ![alt][ref] and [ref]: path
        
        :param text: The markdown text to clean.
        :return: Cleaned text without problematic image references.
        """
        # Remove inline images: ![alt text](image_path)
        text = re.sub(r'!\[([^\]]*)\]\([^\)]+\)', r'[Image: \1]', text)
        
        # Remove reference-style image definitions: [id]: path "title"
        text = re.sub(r'^\[([^\]]+)\]:\s+[^\s]+.*$', '', text, flags=re.MULTILINE)
        
        return text

    async def search(self, message: ChatRequest) -> tuple[str, list[dict]]:
        """
        Search the message in the vector store using hybrid search with semantic ranking.

        :param message: The customer question.
        :return: Tuple of (context string, list of source documents with metadata).
        """
        self._raise_if_no_index()
        embedded_question = (await self._embeddings_client.embed(
            input=message.messages[-1].content,
            dimensions=self._dimensions,
            model=self._model
        ))['data'][0]['embedding']
        
        search_text = message.messages[-1].content
        
        # Get field names from environment or default to sample schema
        vector_field = os.getenv("AZURE_SEARCH_FIELD_VECTOR", "text_vector")
        content_field = os.getenv("AZURE_SEARCH_FIELD_CONTENT", "chunk")
        
        vector_query = VectorizedQuery(vector=embedded_question, k_nearest_neighbors=5, fields=vector_field)
        
        # Use semantic search only if semantic configuration is available
        select_fields = [content_field, 'title', 'chunk_id'] + [field_name for _, field_name, _ in self.METADATA_FIELDS]
        search_params = {
            "search_text": search_text,
            "vector_queries": [vector_query],
            "select": select_fields,
            "top": 5
        }
        
        # Only add semantic parameters if semantic config name is provided
        if self._semantic_config_name:
            search_params["query_type"] = QueryType.SEMANTIC
            search_params["semantic_configuration_name"] = self._semantic_config_name
        
        response = await self._get_client().search(**search_params)
        
        sources = []
        context_chunks = []
        idx = 0
        async for result in response:
            # Handle different content field names
            content = result.get(content_field) or result.get('chunk') or result.get('content') or ""
            
            # Clean markdown images from chunks to avoid LLM API errors
            cleaned_chunk = self._clean_markdown_images(content)
            context_chunks.append(cleaned_chunk)
            sources.append({
                'rank': idx + 1,
                'title': result.get('title', 'Unknown'),
                # Prefer chunk_id if present, otherwise fall back to embedId for legacy indexes
                'chunk_id': result.get('chunk_id') or result.get('embedId', ''),
                'content': content,  # Send full content without truncation
                **{field_name: result.get(field_name) for _, field_name, _ in self.METADATA_FIELDS}
            })
            idx += 1
        
        return "\n------\n".join(context_chunks), sources
    
    async def upload_documents(self, embeddings_file: str, batch_size: int = 200) -> None:
        """
        Upload the embeddings file to index search with retry and resume support.

        :param embeddings_file: The embeddings file to upload.
        :param batch_size: The number of documents to upload in a single batch.
        """
        self._raise_if_no_index()
        checkpoint_path = embeddings_file + ".upload.chk"
        resume_from = 0
        if os.path.exists(checkpoint_path):
            try:
                with open(checkpoint_path, "r", encoding="utf-8") as cp:
                    data = json.load(cp)
                    resume_from = int(data.get("last_row", 0))
                    print(f"Resuming upload from row {resume_from} based on checkpoint {checkpoint_path}")
            except Exception:
                resume_from = 0

        documents = []
        row_index = 0
        uploaded_docs = 0
        skipped_docs = 0
        batches = 0
        retries_total = 0
        client = self._get_client()

        async def upload_batch(payload: list[dict], batch_no: int) -> None:
            nonlocal retries_total
            max_retries = 3
            backoff = 5
            for attempt in range(max_retries):
                try:
                    await client.upload_documents(payload)
                    return
                except Exception as e:
                    if attempt < max_retries - 1:
                        retries_total += 1
                        wait = backoff * (attempt + 1)
                        print(f"Batch {batch_no} failed (attempt {attempt + 1}/{max_retries}), retrying in {wait}s: {e}")
                        await asyncio.sleep(wait)
                        continue
                    raise

        with open(embeddings_file, newline='', encoding="utf-8") as fp:
            reader = csv.DictReader(fp)
            for row in reader:
                if row_index < resume_from:
                    row_index += 1
                    skipped_docs += 1
                    continue

                document = {
                    'chunk_id': row.get('chunk_id', str(row_index)),
                    'chunk': row['chunk'],
                    'text_vector': json.loads(row['embedding'])
                }

                for _, field_name, is_collection in self.METADATA_FIELDS:
                    value = row.get(field_name, "")
                    if not value:
                        continue
                    if is_collection:
                        document[field_name] = [item.strip() for item in value.split(';') if item.strip()]
                    else:
                        document[field_name] = value

                documents.append(document)
                row_index += 1

                if len(documents) >= batch_size:
                    batches += 1
                    print(f"Uploading batch {batches} of {len(documents)} documents...")
                    await upload_batch(documents, batches)
                    uploaded_docs += len(documents)
                    with open(checkpoint_path, "w", encoding="utf-8") as cp:
                        json.dump({"last_row": row_index}, cp)
                    documents = []

        if documents:
            batches += 1
            print(f"Uploading final batch {batches} of {len(documents)} documents...")
            await upload_batch(documents, batches)
            uploaded_docs += len(documents)
            with open(checkpoint_path, "w", encoding="utf-8") as cp:
                json.dump({"last_row": row_index}, cp)

        if os.path.exists(checkpoint_path):
            os.remove(checkpoint_path)

        total_processed = uploaded_docs + skipped_docs
        print(f"Upload summary -> docs processed: {total_processed}, uploaded: {uploaded_docs}, skipped(resume): {skipped_docs}, batches: {batches}, retries: {retries_total}")

    async def is_index_empty(self) -> bool:
        """
        Return True if the index is empty.

        :return: True f index is empty.
        """
        if self._index is None:
            raise ValueError(
                "Unable to perform the operation as the index is absent. "
                "To create index please call create_index")
        document_count = await self._get_client().get_document_count()
        return document_count == 0

    def _raise_if_no_index(self) -> None:
        """
        Raise the exception if the index was not created.

        :raises: ValueError
        """
        if self._index is None:
            raise ValueError(
                "Unable to perform the operation as the index is absent. "
                "To create index please call create_index")

    async def delete_index(self):
        """Delete the index from vector store."""
        self._raise_if_no_index()
        async with SearchIndexClient(endpoint=self._endpoint, credential=self._credential) as ix_client:
            await ix_client.delete_index(self._index.name)
        self._index = None

    def _check_dimensions(self, vector_index_dimensions: Optional[int] = None) -> int:
        """
        Check that the dimensions are set correctly.

        :return: the correct vector index dimensions.
        :raises: Value error if both dimensions of embedding model and vector_index_dimensions are not set
                 or both of them set and they do not equal each other.
        """
        if vector_index_dimensions is None:
            if self._dimensions is None:
                raise ValueError(
                    "No embedding dimensions were provided in neither dimensions in the constructor nor in vector_index_dimensions"
                    "Dimensions are needed to build the search index, please provide the vector_index_dimensions.")
            vector_index_dimensions = self._dimensions
        if self._dimensions is not None and vector_index_dimensions != self._dimensions:
            raise ValueError("vector_index_dimensions is different from dimensions provided to constructor.")
        return vector_index_dimensions

    async def ensure_index_created(self, vector_index_dimensions: Optional[int] = None) -> None:
        """
        Get the search index. Create the index if it does not exist.

        :param vector_index_dimensions: The number of dimensions in the vector index. This parameter is
               needed if the embedding parameter cannot be set for the given model. It can be
               figured out by loading the embeddings file, generated by build_embeddings_file,
               loading the contents of the first row and 'embedding' column as a JSON and calculating
               the length of the list obtained.
               Also please see the embedding model documentation
               https://platform.openai.com/docs/models#embeddings
        :raises: Value error if both dimensions of embedding model and vector_index_dimensions are not set
                 or both of them set and they do not equal each other.
        """
        vector_index_dimensions = self._check_dimensions(vector_index_dimensions)
        if self._index is None:
            self._index = await SearchIndexManager.get_or_create_index(
                self._endpoint,
                self._credential,
                self._index_name,
                vector_index_dimensions,
                self._semantic_config_name)

    @staticmethod
    async def index_exists(
        endpoint: str,
        credential: Union[AsyncTokenCredential, AzureKeyCredential],
        index_name: str) -> bool:
        """
        Check if index exists.

        :param endpoint: The search end point to be used.
        :param credential: The credential to be used for the search.
        :param index_name: The name of an index to get or to create.
        :return: True if index already exists.
        """
        exists = False
        async with SearchIndexClient(endpoint=endpoint, credential=credential) as ix_client:
            try:
                await ix_client.get_index(index_name)
                exists = True
            except ResourceNotFoundError:
                pass
        return exists

    @staticmethod
    async def get_or_create_index(
            endpoint: str,
            credential: Union[AsyncTokenCredential, AzureKeyCredential],
            index_name: str,
            dimensions: int,
            semantic_config_name: str = "semantic-docs",
        ) -> SearchIndex:
        """
        Get o create the search index.

        **Note:** If the search index with index_name exists, the embeddings_file will not be uploaded.
        :param endpoint: The search end point to be used.
        :param credential: The credential to be used for the search.
        :param index_name: The name of an index to get or to create.
        :param dimensions: The number of dimensions in the embedding.
        :return: the search index object.
        """
        index = None
        async with SearchIndexClient(endpoint=endpoint, credential=credential) as ix_client:
            try:
                index = await ix_client.get_index(index_name)
            except ResourceNotFoundError:
                pass
        if index is None:
            index = await SearchIndexManager._index_create(
                endpoint=endpoint,
                credential=credential,
                index_name=index_name,
                dimensions=dimensions,
                semantic_config_name=semantic_config_name
            )
        return index

    async def create_index(
        self,
        vector_index_dimensions: Optional[int] = None) -> bool:
        """
        Create index or return false if it already exists.

        :param vector_index_dimensions: The number of dimensions in the vector index. This parameter is
               needed if the embedding parameter cannot be set for the given model. It can be
               figured out by loading the embeddings file, generated by build_embeddings_file,
               loading the contents of the first row and 'embedding' column as a JSON and calculating
               the length of the list obtained.
               Also please see the embedding model documentation
               https://platform.openai.com/docs/models#embeddings
        :return: True if index was created, False otherwise.
        :raises: Value error if both dimensions of embedding model and vector_index_dimensions are not set
                 or both of them are set and they do not equal each other.
        """
        vector_index_dimensions = self._check_dimensions(vector_index_dimensions)
        try:
            self._index = await SearchIndexManager._index_create(
                endpoint=self._endpoint,
                credential=self._credential,
                index_name=self._index_name,
                dimensions=vector_index_dimensions,
                semantic_config_name=self._semantic_config_name
            )
            return True
        except HttpResponseError:
            return False
        

    @staticmethod
    async def _index_create(
        endpoint: str,
        credential: Union[AsyncTokenCredential, AzureKeyCredential],
        index_name: str,
        dimensions: int,
        semantic_config_name: str = "semantic-docs") -> SearchIndex:
        """Create the index with semantic search enabled."""
        async with SearchIndexClient(endpoint=endpoint, credential=credential) as ix_client:
            fields = [
                SimpleField(name="chunk_id", type=SearchFieldDataType.String, key=True, searchable=True),
                SearchField(
                    name="text_vector",
                    type=SearchFieldDataType.Collection(SearchFieldDataType.Single),
                    vector_search_dimensions=dimensions,
                    searchable=True,
                    vector_search_profile_name="embedding_config"
                ),
                SearchField(name="chunk", type=SearchFieldDataType.String, hidden=False, searchable=True),
                SimpleField(name="title", type=SearchFieldDataType.String, searchable=True, filterable=True),
                SimpleField(name="ms_date", type=SearchFieldDataType.String, searchable=True, filterable=True, sortable=True),
                SimpleField(name="customer_intent", type=SearchFieldDataType.String, searchable=True, filterable=True),
                SimpleField(name="ms_topic", type=SearchFieldDataType.String, searchable=True, filterable=True),
                SimpleField(name="ms_service", type=SearchFieldDataType.String, searchable=True, filterable=True),
                SearchField(name="ms_collection", type=SearchFieldDataType.Collection(SearchFieldDataType.String), searchable=True, filterable=True),
                SimpleField(name="description", type=SearchFieldDataType.String, searchable=True),
                SimpleField(name="audience", type=SearchFieldDataType.String, searchable=True, filterable=True),
                SimpleField(name="ms_product", type=SearchFieldDataType.String, searchable=True, filterable=True),
            ]
            
            # Configure vector search
            vector_search = VectorSearch(
                profiles=[VectorSearchProfile(name="embedding_config",
                                              algorithm_configuration_name="embed-algorithms-config")],
                algorithms=[HnswAlgorithmConfiguration(name="embed-algorithms-config")],
            )
            
            # Configure semantic search
            semantic_search = None
            if semantic_config_name:
                content_fields = [SemanticField(field_name="chunk")]
                for _, field_name, _ in SearchIndexManager.METADATA_FIELDS:
                    if field_name != "title":
                        content_fields.append(SemanticField(field_name=field_name))

                semantic_config = SemanticConfiguration(
                    name=semantic_config_name,
                    prioritized_fields=SemanticPrioritizedFields(
                        title_field=SemanticField(field_name="title"),
                        content_fields=content_fields
                    )
                )
                semantic_search = SemanticSearch(configurations=[semantic_config])
            
            search_index = SearchIndex(
                name=index_name, 
                fields=fields, 
                vector_search=vector_search,
                semantic_search=semantic_search
            )
            new_index = await ix_client.create_index(search_index)
        return new_index

    @staticmethod
    def _extract_front_matter(content: str) -> tuple[dict, str]:
        """Split YAML front matter from markdown body."""
        lines = content.splitlines()
        if not lines or lines[0].strip() != "---":
            # Try to find H1 title if no front matter
            title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
            if title_match:
                return {"title": title_match.group(1).strip()}, content
            return {}, content

        closing_index = None
        for idx in range(1, len(lines)):
            if lines[idx].strip() == "---":
                closing_index = idx
                break

        if closing_index is None:
            return {}, content

        front_matter_raw = "\n".join(lines[1:closing_index])
        body = "\n".join(lines[closing_index + 1:])

        try:
            parsed = yaml.safe_load(front_matter_raw) or {}
        except yaml.YAMLError:
            parsed = {}
            
        # If title is missing in YAML, try to find H1 in body
        if "title" not in parsed:
            title_match = re.search(r'^#\s+(.+)$', body, re.MULTILINE)
            if title_match:
                parsed["title"] = title_match.group(1).strip()

        return parsed, body

    @classmethod
    def _normalize_metadata(cls, metadata: dict) -> tuple[list[str], dict]:
        """Normalize configured metadata fields to strings and a deterministic prefix."""
        prefix_lines: list[str] = []
        normalized: dict = {}

        for raw_name, field_name, is_collection in cls.METADATA_FIELDS:
            if metadata is None:
                continue
            value = metadata.get(raw_name)
            if value is None:
                continue

            if is_collection:
                if isinstance(value, str):
                    values = [item.strip() for item in value.split(',') if item.strip()]
                elif isinstance(value, (list, tuple, set)):
                    values = [str(item).strip() for item in value if str(item).strip()]
                else:
                    values = [str(value).strip()]
                if not values:
                    continue
                value_str = "; ".join(values)
            else:
                value_str = str(value).strip()

            if not value_str:
                continue

            prefix_lines.append(f"{raw_name}: {value_str}")
            normalized[field_name] = value_str

        return prefix_lines, normalized


    async def build_embeddings_file(
            self,
            input_directory: str,
            output_file: str,
            sentences_per_embedding: int=4
            ) -> None:
        """
        In this method we do lazy loading of nltk and download the needed data set to split

        document into tokens. This operation takes time that is why we hide import nltk under this
        method. We also do not include nltk into requirements because this method is only used
        during rag generation.
        :param dimensions: The number of dimensions in the embeddings. Must be the same as
               the one used for SearchIndexManager creation.
        :param input_directory: The directory with the embedding files.
        :param output_file: The file csv file to store embeddings.
        :param embeddings_client: The embedding client, used to create embeddings. 
                Must be the same as the one used for SearchIndexManager creation.
        :param sentences_per_embedding: The number of sentences used to build embedding.
        :param model: The embedding model to be used.
        """
        import nltk
        nltk.download('punkt')

        from nltk.tokenize import sent_tokenize

        chunks: list[dict] = []
        max_chunk_chars = int(os.getenv("MAX_CHUNK_CHARS", "6000"))
        chunk_mode = os.getenv("CHUNK_MODE", "sentences")  # "sentences" (default) or "pages"
        max_page_length = int(os.getenv("MAX_PAGE_LENGTH", "2000"))
        page_overlap_length = int(os.getenv("PAGE_OVERLAP_LENGTH", "500"))
        sentence_chunk_overlap = int(os.getenv("SENTENCE_CHUNK_OVERLAP", "0"))
        truncated_chunks = 0

        # Recursively pick up markdown files in nested folders (e.g., blob prefix subdirectories)
        globs = glob.glob(os.path.join(input_directory, '**', '*.md'), recursive=True)
        print(f"Found {len(globs)} markdown files under {input_directory}")

        for fle in globs:
            with open(fle, encoding="utf-8") as f:
                content = f.read()

            metadata, body = self._extract_front_matter(content)
            prefix_lines, normalized_metadata = self._normalize_metadata(metadata)
            prefix_text = "\n".join(prefix_lines) if prefix_lines else ""

            if chunk_mode == "pages":
                # Aligns with portal SplitSkill textSplitMode=pages style chunking
                full_text = f"{prefix_text}\n\n{body}" if prefix_text else body
                start = 0
                while start < len(full_text):
                    end = min(start + max_page_length, len(full_text))
                    chunk_text = full_text[start:end]
                    if len(chunk_text) > max_chunk_chars:
                        truncated_chunks += 1
                        chunk_text = chunk_text[:max_chunk_chars]
                    chunks.append({
                        "text": chunk_text,
                        "metadata": normalized_metadata
                    })
                    if end == len(full_text):
                        break
                    # slide with overlap
                    start = max(end - page_overlap_length, end)
            else:
                sentences = sent_tokenize(body)
                buffer: list[str] = []
                for sentence in sentences:
                    sentence = sentence.strip()
                    if len(sentence) < SearchIndexManager.MIN_LINE_LENGTH or len(set(sentence)) < SearchIndexManager.MIN_DIFF_CHARACTERS_IN_LINE:
                        continue
                    buffer.append(sentence)
                    if len(buffer) == sentences_per_embedding:
                        chunk_body = " ".join(buffer)
                        chunk_text = f"{prefix_text}\n\n{chunk_body}" if prefix_text else chunk_body
                        if len(chunk_text) > max_chunk_chars:
                            truncated_chunks += 1
                            chunk_text = chunk_text[:max_chunk_chars]
                        chunks.append({
                            "text": chunk_text,
                            "metadata": normalized_metadata
                        })
                        buffer = buffer[-sentence_chunk_overlap:] if sentence_chunk_overlap else []

                if buffer:
                    chunk_body = " ".join(buffer)
                    chunk_text = f"{prefix_text}\n\n{chunk_body}" if prefix_text else chunk_body
                        if len(chunk_text) > max_chunk_chars:
                            truncated_chunks += 1
                            chunk_text = chunk_text[:max_chunk_chars]
                    chunks.append({
                        "text": chunk_text,
                        "metadata": normalized_metadata
                    })

        # For each chunk build the embedding, which will be used in the search.
            if chunks:
                lengths = sorted(len(c["text"]) for c in chunks)
                p95_index = max(int(len(lengths) * 0.95) - 1, 0)
                p95 = lengths[p95_index]
                avg = sum(lengths) / len(lengths)
                print(f"Chunk stats -> count: {len(chunks)}, avg chars: {avg:.1f}, p95 chars: {p95}, max chars: {lengths[-1]}, truncated: {truncated_chunks}")
            else:
                print("Chunk stats -> no chunks produced; check input documents and filters.")

        batch_size = 10
        total_chunks = len(chunks)
        total_batches = (total_chunks + batch_size - 1) // batch_size
        print(f"Embedding {total_chunks} chunks across {total_batches} batches (batch size {batch_size})")
        fieldnames = ['chunk_id', 'chunk', 'embedding'] + [field_name for _, field_name, _ in self.METADATA_FIELDS]
        with open(output_file, 'w', encoding="utf-8", newline='') as fp:
            writer = csv.DictWriter(fp, fieldnames=fieldnames)
            writer.writeheader()
            for i in range(0, len(chunks), batch_size):
                batch_number = (i // batch_size) + 1
                batch = chunks[i:i+batch_size]
                
                # Add a small delay between batches to avoid hitting rate limits
                if i > 0:
                    await asyncio.sleep(1)

                retries = 5
                for attempt in range(retries):
                    try:
                        if isinstance(self._embeddings_client, EmbeddingsClient):
                            embedding_response = (await self._embeddings_client.embed(
                                input=[chunk['text'] for chunk in batch],
                                dimensions=self._dimensions,
                                model=self._model
                            ))["data"]
                            embeddings = [item['embedding'] for item in embedding_response]
                        else:
                            # AsyncAzureOpenAI
                            kwargs = {"dimensions": self._dimensions} if self._dimensions else {}
                            response = await self._embeddings_client.embeddings.create(
                                input=[chunk['text'] for chunk in batch],
                                model=self._model,
                                **kwargs
                            )
                            embeddings = [item.embedding for item in response.data]
                        break
                    except Exception as e:
                        if "RateLimitReached" in str(e) or "429" in str(e):
                            if attempt < retries - 1:
                                # Increase wait time significantly as requested by the API (often 60s)
                                wait_time = 60 + (attempt * 10)
                                print(f"Rate limit hit. Retrying batch {batch_number} in {wait_time}s...")
                                await asyncio.sleep(wait_time)
                                continue
                        raise e

                print(f"Completed batch {batch_number}/{total_batches} ({min(i+batch_size, total_chunks)}/{total_chunks} chunks)")

                for offset, (chunk, embedding) in enumerate(zip(batch, embeddings)):
                    row = {
                        'chunk_id': str(i + offset),
                        'chunk': chunk['text'],
                        'embedding': json.dumps(embedding)
                    }
                    for _, field_name, _ in self.METADATA_FIELDS:
                        row[field_name] = chunk['metadata'].get(field_name, "")
                    writer.writerow(row)

    async def close(self):
        """Close the closeable resources, associated with SearchIndexManager."""
        if self._client:
            await self._client.close()
