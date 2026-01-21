"""
Script to rebuild the search index with documents from Azure Storage.
This script will:
1. Download documents from Azure Storage blob (optional skip)
2. Build embeddings using text-embedding-3-large (optional reuse/skip)
3. Create a new search index
4. Upload the embeddings to the index
"""

import argparse
import asyncio
import os
from pathlib import Path
import hashlib
import json
from azure.identity.aio import DefaultAzureCredential
from azure.storage.blob.aio import BlobServiceClient
from azure.ai.inference.aio import EmbeddingsClient
from azure.search.documents.indexes.aio import SearchIndexClient
from src.api.search_index_manager import SearchIndexManager
from openai import AsyncAzureOpenAI
from azure.identity import get_bearer_token_provider
from azure.core.exceptions import ResourceNotFoundError

# Download NLTK data
import nltk
nltk.download('punkt_tab', quiet=True)
from dotenv import load_dotenv

# Load environment variables from the specific file
load_dotenv(".azure/lmc-doc-chat/.env", override=True)


async def validate_index_alignment(endpoint: str, credential, index_name: str, expected_dims: int, expected_semantic: str, vector_field: str) -> None:
    """Validate an existing index matches expected vector dimensions and semantic config.

    Abort early with a clear message if the live index diverges from env settings.
    """
    async with SearchIndexClient(endpoint=endpoint, credential=credential) as ix_client:
        try:
            index = await ix_client.get_index(index_name)
        except ResourceNotFoundError:
            print(f"Index '{index_name}' not found. A new index will be created.")
            return

        print(f"Found existing index '{index_name}'. Validating schema...")

        vector_field_def = next((f for f in index.fields if f.name == vector_field), None)
        live_dims = getattr(vector_field_def, "vector_search_dimensions", None) if vector_field_def else None
        if live_dims != expected_dims:
            raise RuntimeError(
                f"Index '{index_name}' vector dims {live_dims} do not match expected {expected_dims}. "
                "Please recreate the index to align with the configured embedding dimensions."
            )

        if expected_semantic:
            configs = (index.semantic_search.configurations if index.semantic_search else []) or []
            names = [c.name for c in configs]
            if expected_semantic not in names:
                raise RuntimeError(
                    f"Index '{index_name}' semantic configs {names or '[none]'} do not include expected "
                    f"'{expected_semantic}'. Please recreate the index with the correct semantic configuration."
                )

        print("Existing index matches expected dimensions and semantic configuration; reuse is allowed.")


async def summarize_blobs(storage_account: str, container: str, prefix: str, credential) -> tuple[int, int, str]:
    """Return counts and a stable hash of blob names/sizes for reuse checks."""
    storage_url = f"https://{storage_account}.blob.core.windows.net"
    total = 0
    markdown = 0
    hash_acc = hashlib.sha256()
    async with BlobServiceClient(account_url=storage_url, credential=credential) as client:
        container_client = client.get_container_client(container)
        blobs = []
        async for blob in container_client.list_blobs(name_starts_with=prefix or None):
            blobs.append(blob)
        # Sort for stable hashing regardless of service listing order
        for blob in sorted(blobs, key=lambda b: b.name):
            total += 1
            if blob.name.lower().endswith('.md'):
                markdown += 1
            size = getattr(blob, "size", 0) or 0
            hash_acc.update(f"{blob.name}:{size}".encode("utf-8"))
    inventory_hash = hash_acc.hexdigest()
    print(f"Blob inventory -> total: {total}, markdown: {markdown}, prefix: '{prefix or '[none]'}', hash: {inventory_hash}")
    return total, markdown, inventory_hash


def parse_args():
    parser = argparse.ArgumentParser(description="Rebuild Azure AI Search index from blob docs.")
    parser.add_argument(
        "--skip-download",
        action="store_true",
        help="Skip downloading blobs (reuse existing files in downloaded_documents)",
    )
    parser.add_argument(
        "--force-embeddings",
        action="store_true",
        help="Rebuild embeddings even if an embeddings file already exists",
    )
    parser.add_argument(
        "--embeddings-file",
        default="./embeddings.csv",
        help="Path to embeddings CSV (default: ./embeddings.csv)",
    )
    parser.add_argument(
        "--probe",
        default=None,
        help="Optional test query to run after upload; prints top 3 titles and chunk_ids",
    )
    return parser.parse_args()


