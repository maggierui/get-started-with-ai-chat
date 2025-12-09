# LLM Model Configuration and Usage

## Overview

This document explains how the chat application selects and uses LLM models for both retrieval (embeddings) and generation (chat completions). The system uses Azure OpenAI Service models accessed through Azure AI Foundry project endpoints.

---

## Model Selection Flow

### 1. Infrastructure Provisioning (Bicep)

**File**: `infra/main.bicep`

The models are defined and deployed through Bicep parameters at infrastructure provisioning time:

#### Chat Completion Model Parameters

```bicep
// Default values in main.bicep
@description('Format of the chat model to deploy')
@allowed(['Microsoft', 'OpenAI'])
param chatModelFormat string = 'OpenAI'

@description('Name of the chat model to deploy')
param chatModelName string = 'gpt-4o-mini'

@description('Name of the model deployment')
param chatDeploymentName string = 'gpt-4o-mini'

@description('Version of the chat model to deploy')
param chatModelVersion string = '2024-07-18'

@description('Sku of the chat deployment')
param chatDeploymentSku string = 'GlobalStandard'

@description('Capacity of the chat deployment')
param chatDeploymentCapacity int = 30
```

**Model Configuration**:
- **Model**: `gpt-4o-mini`
- **Version**: `2024-07-18`
- **SKU**: `GlobalStandard` (supports global deployment)
- **Capacity**: 30 TPM (Tokens Per Minute) by default

#### Embedding Model Parameters

```bicep
@description('Format of the embedding model to deploy')
@allowed(['Microsoft', 'OpenAI'])
param embedModelFormat string = 'OpenAI'

@description('Name of the embedding model to deploy')
param embedModelName string = 'text-embedding-3-small'

@description('Name of the embedding model deployment')
param embeddingDeploymentName string = 'text-embedding-3-small'

@description('Embedding model dimensionality')
param embeddingDeploymentDimensions string = '100'

@description('Version of the embedding model to deploy')
param embedModelVersion string = '1'

@description('Sku of the embeddings model deployment')
param embedDeploymentSku string = 'Standard'

@description('Capacity of the embedding deployment')
param embedDeploymentCapacity int = 30
```

**Default Embedding Configuration**:
- **Model**: `text-embedding-3-small`
- **Dimensions**: `100`
- **Version**: `1`
- **SKU**: `Standard`
- **Capacity**: 30 TPM

**Note**: The current deployment uses **`text-embedding-3-large`** with **3072 dimensions** instead of the defaults (overridden during deployment).

#### Model Deployment Array

The models are deployed to Azure OpenAI through the AI Project:

```bicep
var aiChatModel = [
  {
    name: chatDeploymentName
    model: {
      format: chatModelFormat
      name: chatModelName
      version: chatModelVersion
    }
    sku: {
      name: chatDeploymentSku
      capacity: chatDeploymentCapacity
    }
  }
]

var aiEmbeddingModel = [ 
  {
    name: embeddingDeploymentName
    model: {
      format: embedModelFormat
      name: embedModelName
      version: embedModelVersion
    }
    sku: {
      name: embedDeploymentSku
      capacity: embedDeploymentCapacity
    }
  }
]

// Conditional deployment based on RAG usage
var aiDeployments = concat(
  aiChatModel,
  useSearchService ? aiEmbeddingModel : []  // Only deploy embedding if RAG enabled
)
```

**Key Insight**: The embedding model is only deployed if `useSearchService = true`. Without RAG, only the chat model is deployed.

#### Bicep Outputs

The deployment names are exported as outputs to be injected into the application:

```bicep
output AZURE_AI_CHAT_DEPLOYMENT_NAME string = chatDeploymentName
output AZURE_AI_EMBED_DEPLOYMENT_NAME string = embeddingDeploymentName
output AZURE_AI_EMBED_DIMENSIONS string = embeddingDeploymentDimensions
output AZURE_EXISTING_AIPROJECT_ENDPOINT string = projectEndpoint
```

These outputs are automatically written to `.azure/<env-name>/.env` by `azd`.

---

### 2. Application Startup (main.py)

**File**: `src/api/main.py`

