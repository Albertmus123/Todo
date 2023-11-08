from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

uri = os.getenv("DATABASE_URL")

# Create a new client and connect to the server
client = MongoClient(uri)


db = client.todos
collection_name = db["todo_list"]
