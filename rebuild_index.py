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
from azure.identity.aio import DefaultAzureCredential
from azure.storage.blob.aio import BlobServiceClient
from azure.ai.inference.aio import EmbeddingsClient
from src.api.search_index_manager import SearchIndexManager
from openai import AsyncAzureOpenAI
from azure.identity import get_bearer_token_provider

# Download NLTK data
import nltk
nltk.download('punkt_tab', quiet=True)


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
    return parser.parse_args()


async def main(args):
    # Configuration
    storage_account_name = os.getenv("AZURE_STORAGE_ACCOUNT_NAME", "stzpz5xvg2elsve")
    container_name = os.getenv("AZURE_STORAGE_CONTAINER_NAME")  # You need to provide this
    blob_prefix = os.getenv("AZURE_STORAGE_BLOB_PREFIX", "")  # Optional: restrict to a subfolder
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
            azure_ad_token_provider=token_provider
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
    )
    
    # Build embeddings file
    print("\n4. Building embeddings from downloaded documents...")
    embeddings_file = args.embeddings_file

    if os.path.exists(embeddings_file) and not args.force_embeddings:
        print(f"  Found existing embeddings file: {embeddings_file}. Skipping generation.")
    else:
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
    if hasattr(credential, 'close'):
        await credential.close()
    if hasattr(token_credential, 'close') and token_credential != credential:
        await token_credential.close()
    await embeddings_client.close()
    await search_index_manager.close()

if __name__ == "__main__":
    cli_args = parse_args()
    asyncio.run(main(cli_args))
