from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from core.config import Config
import os

def panel():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("▶️ Start Userbot", callback_data="start_ub"),
         InlineKeyboardButton("⏹ Stop Userbot", callback_data="stop_ub")],
        [InlineKeyboardButton("♻️ Restart Userbot", callback_data="restart_ub")]
    ])

def register_panel(app):
    @app.on_message(filters.command("panel") & filters.user(Config.OWNER_ID))
    async def show(_, msg):
        await msg.reply("🎛 Control Panel", reply_markup=panel())

    @app.on_callback_query(filters.user(Config.OWNER_ID))
    async def callbacks(_, cb):
        if cb.data == "start_ub":
            os.system("pm2 start userbot")
            await cb.message.edit("✅ Userbot started", reply_markup=panel())
        elif cb.data == "stop_ub":
            os.system("pm2 stop userbot")
            await cb.message.edit("⛔ Userbot stopped", reply_markup=panel())
        elif cb.data == "restart_ub":
            os.system("pm2 restart userbot")
            await cb.message.edit("♻️ Userbot restarted", reply_markup=panel())
        await cb.answer()
