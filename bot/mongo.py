from pymongo import MongoClient
from datetime import datetime
from config import MONGO_URI, DB_NAME

client = MongoClient(MONGO_URI)
db = client[DB_NAME]

users = db.users
admins = db.admins
groups = db.groups
requests = db.requests
logs = db.logs


def log(action, data):
    logs.insert_one({
        "action": action,
        "data": data,
        "time": datetime.utcnow()
    })
