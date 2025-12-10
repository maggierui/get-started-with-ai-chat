# RAG Setup Documentation

## Overview

This document describes how the RAG (Retrieval-Augmented Generation) system is configured for the SharePoint documentation chat application. The system uses Azure AI Search to index markdown documentation and retrieve relevant context for user queries.

---

## Environment Variables

The following environment variables must be configured in `.azure/<env-name>/.env`:

### Required RAG Configuration

```bash
# Azure AI Search
AZURE_AI_SEARCH_ENDPOINT="https://<search-service-name>.search.windows.net"
AZURE_AI_SEARCH_INDEX_NAME="<index-name>"  # e.g., "rag-1765302551581"

# Embedding Model Configuration
AZURE_AI_EMBED_DEPLOYMENT_NAME="text-embedding-3-large"
AZURE_AI_EMBED_DIMENSIONS=3072

# Chat Model
AZURE_AI_CHAT_DEPLOYMENT_NAME="gpt-4o-mini"

# Azure AI Project (for authentication)
AZURE_EXISTING_AIPROJECT_ENDPOINT="https://<aoai-resource>.services.ai.azure.com/api/projects/<project-name>"
AZURE_EXISTING_AIPROJECT_RESOURCE_ID="/subscriptions/<sub-id>/resourceGroups/<rg>/providers/Microsoft.CognitiveServices/accounts/<aoai-resource>/projects/<project-name>"

# Azure Infrastructure
AZURE_SUBSCRIPTION_ID="<subscription-id>"
AZURE_RESOURCE_GROUP="<resource-group-name>"
AZURE_LOCATION="eastus2"
AZURE_TENANT_ID="<tenant-id>"

# Application Service
SERVICE_API_IDENTITY_PRINCIPAL_ID="<container-app-managed-identity-id>"
```

### Optional Configuration

```bash
# Search Service Toggle
useSearchService="true"  # Set to "false" to disable RAG

# Basic Authentication (optional)
WEB_APP_USERNAME="<username>"
WEB_APP_PASSWORD="<password>"
```

---

## Azure AI Search Setup

### 1. Search Service

- **Service Name**: `lmc-doc-search`
- **SKU**: Standard tier
- **Location**: Same as resource group
- **Authentication**: Azure AD (Entra ID) with managed identity

### 2. Index Configuration

The index was created with the following schema to support markdown parsing with header-based chunking:

**Index Name**: `rag-1765302551581`

**Fields**:
| Field Name | Type | Configuration | Purpose |
|------------|------|---------------|---------|
| `chunk_id` | Edm.String | Key, Searchable, Analyzer: keyword | Unique identifier for each chunk |
| `parent_id` | Edm.String | Filterable | Reference to source blob file |
| `chunk` | Edm.String | Searchable, Retrievable | The text content of the chunk |
| `title` | Edm.String | Searchable, Retrievable | File name (from blob metadata) |
| `header_1` | Edm.String | Searchable, Filterable, Retrievable | H1 header content |
| `header_2` | Edm.String | Searchable, Filterable, Retrievable | H2 header content |
| `header_3` | Edm.String | Searchable, Filterable, Retrievable | H3 header content |
| `text_vector` | Collection(Edm.Single) | Searchable, Dimensions: 3072 | Embedding vector for semantic search |

**Vector Search Configuration**:
```json
{
  "vectorSearch": {
    "algorithms": [
      {
        "name": "default-algorithm",
        "kind": "hnsw"
      }
    ],
    "profiles": [
      {
        "name": "default-vector-profile",
        "algorithm": "default-algorithm"
      }
    ]
  }
}
```

**Creation Method**:
```bash
curl -X POST \
  "https://<search-service>.search.windows.net/indexes?api-version=2024-07-01" \
  -H "Content-Type: application/json" \
  -H "api-key: <admin-key>" \
  -d @index_schema.json
```

### 3. Data Source Configuration

**Data Source Name**: `rag-1765302551581-datasource`

**Configuration**:
- **Type**: Azure Blob Storage (`azureblob`)
- **Connection**: Managed Identity authentication to storage account
- **Container**: `docs`
- **Query Filter**: `OfficeDocs-SharePoint-pr` (folder prefix)

