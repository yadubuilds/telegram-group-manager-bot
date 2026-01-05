import asyncio
from pyrogram import Client, filters
from mongo import users, log
from filters import is_admin

@Client.on_message(filters.command("broadcast"))
async def broadcast(_, m):
    if not is_admin(m.from_user.id):
        return

    if not m.reply_to_message:
        return await m.reply("Reply to a message to broadcast")

    sent = 0
    for u in users.find():
        try:
            await m.reply_to_message.copy(u["user_id"])
            sent += 1
            await asyncio.sleep(0.05)
        except:
            pass

    log("broadcast", {"by": m.from_user.id, "sent": sent})
    await m.reply(f"✅ Broadcast sent to {sent} users")
