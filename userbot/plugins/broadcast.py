import asyncio
import csv
import os
import time
from datetime import datetime

from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from pyrogram.enums import ChatType

DEFAULT_DELAY = 0.8
LOG_DIR = "userbot/plugins/logs"

os.makedirs(LOG_DIR, exist_ok=True)


def parse_delay(cmd):
    try:
        return float(cmd[1])
    except Exception:
        return DEFAULT_DELAY


def save_log(rows, ts):
    path = f"{LOG_DIR}/broadcast_{ts}.csv"
    with open(path, "w", newline="") as f:
        csv.writer(f).writerows(rows)
    return path


@Client.on_message(filters.me & filters.reply & filters.command("broadcast", prefixes=[".", "/"]))
async def broadcast_all(client, message):
    reply = message.reply_to_message
    delay = parse_delay(message.command)

    start = time.time()
    ts = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    total = sent = failed = 0
    rows = [("chat_id", "status")]

    status = await message.reply(f"📢 Broadcast started\n⏱ Delay: `{delay}s`")

    async for dialog in client.get_dialogs():
        chat = dialog.chat

        # ✅ PYROGRAM v2 SAFE CHECK
        if chat.type not in (
            ChatType.PRIVATE,
            ChatType.GROUP,
            ChatType.SUPERGROUP,
        ):
            continue

        total += 1
        try:
            await reply.copy(chat.id)
            sent += 1
            rows.append((chat.id, "sent"))
            await asyncio.sleep(delay)

        except FloodWait as e:
            await asyncio.sleep(e.value)

        except Exception:
            failed += 1
            rows.append((chat.id, "failed"))

        if total % 25 == 0:
            await status.edit(
                f"📢 Broadcasting...\n\n"
                f"📨 Total: `{total}`\n"
                f"✅ Sent: `{sent}`\n"
                f"❌ Failed: `{failed}`"
            )

    log = save_log(rows, ts)
    duration = int(time.time() - start)
    success = round((sent / total) * 100, 2) if total else 0

    await status.edit(
        f"✅ **Broadcast Completed**\n\n"
        f"📨 Total: `{total}`\n"
        f"📤 Sent: `{sent}`\n"
        f"⚠️ Failed: `{failed}`\n"
        f"📈 Success: `{success}%`\n"
        f"⏱ Duration: `{duration}s`\n\n"
        f"🗂 Log:\n`{log}`"
    )
