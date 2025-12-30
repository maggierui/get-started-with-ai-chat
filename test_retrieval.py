import asyncio
import os
from azure.core.credentials import AzureKeyCredential
from azure.search.documents.aio import SearchClient
from azure.search.documents.models import VectorizedQuery
from openai import AsyncAzureOpenAI
from azure.identity import AzureDeveloperCliCredential, get_bearer_token_provider


def _require_env(var_name: str) -> str:
    value = os.getenv(var_name)
    if not value:
        raise RuntimeError(f"Missing required environment variable: {var_name}")
    return value


async def main():
    # Configuration
    endpoint = _require_env("AZURE_SEARCH_ENDPOINT")
    key = _require_env("AZURE_SEARCH_ADMIN_KEY")
    index_name = _require_env("AZURE_SEARCH_INDEX_NAME")
    aoai_endpoint = _require_env("AZURE_OPENAI_ENDPOINT")
    aoai_api_version = os.getenv("AZURE_OPENAI_API_VERSION", "2023-05-15")
    
    # Setup AOAI Client
    credential = AzureDeveloperCliCredential()
    token_provider = get_bearer_token_provider(credential, "https://cognitiveservices.azure.com/.default")
    
    aoai_client = AsyncAzureOpenAI(
        azure_endpoint=aoai_endpoint,
        api_version=aoai_api_version,
        azure_ad_token_provider=token_provider
    )
    
    # Setup Search Client
    search_client = SearchClient(endpoint=endpoint, index_name=index_name, credential=AzureKeyCredential(key))
    
    query = "How do I configure external sharing?"
    print(f"Query: {query}\n")
    
    try:
        # Generate Embedding
        print("Generating embedding...")
        embedding_response = await aoai_client.embeddings.create(
            input=query,
            model="text-embedding-3-large",
            dimensions=3072
        )
        embedding = embedding_response.data[0].embedding
        
        # Execute Search
        print("Searching index...")
        vector_query = VectorizedQuery(vector=embedding, k_nearest_neighbors=3, fields="text_vector")
        
        results = await search_client.search(
            search_text=query,
            vector_queries=[vector_query],
            select=["title", "chunk", "ms_service", "ms_product", "ms_topic"],
            top=3
        )
        
        print("\nResults:")
        async for result in results:
            print(f"Title: {result.get('title')}")
            print(f"Topic: {result.get('ms_topic')}")
            print(f"Service: {result.get('ms_service')}")
            print(f"Chunk snippet: {result.get('chunk')[:150].replace(chr(10), ' ')}...")
            print("-" * 40)
            
    finally:
        await search_client.close()
        await aoai_client.close()


if __name__ == "__main__":
    asyncio.run(main())