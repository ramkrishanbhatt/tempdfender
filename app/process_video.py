import httpx
from typing import List, Dict, Any
from collections import defaultdict

# Hive API details
HIVE_API_URL = "https://api.thehive.ai/api/v2/task/sync"
HIVE_API_TOKEN = "rvi3tYbKFoj7Ww5aTnPTNpCE29wXQQVJ"

async def process_video(file):
    # Prepare file data
    file_data = {
        "filename": file.filename,
        "file_path": file.file_path,
        "content_type": file.content_type,
    }

    try:
        # Upload video to HIVE API
        async with httpx.AsyncClient() as client:
            files = {'media': (file.filename, file.file, file.content_type)}
            headers = {'authorization': f'token {HIVE_API_TOKEN}'}
            response = await client.post(HIVE_API_URL, headers=headers, files=files)
        
        # Check for successful response
        response.raise_for_status()

        # Parse the response
        hive_response = response.json()

    except httpx.RequestError as e:
        print(f"An error occurred while requesting: {e}")
        return {"error": "Request failed"}
    except httpx.HTTPStatusError as e:
        print(f"HTTP error occurred: {e}")
        return {"error": "HTTP error"}
    except ValueError as e:
        print(f"Error parsing JSON response: {e}")
        return {"error": "Invalid JSON response"}

    result = {
        "fileData": file_data,
        "hiveResponse": hive_response,
        "decision": {"status":"Hold", "classes":[]},
    }

    return result