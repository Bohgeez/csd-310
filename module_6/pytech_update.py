'''update student id'''
from pymongo import MongoClient


conn = MongoClient()


db = conn.pytech


collection = db.students


cursor = collection.find()


for record in cursor:
    print(record)
    result = collection.update_one({"student_id": 1007},
    {"$set":{"last_name": "Smith"}})


cursor = collection.find()


for record in cursor:
    print(record)
