import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["taskdatabase"]
mycol = mydb["tasks"]

def insert_task(title, description, priority, status, deadline):
  mycol.insert_one({"title": title, "description": description, "priority": priority, "status": status, "deadline": deadline})

insert_task("Do laundry", "do the laundry", "low", "in progress", "Dec 15")
