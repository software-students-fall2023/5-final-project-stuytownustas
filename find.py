import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mydb = myclient["taskdatabase"]
mycol = mydb["tasks"]

for x in mycol.find():
  print(x)


# x = mycol.delete_many({})
# print(x.deleted_count, " documents deleted.")