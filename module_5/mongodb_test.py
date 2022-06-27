"""gets pytech cluster"""
from pymongo import MongoClient

URL = "mongodb+srv://admin:admin@cluster0.p8dde.mongodb.net/?retryWrites=true&w=majority";

client = MongoClient(URL)

db = client.pytech

print(db.list_collection_names)
