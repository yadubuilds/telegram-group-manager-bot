from pyrogram import Client, filters

@Client.on_message(filters.command("ping") & filters.me)
async def ping(_, msg):
    await msg.reply("🏓 Pong")
