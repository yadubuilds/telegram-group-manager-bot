from pymongo import MongoClient
from config import MONGO_URI, DB_NAME
from datetime import datetime

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
