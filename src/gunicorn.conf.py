# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license.
# See LICENSE file in the project root for full license information.
import asyncio
import multiprocessing
import os

from azure.identity.aio import DefaultAzureCredential


async def create_index_maybe():
    """
    Create the index and upload documents if the index does not exist.

    This code is executed only once, when called on_starting hook is being
    called. This code ensures that the index is being populated only once.
    rag.create_index return True if the index was created, meaning that this
    docker node have started first and must populate index.
    """
    from api.search_index_manager import SearchIndexManager
    async with DefaultAzureCredential() as creds:
        endpoint = os.environ.get('AZURE_AI_SEARCH_ENDPOINT')
        if endpoint:
            search_mgr = SearchIndexManager(
                endpoint=endpoint,
                credential=creds,
                index_name=os.getenv('AZURE_AI_SEARCH_INDEX_NAME'),
                dimensions=None,
                model=os.getenv('AZURE_AI_EMBED_DEPLOYMENT_NAME'),
                embeddings_client=None,
                semantic_config_name=os.getenv('AZURE_AI_SEARCH_SEMANTIC_CONFIG_NAME', 'semantic-docs')
            )
            # If another application instance already have created the index,
            # do not upload the documents.
            # Also skip upload if explicitly disabled (e.g. when using external indexers)
            skip_upload = os.getenv('SKIP_RAG_DATA_UPLOAD', 'false').lower() == 'true'
            
            if not skip_upload and await search_mgr.create_index(
              vector_index_dimensions=int(
                  os.getenv('AZURE_AI_EMBED_DIMENSIONS'))):
                embeddings_path = os.path.join(
                    os.path.dirname(__file__), 'api', 'data', 'embeddings.csv')
                assert embeddings_path, f'File {embeddings_path} not found.'
                await search_mgr.upload_documents(embeddings_path)
                await search_mgr.close()


def on_starting(server):
    """Server hook, called just before the master process is initialized."""
    asyncio.get_event_loop().run_until_complete(create_index_maybe())


max_requests = 1000
max_requests_jitter = 50
log_file = "-"
bind = "0.0.0.0:50505"

if not os.getenv("RUNNING_IN_PRODUCTION"):
    reload = True

# Load application code before the worker processes are forked.
# Needed to execute on_starting.
# Please see the documentation on gunicorn
# https://docs.gunicorn.org/en/stable/settings.html
preload_app = True
num_cpus = multiprocessing.cpu_count()
workers = (num_cpus * 2) + 1
worker_class = "uvicorn.workers.UvicornWorker"

timeout = 120


if __name__ == "__main__":
    print("Running initialize_resources directly...")
    asyncio.run(create_index_maybe())
    print("initialize_resources finished.")