**Creation Method**:
```bash
curl -X POST \
  "https://<search-service>.search.windows.net/datasources?api-version=2024-07-01" \
  -H "Content-Type: application/json" \
  -H "api-key: <admin-key>" \
  -d '{
    "name": "rag-1765302551581-datasource",
    "type": "azureblob",
    "credentials": {
      "connectionString": null
    },
    "container": {
      "name": "docs",
      "query": "OfficeDocs-SharePoint-pr"
    },
    "dataChangeDetectionPolicy": null,
    "dataDeletionDetectionPolicy": null,
    "encryptionKey": null,
    "identity": {
      "@odata.type": "#Microsoft.Azure.Search.DataUserAssignedIdentity",
      "userAssignedIdentity": "/subscriptions/<sub-id>/resourcegroups/<rg>/providers/Microsoft.ManagedIdentity/userAssignedIdentities/<identity-name>"
    }
  }'
```

### 4. Indexer Configuration

**Indexer Name**: `rag-1765302551581-indexer`

**Configuration**:
- **Parsing Mode**: `markdown`
- **Markdown Header Depth**: `h3` (splits on H1, H2, H3)
- **Markdown Parsing Submode**: `oneToMany` (creates one document per section)
- **File Extension Filter**: `.md` (only processes markdown files)

**Field Mappings**:
- `metadata_storage_name` → `title`

**Parameters**:
```json
{
  "parameters": {
    "configuration": {
      "parsingMode": "markdown",
      "markdownHeaderDepth": "h3",
      "markdownParsingSubmode": "oneToMany",
      "indexedFileNameExtensions": ".md"
    }
  },
  "fieldMappings": [
    {
      "sourceFieldName": "metadata_storage_name",
      "targetFieldName": "title"
    }
  ]
}
```

**Creation Method**:
```bash
curl -X POST \
  "https://<search-service>.search.windows.net/indexers?api-version=2024-07-01" \
  -H "Content-Type: application/json" \
  -H "api-key: <admin-key>" \
  -d @indexer_config.json
```

**Run Indexer**:
```bash
curl -X POST \
  "https://<search-service>.search.windows.net/indexers/<indexer-name>/run?api-version=2024-07-01" \
  -H "Content-Length: 0" \
  -H "api-key: <admin-key>"
```

---

## Authentication & Permissions

### Authentication Method

**Azure AD (Entra ID) with Managed Identity**

The application uses the Container App's system-assigned managed identity to authenticate to:
1. Azure AI Search
2. Azure OpenAI (via AI Project)
3. Azure Blob Storage (for indexer data source)

### Required Role Assignments

#### 1. Search Service Permissions

**Container App Managed Identity** → **Search Service**:
- Role: `Search Index Data Reader`
- Scope: Search service resource
- Purpose: Read search index and perform queries

**Search Service Managed Identity** → **Storage Account**:
- Role: `Storage Blob Data Reader`
- Scope: Storage account or specific container
- Purpose: Read blob files for indexing

**Search Service Managed Identity** → **Azure OpenAI**:
- Role: `Cognitive Services OpenAI User`
- Scope: Azure OpenAI resource
- Purpose: Generate embeddings during indexing

#### 2. Application Permissions

**Container App Managed Identity** → **Azure OpenAI**:
- Role: `Cognitive Services OpenAI User`
- Scope: Azure OpenAI resource
- Purpose: Generate embeddings for queries and chat completions

### Assigning Permissions

```bash
# Get the managed identity principal ID
SEARCH_IDENTITY=$(az search service show \
  --name <search-service> \
  --resource-group <rg> \
  --query identity.principalId -o tsv)

APP_IDENTITY=$(az containerapp show \
  --name <container-app> \
  --resource-group <rg> \
  --query identity.principalId -o tsv)

# Assign Search Index Data Reader to app
az role assignment create \
  --assignee $APP_IDENTITY \
  --role "Search Index Data Reader" \
  --scope /subscriptions/<sub-id>/resourceGroups/<rg>/providers/Microsoft.Search/searchServices/<search-service>

# Assign Storage Blob Data Reader to search service
az role assignment create \
  --assignee $SEARCH_IDENTITY \
  --role "Storage Blob Data Reader" \
  --scope /subscriptions/<sub-id>/resourceGroups/<rg>/providers/Microsoft.Storage/storageAccounts/<storage-account>

# Assign Cognitive Services OpenAI User to search service and app
az role assignment create \
  --assignee $SEARCH_IDENTITY \
  --role "Cognitive Services OpenAI User" \
  --scope /subscriptions/<sub-id>/resourceGroups/<rg>/providers/Microsoft.CognitiveServices/accounts/<aoai-resource>

az role assignment create \
  --assignee $APP_IDENTITY \
  --role "Cognitive Services OpenAI User" \
  --scope /subscriptions/<sub-id>/resourceGroups/<rg>/providers/Microsoft.CognitiveServices/accounts/<aoai-resource>
```

