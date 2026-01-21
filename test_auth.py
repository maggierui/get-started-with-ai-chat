
import os
import asyncio
from azure.identity.aio import AzureDeveloperCliCredential
from azure.storage.blob.aio import BlobServiceClient
from azure.search.documents.indexes.aio import SearchIndexClient
from azure.core.credentials import AzureKeyCredential
from dotenv import load_dotenv

load_dotenv(".azure/lmc-doc-chat/.env")

async def test_storage():
    print("Testing Storage...")
    account = os.environ["AZURE_STORAGE_ACCOUNT_NAME"]
    container = os.environ["AZURE_STORAGE_CONTAINER_NAME"]
    url = f"https://{account}.blob.core.windows.net"
    cred = AzureDeveloperCliCredential()
    try:
        async with BlobServiceClient(url, credential=cred) as client:
            container_client = client.get_container_client(container)
            count = 0
            async for blob in container_client.list_blobs():
                count += 1
        print(f"Storage OK. Blobs found: {count}")
    except Exception as e:
        print(f"Storage FAILED: {e}")
    finally:
        await cred.close()

async def test_search():
    print("\nTesting Search...")
    endpoint = os.environ["AZURE_AI_SEARCH_ENDPOINT"]
    key = os.environ.get("AZURE_SEARCH_ADMIN_KEY")
    if key:
        cred = AzureKeyCredential(key)
        print("Using Key for Search")
    else:
        cred = AzureDeveloperCliCredential()
        print("Using Token for Search")

    try:
        async with SearchIndexClient(endpoint, credential=cred) as client:
            indexes = []
            async for idx in client.list_indexes():
                indexes.append(idx.name)
        print(f"Search OK. Indexes: {indexes}")
    except Exception as e:
        print(f"Search FAILED: {e}")
    finally:
        if not key:
            await cred.close()

async def main():
    await test_storage()
    await test_search()

if __name__ == "__main__":
    asyncio.run(main())