The application initializes model clients during startup in the `lifespan` async context manager:

#### Step 1: Load Configuration from Environment

```python
# From .azure/<env-name>/.env (set by azd from Bicep outputs)
endpoint = os.environ["AZURE_EXISTING_AIPROJECT_ENDPOINT"]  # AI Project endpoint
chat_model = os.environ["AZURE_AI_CHAT_DEPLOYMENT_NAME"]     # "gpt-4o-mini"
embed_model = os.getenv('AZURE_AI_EMBED_DEPLOYMENT_NAME')    # "text-embedding-3-large"
embed_dimensions = int(os.getenv('AZURE_AI_EMBED_DIMENSIONS')) if os.getenv('AZURE_AI_EMBED_DIMENSIONS') else None  # 3072
```

#### Step 2: Authentication Setup

```python
# Local development: Use Azure Developer CLI credential
if not os.getenv("RUNNING_IN_PRODUCTION"):
    if tenant_id := os.getenv("AZURE_TENANT_ID"):
        azure_credential = AzureDeveloperCliCredential(tenant_id=tenant_id)
    else:
        azure_credential = AzureDeveloperCliCredential()

# Production: Use Container App's managed identity
else:
    user_identity_client_id = os.getenv("AZURE_CLIENT_ID")
    azure_credential = ManagedIdentityCredential(client_id=user_identity_client_id)
```

#### Step 3: Initialize AI Project Client

```python
from azure.ai.projects.aio import AIProjectClient

project = AIProjectClient(
    credential=azure_credential,
    endpoint=endpoint,  # e.g., "https://aoai-xyz.services.ai.azure.com/api/projects/proj-xyz"
)
```

The AI Project client is used for:
- Retrieving Application Insights connection string (if tracing enabled)
- Managing project-level resources
- Not directly used for model inference

#### Step 4: Create Inference Endpoint

The AI Project endpoint needs to be transformed to an inference endpoint:

```python
from urllib.parse import urlparse

# Project endpoint:   https://aoai-xyz.services.ai.azure.com/api/projects/proj-xyz
# Inference endpoint: https://aoai-xyz.services.ai.azure.com/models

inference_endpoint = f"https://{urlparse(endpoint).netloc}/models"
```

**Why?** The AI Foundry inference API is at `/models` path, not project-specific.

#### Step 5: Initialize Chat Client

```python
from azure.ai.inference.aio import ChatCompletionsClient

chat = ChatCompletionsClient(
    endpoint=inference_endpoint,  # "https://aoai-xyz.services.ai.azure.com/models"
    credential=azure_credential,
    credential_scopes=["https://ai.azure.com/.default"],
)
```

**Important**: 
- **Endpoint**: Points to `/models` (not project-specific)
- **Credential Scopes**: `https://ai.azure.com/.default` (not standard Azure OpenAI scope)
- **Model Selection**: Done at request time via `model=` parameter, not client initialization

#### Step 6: Initialize Embeddings Client

```python
from azure.ai.inference.aio import EmbeddingsClient

embed = EmbeddingsClient(
    endpoint=inference_endpoint,  # Same endpoint as chat
    credential=azure_credential,
    credential_scopes=["https://ai.azure.com/.default"],
)
```

**Same pattern** as ChatCompletionsClient - model specified at request time.

#### Step 7: Initialize Search Index Manager (RAG)

```python
from .search_index_manager import SearchIndexManager

search_index_manager = None

# Only initialize if RAG is enabled
if (endpoint and 
    os.getenv('AZURE_AI_SEARCH_INDEX_NAME') and 
    os.getenv('AZURE_AI_EMBED_DEPLOYMENT_NAME')):
    
    search_index_manager = SearchIndexManager(
        endpoint=os.environ.get('AZURE_AI_SEARCH_ENDPOINT'),  # Search service
        credential=azure_credential,
        index_name=os.getenv('AZURE_AI_SEARCH_INDEX_NAME'),
        dimensions=embed_dimensions,  # 3072
        model=os.getenv('AZURE_AI_EMBED_DEPLOYMENT_NAME'),  # "text-embedding-3-large"
        embeddings_client=embed
    )
```

