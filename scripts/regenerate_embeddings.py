import asyncio
import csv
import json
import os
from urllib.parse import urlparse
from azure.identity import AzureDeveloperCliCredential, DefaultAzureCredential
from azure.ai.inference.aio import EmbeddingsClient
from dotenv import load_dotenv

async def main():
    # Load environment variables from the azure env file
    env_path = ".azure/lmc-doc-chat/.env"
    if os.path.exists(env_path):
        load_dotenv(env_path, override=True)
    else:
        load_dotenv("src/.env", override=True)
    
    endpoint = os.getenv("AZURE_EXISTING_AIPROJECT_ENDPOINT")
    if not endpoint:
        print("Error: AZURE_EXISTING_AIPROJECT_ENDPOINT not found in environment.")
        return

    # Construct inference endpoint
    inference_endpoint = f"https://{urlparse(endpoint).netloc}/models"
    
    print(f"Using inference endpoint: {inference_endpoint}")
    
    credential = DefaultAzureCredential()
    
    client = EmbeddingsClient(
        endpoint=inference_endpoint,
        credential=credential,
        credential_scopes=["https://ai.azure.com/.default"],
    )
    
    model = os.getenv("AZURE_AI_EMBED_DEPLOYMENT_NAME", "text-embedding-3-large")
    dimensions_str = os.getenv("AZURE_AI_EMBED_DIMENSIONS", "3072")
    dimensions = int(dimensions_str)
    
    input_file = "src/api/data/embeddings.csv"
    output_file = "src/api/data/embeddings_new.csv"
    
    print(f"Regenerating embeddings using model '{model}' with dimensions {dimensions}...")
    
    rows = []
    if not os.path.exists(input_file):
        print(f"Error: {input_file} not found.")
        return

    with open(input_file, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)
            
    print(f"Found {len(rows)} rows in {input_file}.")
    
    new_rows = []
    batch_size = 10
    
    try:
        for i in range(0, len(rows), batch_size):
            batch = rows[i:i+batch_size]
            inputs = [row["token"] for row in batch]
            
            # Call the embedding API
            response = await client.embed(input=inputs, model=model, dimensions=dimensions)
            
            for j, item in enumerate(response.data):
                row = batch[j]
                row["embedding"] = json.dumps(item.embedding)
                new_rows.append(row)
                
            print(f"Processed {len(new_rows)}/{len(rows)} rows...")
            
    except Exception as e:
        print(f"\nError during embedding generation: {e}")
        print("Please ensure you are logged in (azd auth login) and the model deployment exists.")
        await client.close()
        return

    await client.close()
    
    if len(new_rows) == len(rows):
        with open(output_file, "w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["token", "embedding"])
            writer.writeheader()
            writer.writerows(new_rows)
        
        print(f"\nSuccessfully generated {output_file}.")
        print(f"Replacing {input_file} with new embeddings...")
        os.replace(output_file, input_file)
        print("Done! Now you need to update the search index.")
        print("Since the index schema might need to change (dimensions), it's best to delete the old index or change the index name.")
    else:
        print("Failed to regenerate all embeddings.")

if __name__ == "__main__":
    asyncio.run(main())
