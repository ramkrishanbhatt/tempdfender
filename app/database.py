import motor.motor_asyncio
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

MONGO_URL = os.getenv("MONGO_URL")

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URL)
db = client.fastapi_db
collection = db["HiveVideo"]