**Key Parameters**:
- **endpoint**: Azure AI Search service endpoint
- **model**: Deployment name for embeddings (used in API calls)
- **dimensions**: Must match embedding model output (3072 for text-embedding-3-large)
- **embeddings_client**: The initialized EmbeddingsClient

#### Step 8: Store in Application State

```python
app.state.chat = chat
app.state.search_index_manager = search_index_manager
app.state.chat_model = os.environ["AZURE_AI_CHAT_DEPLOYMENT_NAME"]  # Store model name
```

**Why store model name separately?** The client doesn't know which model to use until request time.

---

### 3. Request Processing (routes.py)

**File**: `src/api/routes.py`

#### Dependency Injection

FastAPI dependencies extract the stored clients and model name:

```python
def get_chat_client(request: Request) -> ChatCompletionsClient:
    return request.app.state.chat

def get_chat_model(request: Request) -> str:
    return request.app.state.chat_model  # Returns "gpt-4o-mini"

def get_search_index_namager(request: Request) -> SearchIndexManager:
    return request.app.state.search_index_manager
```

#### Chat Endpoint

```python
@router.post("/chat")
async def chat_stream_handler(
    chat_request: ChatRequest,
    chat_client: ChatCompletionsClient = Depends(get_chat_client),
    model_deployment_name: str = Depends(get_chat_model),  # "gpt-4o-mini"
    search_index_manager: SearchIndexManager = Depends(get_search_index_namager),
    _ = auth_dependency
) -> StreamingResponse:
```

**Dependencies injected**:
1. `chat_client`: ChatCompletionsClient instance
2. `model_deployment_name`: String with deployment name ("gpt-4o-mini")
3. `search_index_manager`: SearchIndexManager (or None if RAG disabled)

---

### 4. RAG Retrieval (search_index_manager.py)

**File**: `src/api/search_index_manager.py`

When RAG is enabled, the query embedding happens first:

```python
async def search(self, message: ChatRequest) -> tuple[str, list[dict]]:
    """
    Search the message in the vector store.
    """
    # Extract user question from message history
    user_question = message.messages[-1].content
    
    # Step 1: Generate embedding for user query using embedding model
    embedded_question = (await self._embeddings_client.embed(
        input=user_question,
        dimensions=self._dimensions,  # 3072
        model=self._model  # "text-embedding-3-large"
    ))['data'][0]['embedding']
    
    # Step 2: Perform vector search in Azure AI Search
    vector_query = VectorizedQuery(
        vector=embedded_question,
        k_nearest_neighbors=5,
        fields="text_vector"
    )
    
    response = await self._get_client().search(
        vector_queries=[vector_query],
        select=['chunk', 'title', 'chunk_id'],
    )
    
    # Step 3: Collect results
    sources = []
    context_chunks = []
    idx = 0
    async for result in response:
        context_chunks.append(result['chunk'])
        sources.append({
            'rank': idx + 1,
            'title': result.get('title', 'Unknown'),
            'chunk_id': result.get('chunk_id', ''),
            'content': result['chunk'][:200] + '...'
        })
        idx += 1
    
    # Return concatenated context + source metadata
    return "\n------\n".join(context_chunks), sources
```

**Key Points**:
- **Embedding Model Used**: `text-embedding-3-large` (from `self._model`)
- **Dimensions**: 3072 (from `self._dimensions`)
- **API Call**: `embeddings_client.embed(input=..., dimensions=..., model=...)`
- **Output**: 3072-dimensional vector for semantic search

---

### 5. Chat Completion Generation (routes.py)

**File**: `src/api/routes.py`

Back in the `/chat` endpoint handler:

