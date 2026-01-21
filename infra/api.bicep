param name string
param location string = resourceGroup().location
param tags object = {}

param containerRegistryName string
param identityName string
param containerAppsEnvironmentName string
param azureExistingAIProjectResourceId string
param chatDeploymentName string
param embeddingDeploymentName string
param aiSearchIndexName string
param embeddingDeploymentDimensions string
param searchServiceEndpoint string
param enableAzureMonitorTracing bool
param azureTracingGenAIContentRecordingEnabled bool
param projectEndpoint string
param indexDescription string
param semanticConfigName string

resource apiIdentity 'Microsoft.ManagedIdentity/userAssignedIdentities@2023-01-31' = {
  name: identityName
  location: location
}

var env = [
  {
    name: 'AZURE_CLIENT_ID'
    value: apiIdentity.properties.clientId
  }
  {
    name: 'AZURE_EXISTING_AIPROJECT_RESOURCE_ID'
    value: azureExistingAIProjectResourceId
  }
  {
    name: 'AZURE_AI_CHAT_DEPLOYMENT_NAME'
    value: chatDeploymentName
  }
  {
    name: 'AZURE_AI_EMBED_DEPLOYMENT_NAME'
    value: embeddingDeploymentName
  }
  {
    name: 'AZURE_AI_SEARCH_INDEX_NAME'
    value: aiSearchIndexName
  }
  {
    name: 'AZURE_AI_EMBED_DIMENSIONS'
    value: embeddingDeploymentDimensions
  }
  {
    name: 'RUNNING_IN_PRODUCTION'
    value: 'true'
  }
  {
    name: 'AZURE_AI_SEARCH_ENDPOINT'
    value: searchServiceEndpoint
  }
  {
    name: 'ENABLE_AZURE_MONITOR_TRACING'
    value: enableAzureMonitorTracing
  }
  {
    name: 'AZURE_TRACING_GEN_AI_CONTENT_RECORDING_ENABLED'
    value: azureTracingGenAIContentRecordingEnabled
  }
  {
    name: 'AZURE_EXISTING_AIPROJECT_ENDPOINT'
    value: projectEndpoint
  }
  {
    name: 'INDEX_DESCRIPTION'
    value: indexDescription
  }
  {
    name: 'AZURE_AI_SEARCH_SEMANTIC_CONFIG_NAME'
    value: semanticConfigName
  }
]


module app 'core/host/container-app-upsert.bicep' = {
  name: 'container-app-module'
  params: {
    name: name
    location: location
    tags: union(tags, { 'azd-service-name': 'api_and_frontend' })
    identityName: apiIdentity.name
    containerRegistryName: containerRegistryName
    containerAppsEnvironmentName: containerAppsEnvironmentName
    targetPort: 50505
    env: env
  }
}


output SERVICE_API_IDENTITY_PRINCIPAL_ID string = apiIdentity.properties.principalId
output SERVICE_API_NAME string = app.outputs.name
output SERVICE_API_URI string = app.outputs.uri
