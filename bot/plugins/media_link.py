from pyrogram import Client, filters
from filters import is_admin

@Client.on_message(filters.command("link"))
async def media_link(client, m):
    if not is_admin(m.from_user.id):
        return

    if not m.reply_to_message or not m.reply_to_message.media:
        return await m.reply("Reply to a media file")

    file_id = m.reply_to_message.media.file_id
    link = f"https://t.me/{client.me.username}?start=file_{file_id}"

    await m.reply(f"🔗 **Media Link:**\n{link}")
