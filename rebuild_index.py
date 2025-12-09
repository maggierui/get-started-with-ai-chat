"""
Script to rebuild the search index with documents from Azure Storage.
This script will:
1. Download documents from Azure Storage blob
2. Build embeddings using text-embedding-3-large
3. Create a new search index
4. Upload the embeddings to the index
"""

import asyncio
import os
from pathlib import Path
from azure.identity.aio import DefaultAzureCredential
from azure.storage.blob.aio import BlobServiceClient
from azure.ai.inference.aio import EmbeddingsClient
from src.api.search_index_manager import SearchIndexManager

# Download NLTK data
import nltk
nltk.download('punkt_tab', quiet=True)


async def main():
    # Configuration
    storage_account_name = os.getenv("AZURE_STORAGE_ACCOUNT_NAME", "stzpz5xvg2elsve")
    container_name = os.getenv("AZURE_STORAGE_CONTAINER_NAME")  # You need to provide this
    search_endpoint = os.getenv("AZURE_AI_SEARCH_ENDPOINT")
    index_name = os.getenv("AZURE_AI_SEARCH_INDEX_NAME")
    embed_deployment = os.getenv("AZURE_AI_EMBED_DEPLOYMENT_NAME", "text-embedding-3-large")
    embed_dimensions = int(os.getenv("AZURE_AI_EMBED_DIMENSIONS", "3072"))
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
    print(f"  Embedding Model: {embed_deployment}")
    print(f"  Embedding Dimensions: {embed_dimensions}")
    print(f"  AI Project Endpoint: {ai_project_endpoint}")
    
    # Create credential - use AzureDeveloperCliCredential for local development
    from azure.identity.aio import AzureDeveloperCliCredential
    credential = AzureDeveloperCliCredential()
    
    # Download documents from blob storage
    print("\n1. Downloading .md documents from blob storage...")
    download_dir = Path("./downloaded_documents")
    download_dir.mkdir(exist_ok=True)
    
    storage_url = f"https://{storage_account_name}.blob.core.windows.net"
    async with BlobServiceClient(account_url=storage_url, credential=credential) as blob_service_client:
        container_client = blob_service_client.get_container_client(container_name)
        
        blob_count = 0
        async for blob in container_client.list_blobs():
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
    embeddings_client = EmbeddingsClient(
        endpoint=ai_project_endpoint,
        credential=credential,
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
    )
    
    # Build embeddings file
    print("\n4. Building embeddings from downloaded documents...")
    embeddings_file = "./embeddings.csv"
    await search_index_manager.build_embeddings_file(
        input_directory=str(download_dir),
        output_file=embeddings_file,
        sentences_per_embedding=4
    )
    print(f"  Embeddings saved to: {embeddings_file}")
    
    # Create the index
    print("\n5. Creating search index...")
    await search_index_manager.ensure_index_created(embed_dimensions)
    print(f"  Index '{index_name}' created successfully")
    
    # Upload documents to the index
    print("\n6. Uploading embeddings to search index...")
    await search_index_manager.upload_documents(embeddings_file)
    print("  Upload complete!")
    
    print("\n✅ Index rebuild complete!")
    print(f"Your search index '{index_name}' is ready to use.")
    
    # Cleanup
    await credential.close()
    await embeddings_client.close()


if __name__ == "__main__":
    asyncio.run(main())
