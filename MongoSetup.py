import pymongo
client = pymongo.MongoClient("mongodb+srv://datascienceMongoDB:x0do8lh2Nz7xKiWU@datasciencemongodb.4b9oehe.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d={"candidate":"Prashant",
   "contact":"8868823635",
   "Email":"prashant886882@gmail.com"}

db1=client["MongoCollections"]
coll=db1["CollectionCandidate"]
coll.insert_one(d)