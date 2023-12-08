import os
import pymongo
MONGO_URI= "mongodb://mongodb:27017"
client = pymongo.MongoClient(os.getenv("MONGODB_URI"))
task_database = client[os.getenv("MONGODB_DATABASE")]
tasks = task_database[os.getenv("MONGODB_COLLECTION")]

def insert_task(title, description, priority, status, deadline):
  tasks.insert_one({"title": title, "description": description, "priority": priority, "status": status, "deadline": deadline})

insert_task("Do laundry", "do the laundry", "low", "in progress", "Dec 15")

for x in tasks.find():
  print(x)