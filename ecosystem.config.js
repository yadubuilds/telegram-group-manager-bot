module.exports = {
  apps: [
    {
      name: "control-bot",
      script: "bot/main.py",
      interpreter: "python3",
      cwd: "/root/pyrogram-control-userbot",
      env: {
        PYTHONPATH: "."
      }
    },
    {
      name: "userbot",
      script: "userbot/main.py",
      interpreter: "python3",
      cwd: "/root/pyrogram-control-userbot",
      env: {
        PYTHONPATH: "."
      }
    }
  ]
}