---

## How the Chat Application Works

### Architecture Flow

```
User Query
    ↓
Frontend (React) → POST /chat
    ↓
Backend (FastAPI)
    ↓
1. SearchIndexManager.search()
   - Embed query using text-embedding-3-large
   - Vector search in Azure AI Search
   - Retrieve top 5 chunks + metadata
    ↓
2. Build RAG prompt with context
    ↓
3. ChatCompletionsClient.complete()
   - Stream response from gpt-4o-mini
    ↓
4. Stream back to frontend
   - Sources (chunks) sent first
   - Answer streamed as SSE events
    ↓
Frontend displays:
   - Chat message (left panel)
   - Retrieved sources (right panel)
```

### Backend Components

#### 1. SearchIndexManager (`src/api/search_index_manager.py`)

**Purpose**: Manages semantic search over the index

**Key Methods**:
- `search(message: ChatRequest) → tuple[str, list[dict]]`
  - Embeds user query using embedding model
  - Performs vector search with `VectorizedQuery`
  - Retrieves top 5 chunks with metadata
  - Returns: (concatenated context, list of source metadata)

**Vector Search Configuration**:
```python
vector_query = VectorizedQuery(
    vector=embedded_question,
    k_nearest_neighbors=5,
    fields="text_vector"
)

response = await search_client.search(
    vector_queries=[vector_query],
    select=['chunk', 'title', 'chunk_id']
)
```

#### 2. Chat Router (`src/api/routes.py`)

**Endpoint**: `POST /chat`

**Request Body**:
```json
{
  "messages": [
    {"role": "user", "content": "How do I configure SharePoint?"}
  ]
}
```

**Response Flow**:
1. **Sources Event** (if RAG enabled):
   ```json
   {
     "type": "sources",
     "sources": [
       {
         "rank": 1,
         "title": "configure-settings.md",
         "chunk_id": "base64-encoded-id",
         "content": "First 200 chars of chunk..."
       }
     ]
   }
   ```

2. **Message Chunks** (streaming):
   ```json
   {"type": "message", "content": "To configure SharePoint..."}
   ```

3. **Completed Message**:
   ```json
   {"type": "completed_message", "content": "Full response text"}
   ```

**RAG Prompt Construction**:
```python
if context:
    prompt_messages = PromptTemplate.from_string(
        'You are a helpful assistant that answers some questions '
        'with the help of some context data.\n\nHere is '
        'the context data:\n\n{{context}}'
    ).create_messages(data=dict(context=context))
```

### Frontend Components

#### SourcesPanel (`src/frontend/src/components/agents/SourcesPanel.tsx`)

**Purpose**: Display retrieved document chunks in right sidebar

**Features**:
- Shows ranked list of sources (1-5)
- Displays title, chunk_id, and content preview
- Updates when new sources arrive from backend

#### AgentPreview (`src/frontend/src/components/agents/AgentPreview.tsx`)

**Purpose**: Main chat interface

**State Management**:
```typescript
const [sources, setSources] = useState<Source[]>([]);

// When receiving SSE events:
if (data.type === 'sources') {
  setSources(data.sources);
}
```

---

## YAML Frontmatter Handling

**Behavior**: YAML frontmatter in markdown files **is indexed** as text content.

**Example**:
```markdown
---
ms.date: 04/17/2025
title: Introduction to SharePoint
ms.author: ruihu
---

# Introduction to SharePoint
```

The YAML section is treated as regular text, so you can search for:
- `ms.date`
- Author names
- Topics
- Other metadata fields

**Search Query Example**:
```
"ms.author ruihu" → Will find chunks containing this metadata
```

---

## Troubleshooting

### Common Issues

1. **"No matching index field" error**
   - Ensure index schema includes all fields required by indexer
   - For `oneToMany` parsing, must have: `header_1`, `header_2`, `header_3`

2. **Non-markdown files being indexed**
   - Add `indexedFileNameExtensions: ".md"` to indexer configuration

3. **Empty search results**
   - Check indexer status: `GET /indexers/<name>/status`
   - Verify document count: `GET /indexes/<name>/stats`
   - Check embedding model dimensions match (3072 for text-embedding-3-large)

4. **Authentication errors**
   - Verify managed identity has required role assignments
   - Check role assignments propagated (can take 5-10 minutes)
   - Use `az role assignment list` to verify

### Monitoring

