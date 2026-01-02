import asyncio
import os
from azure.identity.aio import AzureDeveloperCliCredential
from azure.search.documents.indexes.aio import SearchIndexClient
from dotenv import load_dotenv

load_dotenv(dotenv_path="/workspaces/get-started-with-ai-chat/.azure/lmc-doc-chat/.env")

async def main():
    endpoint = os.getenv("AZURE_AI_SEARCH_ENDPOINT")
    index_name = os.getenv("AZURE_AI_SEARCH_INDEX_NAME")
    search_key = os.getenv("AZURE_SEARCH_ADMIN_KEY")
    
    from azure.core.credentials import AzureKeyCredential
    if search_key:
        credential = AzureKeyCredential(search_key)
    else:
        credential = AzureDeveloperCliCredential()
        
    client = SearchIndexClient(endpoint=endpoint, credential=credential)
    
    print(f"Deleting index {index_name}...")
    try:
        await client.delete_index(index_name)
        print("Index deleted.")
    except Exception as e:
        print(f"Error deleting index: {e}")
    finally:
        await client.close()
        if hasattr(credential, 'close'):
            await credential.close()

if __name__ == "__main__":
    asyncio.run(main())