```python
async def response_stream():
    # Convert request messages to dict format
    messages = [
        {"role": message.role, "content": message.content} 
        for message in chat_request.messages
    ]

    # Default system prompt (no RAG)
    prompt_messages = PromptTemplate.from_string(
        'You are a helpful assistant'
    ).create_messages()
    
    sources = []
    
    # If RAG enabled, retrieve context
    if search_index_manager is not None:
        context, sources = await search_index_manager.search(chat_request)
        
        if context:
            logger.info(f"Retrieved context chunks:\n{context}")
            
            # Send sources to frontend first (SSE event)
            yield serialize_sse_event({
                "type": "sources",
                "sources": sources
            })
            
            # Update system prompt with RAG context
            prompt_messages = PromptTemplate.from_string(
                'You are a helpful assistant that answers some questions '
                'with the help of some context data.\n\nHere is '
                'the context data:\n\n{{context}}'
            ).create_messages(data=dict(context=context))
    
    # Generate chat completion with selected model
    chat_coroutine = await chat_client.complete(
        model=model_deployment_name,  # "gpt-4o-mini" - THIS IS WHERE MODEL IS SELECTED
        messages=prompt_messages + messages,  # System prompt + user messages
        stream=True  # Enable streaming
    )
    
    # Stream response back to frontend
    async for event in chat_coroutine:
        if event.choices:
            first_choice = event.choices[0]
            if first_choice.delta.content:
                message = first_choice.delta.content
                yield serialize_sse_event({
                    "content": message,
                    "type": "message",
                })
```

**Critical Line**:
```python
chat_coroutine = await chat_client.complete(
    model=model_deployment_name,  # ← "gpt-4o-mini" specified here
    messages=prompt_messages + messages,
    stream=True
)
```

**This is where the chat model is actually selected and invoked.**

---

## Complete Model Usage Flow

### RAG-Enabled Request Flow

```
1. User sends message → POST /chat
   ↓
2. FastAPI dependency injection
   - chat_client: ChatCompletionsClient
   - model_deployment_name: "gpt-4o-mini"
   - search_index_manager: SearchIndexManager
   ↓
3. RAG Retrieval (SearchIndexManager.search)
   - Embed query using: embeddings_client.embed(
       model="text-embedding-3-large",
       dimensions=3072,
       input=user_question
     )
   - Vector search in Azure AI Search index
   - Return: (context, sources)
   ↓
4. Prompt Construction
   - Build system message with context
   - Combine with user message history
   ↓
5. Chat Completion (ChatCompletionsClient.complete)
   - API call with: model="gpt-4o-mini"
   - Messages: [system_prompt_with_context] + [user_messages]
   - Stream: True
   ↓
6. Stream Response
   - Send sources as SSE event (type: "sources")
   - Stream answer chunks (type: "message")
   - Send completion marker (type: "completed_message")
   ↓
7. Frontend displays chat + sources panel
```

### Non-RAG Request Flow

```
1. User sends message → POST /chat
   ↓
2. FastAPI dependency injection
   - chat_client: ChatCompletionsClient
   - model_deployment_name: "gpt-4o-mini"
   - search_index_manager: None
   ↓
3. Prompt Construction
   - Default system message: "You are a helpful assistant"
   - User message history
   ↓
4. Chat Completion (ChatCompletionsClient.complete)
   - API call with: model="gpt-4o-mini"
   - Messages: [default_system_prompt] + [user_messages]
   - Stream: True
   ↓
5. Stream Response
   - Stream answer chunks (type: "message")
   - Send completion marker (type: "completed_message")
   ↓
6. Frontend displays chat only
```

---

## Model Selection Configuration

### Current Production Configuration

From `.azure/lmc-doc-chat/.env`:

```bash
# Chat Model (Generation)
AZURE_AI_CHAT_DEPLOYMENT_NAME="gpt-4o-mini"

# Embedding Model (Retrieval)
AZURE_AI_EMBED_DEPLOYMENT_NAME="text-embedding-3-large"
AZURE_AI_EMBED_DIMENSIONS=3072
```

### How to Change Models

#### Option 1: Update Bicep Parameters (Infrastructure)

Edit `infra/main.bicep` defaults or pass parameters during `azd up`:

```bash
# Change chat model to GPT-4
azd up --parameter chatModelName=gpt-4o --parameter chatDeploymentName=gpt-4o

# Change embedding model to larger version
azd up --parameter embedModelName=text-embedding-3-large \
       --parameter embeddingDeploymentName=text-embedding-3-large \
       --parameter embeddingDeploymentDimensions=3072
```

