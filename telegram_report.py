import requests
import json

TELEGRAM_TOKEN = "7679171745:AAG2ElvAtIWTOG7WQuj7jQWTfQBXx0EUwKI"
CHAT_ID = "6821675571"

with open("modules/youtube/youtube_view_log.txt", "r") as f:
    log_data = f.read()

summary = f"[YouTube Bot Звіт]\n{log_data[-2000:]}"  # останні 2000 символів

url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
data = {
    "chat_id": CHAT_ID,
    "text": summary
}

response = requests.post(url, data=data)
print("[Telegram] Статус надсилання:", response.status_code)