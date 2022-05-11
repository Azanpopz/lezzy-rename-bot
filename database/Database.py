import pymongo 
import os

DATABASE_NAME = os.environ.get("DATABASE_NAME","")
DATABASE_URI = os.environ.get("DATABASE_URI","")
mongo = pymongo.MongoClient(DATABASE_URI)
db = mongo[DATABASE_NAME]
dbcol = db["user"]

def insert(chat_id):
            user_id = int(chat_id)
            user_det = {"_id":user_id,"file_id":None}
            try:
            	dbcol.insert_one(user_det)
            except:
            	pass

def addthumb(chat_id, file_id):
	dbcol.update_one({"_id":chat_id},{"$set":{"file_id":file_id}})
	
def delthumb(chat_id):
	dbcol.update_one({"_id":chat_id},{"$set":{"file_id":None}})
	
def find(chat_id):
	id =  {"_id":chat_id}
	x = dbcol.find(id)
	for i in x:
             lgcd = i["file_id"]
             return lgcd 

def getid():
    values = []
    for key  in dbcol.find():
         id = key["_id"]
         values.append((id)) 
    return values