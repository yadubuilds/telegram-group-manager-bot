import subprocess
from pyrogram import filters
from core.config import Config


def register_update(app):

    @app.on_message(filters.command("update") & filters.user(Config.OWNER_ID))
    async def update_handler(_, message):
        status = await message.reply("🔄 Updating system...")

        try:
            git_pull = subprocess.run(
                ["git", "pull"],
                capture_output=True,
                text=True
            )

            pm2_restart = subprocess.run(
                ["pm2", "restart", "all"],
                capture_output=True,
                text=True
            )

            reply_text = (
                "✅ **Update Successful**\n\n"
                "📥 **Git Pull Output:**\n"
                f"```{git_pull.stdout.strip() or 'No changes'}```\n\n"
                "♻️ **PM2 Restart Output:**\n"
                f"```{pm2_restart.stdout.strip()}```"
            )

            await status.edit(reply_text[:3800])

        except Exception as e:
            await status.edit(
                "❌ **Update Failed**\n\n"
                f"```{str(e)}```"
            )
