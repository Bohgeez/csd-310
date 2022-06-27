'''update student id'''
from pymongo import MongoClient


conn = MongoClient()


db = conn.pytech


collection = db.students

#Call the find() method and display the results to the terminal window.
cursor = collection.find()
for record in cursor:
    print(record)

#Call the insert_one() method and Insert a new document into the pytech collection with student_id 1010
cursor = collection.find_one()
for record in cursor:
    print(record)
    result = collection.insert_one({"student_id": 1010},
    {"$set":{"last_name": "Smith"}})

#Call the find_one() method and display the results to the terminal window.
cursor = collection.find_one()
for record in cursor:
    print(record)
#Call the delete_one() method by student_id 1010.
cursor = collection.find_one()
for record in cursor:
    print(record)
    result = collection.delete_one({"student_id": 1010})
#Call the find() method and display the results to the terminal window.
cursor = collection.find()

for record in cursor:
    print(record)