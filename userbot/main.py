from pyrogram import Client
from core.config import Config

app = Client(
    "userbot",
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    session_string=Config.USER_SESSION,
    plugins=dict(root="userbot/plugins")
)

print("Userbot started")
app.run()
