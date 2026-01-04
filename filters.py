from mongo import admins
from config import OWNER_ID

def is_admin(uid):
    return uid == OWNER_ID or admins.find_one({"user_id": uid})
