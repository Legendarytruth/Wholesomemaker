from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

database_url = os.getenv("MONGODB_URL")

client = MongoClient(database_url)
db = client.discord
try:
    db.command("serverStatus")
except Exception as e:
    print(e)
else:
    print("You are connected!")
client.close()
