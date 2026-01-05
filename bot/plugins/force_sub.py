from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import FORCE_SUB_CHANNELS

@Client.on_message(filters.command("start"))
async def start(client, message):
    user_id = message.from_user.id

    for ch in FORCE_SUB_CHANNELS:
        try:
            member = await client.get_chat_member(ch, user_id)
            if member.status == "left":
                raise Exception
        except:
            buttons = [
                [InlineKeyboardButton(f"Join @{ch}", url=f"https://t.me/{ch}")]
                for ch in FORCE_SUB_CHANNELS
            ]
            buttons.append(
                [InlineKeyboardButton("✅ Joined", callback_data="checksub")]
            )
            return await message.reply(
                "🔔 Please join required channels",
                reply_markup=InlineKeyboardMarkup(buttons)
            )

    await message.reply("✅ Access granted")
