import asyncio
import os
from azure.core.credentials import AzureKeyCredential
from azure.search.documents.indexes.aio import SearchIndexClient


def _require_env(var_name: str) -> str:
    value = os.getenv(var_name)
    if not value:
        raise RuntimeError(f"Missing required environment variable: {var_name}")
    return value


async def main():
    endpoint = _require_env("AZURE_SEARCH_ENDPOINT")
    key = _require_env("AZURE_SEARCH_ADMIN_KEY")
    index_name = _require_env("AZURE_SEARCH_INDEX_NAME")

    credential = AzureKeyCredential(key)
    client = SearchIndexClient(endpoint=endpoint, credential=credential)

    try:
        index = await client.get_index(index_name)
        print("Fields:", [f.name for f in index.fields])
    finally:
        await client.close()


if __name__ == "__main__":
    asyncio.run(main())