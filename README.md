apt update && apt upgrade -y

apt install python3 python3-venv git -y

npm install -g pm2

git clone https://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@github.com/yadubuilds/pyrogram-control-userbot 

cd pyrogram-control-userbot

python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt

pm2 start ecosystem.config.js

pm2 save

pm2 startup
