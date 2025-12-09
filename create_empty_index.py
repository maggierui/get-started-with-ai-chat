"""
Simple test script to create the index and upload sample data.
This bypasses the embedding generation to test if the basic setup works.
"""

import asyncio
import os
from azure.identity.aio import AzureDeveloperCliCredential  
from src.api.search_index_manager import SearchIndexManager
from azure.ai.inference.aio import EmbeddingsClient


async def main():
    # Configuration from environment
    search_endpoint = os.getenv("AZURE_AI_SEARCH_ENDPOINT")
    index_name = os.getenv("AZURE_AI_SEARCH_INDEX_NAME")
    embed_deployment = os.getenv("AZURE_AI_EMBED_DEPLOYMENT_NAME", "text-embedding-3-large")
    embed_dimensions = int(os.getenv("AZURE_AI_EMBED_DIMENSIONS", "3072"))
    ai_project_endpoint = os.getenv("AZURE_EXISTING_AIPROJECT_ENDPOINT")
    
    print(f"Creating index with {embed_dimensions} dimensions...")
    print(f"Search Endpoint: {search_endpoint}")
    print(f"Index Name: {index_name}")
    
    # Create credential
    credential = AzureDeveloperCliCredential()
    
    # Create embeddings client (needed for SearchIndexManager init, even if we don't use it)
    embeddings_client = EmbeddingsClient(
        endpoint=ai_project_endpoint,
        credential=credential,
    )
    
    # Create search index manager
    search_index_manager = SearchIndexManager(
        endpoint=search_endpoint,
        credential=credential,
        index_name=index_name,
        dimensions=embed_dimensions,
        model=embed_deployment,
        embeddings_client=embeddings_client,
    )
    
    # Create the index
    print("\nCreating search index...")
    await search_index_manager.ensure_index_created(embed_dimensions)
    print(f"✅ Index '{index_name}' created successfully with {embed_dimensions}-dimensional vectors")
    
    # Cleanup
    await credential.close()
    await embeddings_client.close()


if __name__ == "__main__":
    asyncio.run(main())
