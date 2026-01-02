import asyncio
import os
from azure.identity.aio import AzureDeveloperCliCredential
from azure.core.credentials import AzureKeyCredential
from azure.search.documents.indexes.aio import SearchIndexClient
from azure.search.documents.indexes.models import (
    ScoringProfile,
    TagScoringFunction,
    TagScoringParameters,
    ScoringFunctionAggregation
)
from dotenv import load_dotenv

load_dotenv(dotenv_path="/workspaces/get-started-with-ai-chat/.azure/lmc-doc-chat/.env")

async def main():
    endpoint = os.getenv("AZURE_AI_SEARCH_ENDPOINT")
    index_name = os.getenv("AZURE_AI_SEARCH_INDEX_NAME")
    search_key = os.getenv("AZURE_SEARCH_ADMIN_KEY")
    
    if search_key:
        credential = AzureKeyCredential(search_key)
    else:
        credential = AzureDeveloperCliCredential()
        
    client = SearchIndexClient(endpoint=endpoint, credential=credential)
    
    print(f"Updating index {index_name}...")
    try:
        index = await client.get_index(index_name)
        
        # Define the scoring profile
        scoring_profile = ScoringProfile(
            name="metadata-boost",
            functions=[
                TagScoringFunction(
                    field_name="ms_topic",
                    boost=3.0,
                    parameters=TagScoringParameters(tags_parameter="topicTags")
                ),
                TagScoringFunction(
                    field_name="audience",
                    boost=2.0,
                    parameters=TagScoringParameters(tags_parameter="audienceTags")
                )
            ],
            function_aggregation=ScoringFunctionAggregation.SUM
        )
        
        index.scoring_profiles = [scoring_profile]
        
        await client.create_or_update_index(index)
        print("Index updated successfully with scoring profile.")
        
    except Exception as e:
        print(f"Error updating index: {e}")
    finally:
        await client.close()
        if hasattr(credential, 'close'):
            await credential.close()

if __name__ == "__main__":
    asyncio.run(main())