**Check Indexer Status**:
```bash
curl -s "https://<search-service>.search.windows.net/indexers/<indexer-name>/status?api-version=2024-07-01" \
  -H "api-key: <admin-key>" | jq '{status, lastResult}'
```

**Check Index Document Count**:
```bash
curl -s "https://<search-service>.search.windows.net/indexes/<index-name>/stats?api-version=2024-07-01" \
  -H "api-key: <admin-key>" | jq '{documentCount, storageSize}'
```

**Test Search Query**:
```bash
curl -X POST "https://<search-service>.search.windows.net/indexes/<index-name>/docs/search?api-version=2024-07-01" \
  -H "Content-Type: application/json" \
  -H "api-key: <admin-key>" \
  -d '{
    "search": "*",
    "select": "title,chunk",
    "top": 3
  }'
```

---

## Application Code

### Markdown Image Handling

The application automatically filters markdown image references from retrieved chunks to prevent LLM API errors.

**Issue**: Markdown files contain relative image paths (e.g., `![diagram](media/folder/image.png)`). The Azure AI Inference SDK's `PromptTemplate` automatically detects these and attempts to convert them to `image_url` message content types. However, relative paths are not valid URLs, causing `BadRequest: Invalid image URL` errors.

**Solution**: The `SearchIndexManager._clean_markdown_images()` method strips image references before sending context to the LLM:

```python
@staticmethod
def _clean_markdown_images(text: str) -> str:
    """Remove markdown image references that would cause LLM API errors."""
    # Remove inline images: ![alt text](image_path) → [Image: alt text]
    text = re.sub(r'!\[([^\]]*)\]\([^\)]+\)', r'[Image: \1]', text)
    
    # Remove reference-style image definitions: [id]: path "title"
    text = re.sub(r'^\[([^\]]+)\]:\s+[^\s]+.*$', '', text, flags=re.MULTILINE)
    
    return text
```

This ensures:
- ✅ LLM receives clean text context without broken image URLs
- ✅ Alt text is preserved as `[Image: description]` for context
- ✅ No API errors during chat completion
- ✅ Retrieved chunks still contain original content in the sources panel

**Location**: `src/api/search_index_manager.py`

### Container App Environment Variables

If RAG is not working after deployment, verify the Container App has the correct environment variables:

```bash
# Check AZURE_AI_SEARCH_ENDPOINT is set
az containerapp show \
  --name <container-app-name> \
  --resource-group <resource-group> \
  --query 'properties.template.containers[0].env[] | [?name==`AZURE_AI_SEARCH_ENDPOINT`]'
```

If the value is empty (`""`), set it manually:

```bash
az containerapp update \
  --name <container-app-name> \
  --resource-group <resource-group> \
  --set-env-vars "AZURE_AI_SEARCH_ENDPOINT=https://<search-service>.search.windows.net"
```

The Container App will automatically restart with the new configuration.

**Common Issue**: The `.env` file in `.azure/<env-name>/.env` is only used locally during development. For production deployments, environment variables must be set in the Container App configuration (either via Bicep parameters or direct `az containerapp update`).

---

## Performance Considerations

### Embedding Model Capacity

- **Model**: `text-embedding-3-large`
- **Current Capacity**: 50 TPM (Tokens Per Minute)
- **Recommendation**: Increase if indexing >1000 files or expecting high query volume

### Index Statistics

- **Files**: ~2,190 markdown files
- **Documents**: ~14,040+ chunks (with header-based chunking)
- **Indexing Time**: ~120 minutes (hits indexer timeout, requires restart)

### Vector Search

- **Algorithm**: HNSW (Hierarchical Navigable Small World)
- **k_nearest_neighbors**: 5 (retrieving top 5 chunks)
- **Dimensions**: 3072 (matches embedding model)

---

## Next Steps

### Potential Improvements

1. **Incremental Indexing**:
   - Enable change detection policy to only index new/modified files
   - Configure deletion detection for removed files

2. **Advanced Chunking**:
   - Consider custom chunking strategy for very long sections
   - Add overlap between chunks for better context preservation

3. **Metadata Enrichment**:
   - Extract YAML frontmatter into separate fields
   - Add custom skill for structured metadata

4. **Query Optimization**:
   - Implement hybrid search (vector + keyword)
   - Add filters for specific document types or dates
   - Tune k_nearest_neighbors based on query type

5. **Monitoring**:
   - Enable Application Insights for search analytics
   - Track query performance and relevance metrics
   - Monitor embedding generation costs
