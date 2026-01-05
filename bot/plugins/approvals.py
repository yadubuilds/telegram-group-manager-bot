from pyrogram import Client
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from mongo import requests, log
from filters import is_admin

@Client.on_chat_join_request()
async def on_request(client, req):
    requests.insert_one({
        "user_id": req.from_user.id,
        "chat_id": req.chat.id
    })

    await client.send_message(
        req.from_user.id,
        "📨 Your join request has been received."
    )


@Client.on_callback_query(filters.regex("^approve_"))
async def approve(client, cb):
    if not is_admin(cb.from_user.id):
        return

    _, uid, gid = cb.data.split("_")

    await client.approve_chat_join_request(int(gid), int(uid))
    requests.delete_one({"user_id": int(uid), "chat_id": int(gid)})

    await client.send_message(int(uid), "✅ Your join request was approved")
    log("approve", {"user": uid, "group": gid})

    await cb.answer("Approved")
