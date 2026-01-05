from pyrogram import Client, filters
from mongo import logs
from filters import is_admin

@Client.on_message(filters.command("logs"))
async def show_logs(_, m):
    if not is_admin(m.from_user.id):
        return

    text = "🧾 **Recent Logs**\n\n"
    for l in logs.find().sort("time", -1).limit(10):
        text += f"• {l['action']} → {l['data']}\n"

    await m.reply(text)
