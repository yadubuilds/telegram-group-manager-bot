from pyrogram import Client
from config import *

app = Client(
    "manager_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="bot/plugins")
)

print("🤖 Manager Bot Started")
app.run()
