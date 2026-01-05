from mongo import admins
from config import OWNER_ID

def is_admin(user_id: int) -> bool:
    return user_id == OWNER_ID or admins.find_one({"user_id": user_id}) is not None
