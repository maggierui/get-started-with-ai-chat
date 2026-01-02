# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license.
# See LICENSE file in the project root for full license information.
import contextlib
import logging
import os
from pathlib import Path
from typing import Union
from urllib.parse import urlparse

import fastapi
from azure.ai.projects.aio import AIProjectClient
from azure.ai.inference.aio import ChatCompletionsClient, EmbeddingsClient
from azure.core.credentials import AzureKeyCredential
from azure.identity import AzureDeveloperCliCredential, ManagedIdentityCredential
from dotenv import load_dotenv
from fastapi.staticfiles import StaticFiles

from .search_index_manager import SearchIndexManager
from .util import get_logger

logger = None
enable_trace = False

@contextlib.asynccontextmanager
async def lifespan(app: fastapi.FastAPI):
    azure_credential: Union[AzureDeveloperCliCredential, ManagedIdentityCredential]
    if not os.getenv("RUNNING_IN_PRODUCTION"):
        if tenant_id := os.getenv("AZURE_TENANT_ID"):
            logger.info("Using AzureDeveloperCliCredential with tenant_id %s", tenant_id)
            azure_credential = AzureDeveloperCliCredential(tenant_id=tenant_id)
        else:
            logger.info("Using AzureDeveloperCliCredential")
            azure_credential = AzureDeveloperCliCredential()
    else:
        # User-assigned identity was created and set in api.bicep
        user_identity_client_id = os.getenv("AZURE_CLIENT_ID")
        logger.info("Using ManagedIdentityCredential with client_id %s", user_identity_client_id)
        azure_credential = ManagedIdentityCredential(client_id=user_identity_client_id)

    endpoint = os.environ["AZURE_EXISTING_AIPROJECT_ENDPOINT"]
    project = AIProjectClient(
        credential=azure_credential,
        endpoint=endpoint,
    )

    if enable_trace:
        application_insights_connection_string = ""
        try:
            application_insights_connection_string = await project.telemetry.get_application_insights_connection_string()
        except Exception as e:
            e_string = str(e)
            logger.error("Failed to get Application Insights connection string, error: %s", e_string)
        if not application_insights_connection_string:
            logger.error("Application Insights was not enabled for this project.")
            logger.error("Enable it via the 'Tracing' tab in your AI Foundry project page.")
            exit()
        else:
            from azure.monitor.opentelemetry import configure_azure_monitor
            configure_azure_monitor(connection_string=application_insights_connection_string)


    # Project endpoint has the form:   https://your-ai-services-account-name.services.ai.azure.com/api/projects/your-project-name
    # Inference endpoint has the form: https://your-ai-services-account-name.services.ai.azure.com/models
    # Strip the "/api/projects/your-project-name" part and replace with "/models":
    inference_endpoint = f"https://{urlparse(endpoint).netloc}/models"

    chat =  ChatCompletionsClient(
        endpoint=inference_endpoint,
        credential=azure_credential,
        credential_scopes=["https://ai.azure.com/.default"],
    )
    embed =  EmbeddingsClient(
        endpoint=inference_endpoint,
        credential=azure_credential,
        credential_scopes=["https://ai.azure.com/.default"],
    )

    endpoint = os.environ.get('AZURE_AI_SEARCH_ENDPOINT')
    search_index_manager = None
    embed_dimensions = None
    if os.getenv('AZURE_AI_EMBED_DIMENSIONS'):
        embed_dimensions = int(os.getenv('AZURE_AI_EMBED_DIMENSIONS'))
        
    if endpoint and os.getenv('AZURE_AI_SEARCH_INDEX_NAME') and os.getenv('AZURE_AI_EMBED_DEPLOYMENT_NAME'):
        search_key = os.getenv('AZURE_SEARCH_ADMIN_KEY')
        if search_key:
            logger.info("Using search admin key for SearchClient authentication")
            search_credential = AzureKeyCredential(search_key)
        else:
            logger.info("Using token credential for SearchClient authentication")
            search_credential = azure_credential
        logger.info(
            "Search config -> endpoint: %s, index: %s, semantic config: %s, include metadata: %s",
            endpoint,
            os.getenv('AZURE_AI_SEARCH_INDEX_NAME'),
            os.getenv('AZURE_AI_SEARCH_SEMANTIC_CONFIG_NAME'),
            os.getenv('AZURE_SEARCH_INCLUDE_METADATA_FIELDS'),
        )
        search_index_manager = SearchIndexManager(
            endpoint = endpoint,
            credential = search_credential,
            index_name = os.getenv('AZURE_AI_SEARCH_INDEX_NAME'),
            dimensions = embed_dimensions,
            model = os.getenv('AZURE_AI_EMBED_DEPLOYMENT_NAME'),
            embeddings_client=embed,
            chat_client=chat,
            chat_model=os.environ["AZURE_AI_CHAT_DEPLOYMENT_NAME"],
            semantic_config_name=os.getenv('AZURE_AI_SEARCH_SEMANTIC_CONFIG_NAME', 'semantic-docs')
        )
        # Create index and upload the documents only if index does not exist.
        logger.info(f"Creating index {os.getenv('AZURE_AI_SEARCH_INDEX_NAME')}.")
        await search_index_manager.ensure_index_created(
            vector_index_dimensions=embed_dimensions if embed_dimensions else 100)
    else:
        logger.info("The RAG search will not be used.")

    app.state.chat = chat
    app.state.search_index_manager = search_index_manager
    app.state.chat_model = os.environ["AZURE_AI_CHAT_DEPLOYMENT_NAME"]
    yield

    await project.close()
    await chat.close()
    if search_index_manager is not None:
        await search_index_manager.close()


def create_app():
    if not os.getenv("RUNNING_IN_PRODUCTION"):
        # Load envs in a deterministic order so .azure overrides the sample src/.env
        repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
        azd_env_path = os.path.join(repo_root, ".azure", "lmc-doc-chat", ".env")
        root_env_path = os.path.join(repo_root, ".env")

        if os.path.exists(azd_env_path):
            load_dotenv(dotenv_path=azd_env_path, override=True)
        if os.path.exists(root_env_path):
            load_dotenv(dotenv_path=root_env_path, override=False)
        # Finally load any cwd .env without overriding higher-priority values
        load_dotenv(override=False)

    global logger
    logger = get_logger(
        name="azureaiapp",
        log_level=logging.INFO,
        log_file_name = os.getenv("APP_LOG_FILE"),
        log_to_console=True
    )

    enable_trace_string = os.getenv("ENABLE_AZURE_MONITOR_TRACING", "")
    global enable_trace
    enable_trace = False
    if enable_trace_string == "":
        enable_trace = False
    else:
        enable_trace = str(enable_trace_string).lower() == "true"
    if enable_trace:
        logger.info("Tracing is enabled.")
        try:
            from azure.monitor.opentelemetry import configure_azure_monitor
        except ModuleNotFoundError:
            logger.error("Required libraries for tracing not installed.")
            logger.error("Please make sure azure-monitor-opentelemetry is installed.")
            exit()
    else:
        logger.info("Tracing is not enabled")

    app = fastapi.FastAPI(lifespan=lifespan)
    static_dir = Path(__file__).resolve().parent / "static"
    app.mount("/static", StaticFiles(directory=static_dir), name="static")

    from . import routes  # noqa

    app.include_router(routes.router)

    return app
