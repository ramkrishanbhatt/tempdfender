import os
from fastapi import UploadFile
from uuid import uuid4
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

VIDEO_STORAGE_PATH = os.getenv("VIDEO_STORAGE_PATH", "/app/app/storage/videos/")

async def save_video(file: UploadFile) -> str:
    extension = file.filename.split(".")[-1]
    file_id = f"{uuid4()}.{extension}"
    file_path = os.path.join(VIDEO_STORAGE_PATH, file_id)

    with open(file_path, "wb") as f:
        f.write(await file.read())

    return file_id

def get_video_url(file_id: str) -> str:
    return f"/videos/{file_id}"