**Important**: Changing embedding model requires:
1. Recreating the search index with new dimensions
2. Re-running the indexer to regenerate embeddings

#### Option 2: Manually Update Environment Variables

Edit `.azure/<env-name>/.env`:

```bash
# Change to GPT-4o
AZURE_AI_CHAT_DEPLOYMENT_NAME="gpt-4o"

# Change to different embedding model
AZURE_AI_EMBED_DEPLOYMENT_NAME="text-embedding-ada-002"
AZURE_AI_EMBED_DIMENSIONS=1536
```

Then redeploy:
```bash
azd deploy
```

**Caution**: The deployment must exist in your Azure OpenAI resource. You cannot reference a deployment that doesn't exist.

#### Option 3: Deploy New Model via Azure Portal/CLI

1. Deploy new model in Azure AI Foundry or Azure OpenAI:
   ```bash
   az cognitiveservices account deployment create \
     --resource-group rg-lmc-doc-chat \
     --name aoai-zpz5xvg2elsve \
     --deployment-name gpt-4o \
     --model-name gpt-4o \
     --model-version "2024-08-06" \
     --model-format OpenAI \
     --sku-name "GlobalStandard" \
     --sku-capacity 10
   ```

2. Update `.env` with new deployment name

3. Redeploy application

---

## API Client Details

### ChatCompletionsClient API

**Initialization**:
```python
ChatCompletionsClient(
    endpoint="https://<resource>.services.ai.azure.com/models",
    credential=azure_credential,
    credential_scopes=["https://ai.azure.com/.default"]
)
```

**Usage**:
```python
response = await chat_client.complete(
    model="gpt-4o-mini",  # Deployment name (required)
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "What is SharePoint?"}
    ],
    stream=True,  # Enable streaming
    temperature=0.7,  # Optional parameters
    max_tokens=1000
)
```

**Response Format (Streaming)**:
```python
async for event in response:
    if event.choices:
        delta = event.choices[0].delta
        if delta.content:
            print(delta.content, end='')
```

### EmbeddingsClient API

**Initialization**:
```python
EmbeddingsClient(
    endpoint="https://<resource>.services.ai.azure.com/models",
    credential=azure_credential,
    credential_scopes=["https://ai.azure.com/.default"]
)
```

**Usage**:
```python
response = await embeddings_client.embed(
    model="text-embedding-3-large",  # Deployment name (required)
    input="What is SharePoint?",  # Or list of strings
    dimensions=3072  # Optional, model-dependent
)

embedding_vector = response['data'][0]['embedding']  # List of floats
```

**Response Format**:
```python
{
    'data': [
        {
            'embedding': [0.123, -0.456, ...],  # 3072 floats for text-embedding-3-large
            'index': 0
        }
    ],
    'model': 'text-embedding-3-large',
    'usage': {'prompt_tokens': 5, 'total_tokens': 5}
}
```

---

## Model Compatibility Matrix

### Chat Completion Models

| Model | Deployment Name | Use Case | Context Window | Output Tokens |
|-------|----------------|----------|----------------|---------------|
| gpt-4o-mini | gpt-4o-mini | Cost-effective chat | 128K | 16K |
| gpt-4o | gpt-4o | Advanced reasoning | 128K | 16K |
| gpt-4 | gpt-4 | Complex tasks | 8K/32K | 4K/8K |
| gpt-35-turbo | gpt-35-turbo | Legacy support | 16K | 4K |

**Current**: `gpt-4o-mini` (good balance of performance and cost)

### Embedding Models

| Model | Deployment Name | Dimensions | Max Tokens | Use Case |
|-------|----------------|------------|------------|----------|
| text-embedding-3-small | text-embedding-3-small | 512/1536 | 8191 | Cost-effective RAG |
| text-embedding-3-large | text-embedding-3-large | 256/1024/3072 | 8191 | High-quality RAG |
| text-embedding-ada-002 | text-embedding-ada-002 | 1536 | 8191 | Legacy support |

**Current**: `text-embedding-3-large` with 3072 dimensions (highest quality)

**Important**: 
- text-embedding-3-small/large support custom dimensions
- Lower dimensions = faster search, less storage, slightly lower quality
- text-embedding-ada-002 has fixed 1536 dimensions