async def main(args):
    # Configuration
    storage_account_name = os.getenv("AZURE_STORAGE_ACCOUNT_NAME", "stzpz5xvg2elsve")
    container_name = os.getenv("AZURE_STORAGE_CONTAINER_NAME")  # You need to provide this
    blob_prefix = os.getenv("AZURE_STORAGE_BLOB_PREFIX", "")  # Optional: restrict to a subfolder
    vector_field = os.getenv("AZURE_SEARCH_FIELD_VECTOR", "text_vector")
    search_endpoint = os.getenv("AZURE_AI_SEARCH_ENDPOINT")
    index_name = os.getenv("AZURE_AI_SEARCH_INDEX_NAME")
    embed_deployment = os.getenv("AZURE_AI_EMBED_DEPLOYMENT_NAME", "text-embedding-3-large")
    embed_dimensions = int(os.getenv("AZURE_AI_EMBED_DIMENSIONS", "3072"))
    semantic_config_name = os.getenv("AZURE_AI_SEARCH_SEMANTIC_CONFIG_NAME", "semantic-docs")
    ai_project_endpoint = os.getenv("AZURE_EXISTING_AIPROJECT_ENDPOINT")
    
    # Validate required environment variables
    if not all([container_name, search_endpoint, index_name, ai_project_endpoint]):
        print("ERROR: Missing required environment variables:")
        print(f"  AZURE_STORAGE_CONTAINER_NAME: {container_name}")
        print(f"  AZURE_AI_SEARCH_ENDPOINT: {search_endpoint}")
        print(f"  AZURE_AI_SEARCH_INDEX_NAME: {index_name}")
        print(f"  AZURE_EXISTING_AIPROJECT_ENDPOINT: {ai_project_endpoint}")
        return
    
    print(f"Configuration:")
    print(f"  Storage Account: {storage_account_name}")
    print(f"  Container: {container_name}")
    print(f"  Search Endpoint: {search_endpoint}")
    print(f"  Index Name: {index_name}")
    print(f"  Vector Field: {vector_field}")
    print(f"  Embedding Model: {embed_deployment}")
    print(f"  Embedding Dimensions: {embed_dimensions}")
    print(f"  Semantic Config: {semantic_config_name}")
    print(f"  AI Project Endpoint: {ai_project_endpoint}")
    print(f"  Blob Prefix: {blob_prefix or '[none]'}")
    
    # Create credential - use AzureDeveloperCliCredential for local development
    from azure.identity.aio import AzureDeveloperCliCredential
    from azure.core.credentials import AzureKeyCredential
    
    search_key = os.getenv("AZURE_SEARCH_ADMIN_KEY")
    if search_key:
        print("  Using Azure Search Admin Key for authentication")
        credential = AzureKeyCredential(search_key)
        # We still need a token credential for Blob Storage and AI Project if they use RBAC
        # But SearchIndexManager will use the key.
        # Wait, SearchIndexManager takes one credential.
        # If we pass KeyCredential, it works for Search.
        # But BlobServiceClient needs TokenCredential.
        # So we need two credentials.
        token_credential = AzureDeveloperCliCredential()
    else:
        credential = AzureDeveloperCliCredential()
        token_credential = credential

    # Validate existing index alignment before proceeding
    await validate_index_alignment(
        endpoint=search_endpoint,
        credential=credential,
        index_name=index_name,
        expected_dims=embed_dimensions,
        expected_semantic=semantic_config_name,
        vector_field=vector_field,
    )

    # Summarize blobs before any download to catch scope issues early
    _, _, inventory_hash = await summarize_blobs(
        storage_account=storage_account_name,
        container=container_name,
        prefix=blob_prefix,
        credential=token_credential,
    )
    
    # Download documents from blob storage
    download_dir = Path("./downloaded_documents")
    if args.skip_download:
        print("\n1. Skipping download (reusing existing downloaded_documents directory)")
    else:
        print("\n1. Downloading .md documents from blob storage...")
        download_dir.mkdir(exist_ok=True)
        storage_url = f"https://{storage_account_name}.blob.core.windows.net"
        async with BlobServiceClient(account_url=storage_url, credential=token_credential) as blob_service_client:
            container_client = blob_service_client.get_container_client(container_name)
            blob_count = 0
            async for blob in container_client.list_blobs(name_starts_with=blob_prefix or None):
                # Only download .md files
                if not blob.name.lower().endswith('.md'):
                    continue

                print(f"  Downloading: {blob.name}")
                blob_client = container_client.get_blob_client(blob.name)
                file_path = download_dir / blob.name
                file_path.parent.mkdir(parents=True, exist_ok=True)
                with open(file_path, "wb") as f:
                    download_stream = await blob_client.download_blob()
                    data = await download_stream.readall()
                    f.write(data)
                blob_count += 1

            print(f"  Downloaded {blob_count} .md files")
    
    # Create embeddings client
    print("\n2. Creating embeddings client...")
    
    # Normalize endpoint to the resource host (strip /api/projects/... if present)
    project_base_endpoint = ai_project_endpoint.split('/api')[0].rstrip('/') if ai_project_endpoint else None

    if any(host in ai_project_endpoint for host in ["cognitiveservices.azure.com", "openai.azure.com", "services.ai.azure.com"]):
        print(f"  Detected Azure OpenAI/Azure AI endpoint: {ai_project_endpoint}")
        # We need a synchronous credential for get_bearer_token_provider
        from azure.identity import AzureDeveloperCliCredential as SyncAzureDeveloperCliCredential
        sync_credential = SyncAzureDeveloperCliCredential()
        token_provider = get_bearer_token_provider(sync_credential, "https://cognitiveservices.azure.com/.default")
        
        embeddings_client = AsyncAzureOpenAI(
            azure_endpoint=project_base_endpoint,
            api_version="2023-05-15", 
            azure_ad_token_provider=token_provider,
            max_retries=10,
        )
    else:
        print(f"  Detected AI Project endpoint: {ai_project_endpoint}")
        embeddings_client = EmbeddingsClient(
            endpoint=ai_project_endpoint,
            credential=token_credential,
        )
    
    # Create search index manager
    print("\n3. Initializing search index manager...")
    search_index_manager = SearchIndexManager(
        endpoint=search_endpoint,
        credential=credential,
        index_name=index_name,
        dimensions=embed_dimensions,
        model=embed_deployment,
        embeddings_client=embeddings_client,
        semantic_config_name=semantic_config_name,
    )
    
    # Build embeddings file
    print("\n4. Building embeddings from downloaded documents...")
    embeddings_file = args.embeddings_file

    manifest_path = embeddings_file + ".manifest.json"
    reuse_embeddings = os.path.exists(embeddings_file) and not args.force_embeddings
    manifest = None
    if os.path.exists(manifest_path):
        try:
            with open(manifest_path, "r", encoding="utf-8") as mf:
                manifest = json.load(mf)
        except Exception:
            manifest = None

    if reuse_embeddings:
        if manifest and manifest.get("inventory_hash") == inventory_hash:
            print(f"  Reusing existing embeddings file: {embeddings_file} (inventory hash match)")
        else:
            reason = "manifest mismatch" if manifest else "missing manifest"
            print(f"  Existing embeddings file found but {reason}; regenerating to align with current blobs.")
            reuse_embeddings = False

    if not reuse_embeddings:
        await search_index_manager.build_embeddings_file(
            input_directory=str(download_dir),
            output_file=embeddings_file,
            sentences_per_embedding=4
        )
        print(f"  Embeddings saved to: {embeddings_file}")
        new_manifest = {
            "inventory_hash": inventory_hash,
            "container": container_name,
            "prefix": blob_prefix,
            "blob_account": storage_account_name,
        }
        with open(manifest_path, "w", encoding="utf-8") as mf:
            json.dump(new_manifest, mf, indent=2)
        print(f"  Wrote manifest: {manifest_path}")
    
    # Create the index
    print("\n5. Creating search index...")
    await search_index_manager.ensure_index_created(embed_dimensions)
    print(f"  Index '{index_name}' created successfully")
    
    # Upload documents to the index
    print("\n6. Uploading embeddings to search index...")
    await search_index_manager.upload_documents(embeddings_file)
    print("  Upload complete!")

    # Post-upload document count check
    with open(embeddings_file, newline='', encoding="utf-8") as fp:
        rows = sum(1 for _ in fp) - 1  # subtract header
    doc_count = await search_index_manager._get_client().get_document_count()
    if doc_count != rows:
        print(f"WARNING: Index document count ({doc_count}) != embeddings rows ({rows}). Consider re-uploading.")
    else:
        print(f"Validation: Index document count matches embeddings rows ({rows}).")

    # Optional probe query to sanity-check the index
    if args.probe:
        print(f"\n7. Running probe query: {args.probe}")
        vector_field = os.getenv("AZURE_SEARCH_FIELD_VECTOR", "text_vector")
        content_field = os.getenv("AZURE_SEARCH_FIELD_CONTENT", "chunk")
        query = args.probe
        embedded_question = (await embed.embed(
            input=query,
            dimensions=embed_dimensions,
            model=embed_deployment,
        ))["data"][0]["embedding"]

        vector_query = {
            "vector": embedded_question,
            "k_nearest_neighbors": 3,
            "fields": vector_field,
        }

        search_params = {
            "search_text": query,
            "vector_queries": [vector_query],
            "select": [content_field, "title", "chunk_id"],
            "top": 3,
        }

        if semantic_config_name:
            search_params["query_type"] = "semantic"
            search_params["semantic_configuration_name"] = semantic_config_name

        search_client = search_index_manager._get_client()
        results = await search_client.search(**search_params)
        print("Probe results (top 3):")
        idx = 1
        async for doc in results:
            title = doc.get("title", "Unknown")
            chunk_id = doc.get("chunk_id", "")
            snippet = (doc.get(content_field) or "")[:200].replace("\n", " ")
            print(f"  {idx}. title='{title}' chunk_id='{chunk_id}' snippet='{snippet}'")
            idx += 1
    
    print("\n✅ Index rebuild complete!")
    print(f"Your search index '{index_name}' is ready to use.")
    
    # Cleanup
    if hasattr(credential, 'close'):
        await credential.close()
    if hasattr(token_credential, 'close') and token_credential != credential:
        await token_credential.close()
    await embeddings_client.close()
    await search_index_manager.close()

if __name__ == "__main__":
    cli_args = parse_args()
    asyncio.run(main(cli_args))
