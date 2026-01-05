from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from filters import is_admin

@Client.on_message(filters.command("panel"))
async def panel(_, m):
    if not is_admin(m.from_user.id):
        return

    kb = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("🗂 Join Requests", callback_data="pending"),
                InlineKeyboardButton("📢 Broadcast", callback_data="broadcast")
            ],
            [
                InlineKeyboardButton("🧾 Logs", callback_data="logs")
            ]
        ]
    )

    await m.reply("📊 **Admin Dashboard**", reply_markup=kb)