---

## Performance Considerations

### Chat Model Capacity

Current: **30 TPM (Tokens Per Minute)**

- Suitable for: ~100-200 requests/minute (depending on message length)
- Monitor: Azure Monitor metrics for throttling (429 errors)
- Scale: Increase `chatDeploymentCapacity` in Bicep

### Embedding Model Capacity

Current: **50 TPM**

- Indexing: 183 markdown files took ~2-5 minutes
- Query: 1 embedding per query (minimal overhead)
- Monitor: Indexer errors if capacity exceeded during bulk indexing
- Scale: Increase `embedDeploymentCapacity` or use batch indexing

### Cost Optimization

**Chat Model**:
- gpt-4o-mini: ~$0.15/1M input tokens, ~$0.60/1M output tokens
- gpt-4o: ~$2.50/1M input tokens, ~$10/1M output tokens
- Use gpt-4o-mini for most queries, gpt-4o for complex reasoning

**Embedding Model**:
- text-embedding-3-small: ~$0.02/1M tokens
- text-embedding-3-large: ~$0.13/1M tokens
- text-embedding-ada-002: ~$0.10/1M tokens

**Current configuration** (gpt-4o-mini + text-embedding-3-large) is cost-optimized for chat while maintaining high RAG quality.

---

## Troubleshooting

### Model Not Found Error

```
Error: The model 'gpt-4o-mini' was not found
```

**Cause**: Deployment doesn't exist in Azure OpenAI resource

**Fix**:
1. Check deployed models:
   ```bash
   az cognitiveservices account deployment list \
     --resource-group rg-lmc-doc-chat \
     --name aoai-zpz5xvg2elsve
   ```
2. Deploy missing model or update `AZURE_AI_CHAT_DEPLOYMENT_NAME` to match existing deployment

### Dimension Mismatch Error

```
Error: Vector dimension mismatch: expected 1536, got 3072
```

**Cause**: Search index dimensions don't match embedding model output

**Fix**:
1. Delete and recreate index with correct dimensions
2. Or change embedding model to match index dimensions
3. Update `AZURE_AI_EMBED_DIMENSIONS` to match

### Authentication Error

```
Error: (Unauthorized) Access denied due to invalid subscription key or wrong API endpoint
```

**Cause**: Managed identity doesn't have Cognitive Services OpenAI User role

**Fix**:
```bash
az role assignment create \
  --assignee <managed-identity-principal-id> \
  --role "Cognitive Services OpenAI User" \
  --scope /subscriptions/<sub>/resourceGroups/<rg>/providers/Microsoft.CognitiveServices/accounts/<aoai-resource>
```

### Rate Limiting (429 Errors)

```
Error: Rate limit exceeded. Retry after X seconds.
```

**Cause**: TPM capacity exceeded

**Fix**:
1. Increase capacity in Bicep: `chatDeploymentCapacity = 50`
2. Implement exponential backoff in application
3. Use GlobalStandard SKU for better throughput

---

## Summary

### Key Takeaways

1. **Model Selection Happens at Request Time**: 
   - Clients are initialized once at startup
   - Model name passed to `chat_client.complete(model=...)` and `embeddings_client.embed(model=...)`

2. **Two Separate Models**:
   - **Chat Model** (`gpt-4o-mini`): Generates responses
   - **Embedding Model** (`text-embedding-3-large`): Converts text to vectors

3. **Configuration Hierarchy**:
   - Bicep parameters → Azure OpenAI deployments
   - Bicep outputs → `.env` file
   - Environment variables → Application runtime

4. **RAG Flow**:
   - Query → Embed (text-embedding-3-large) → Search → Context
   - Context + Query → Complete (gpt-4o-mini) → Response

5. **Authentication**:
   - Managed identity in production
   - Azure Developer CLI credential in development
   - Scopes: `https://ai.azure.com/.default` (AI Foundry)

6. **Endpoint Structure**:
   - Project: `https://<resource>.services.ai.azure.com/api/projects/<project>`
   - Inference: `https://<resource>.services.ai.azure.com/models` (used by clients)
