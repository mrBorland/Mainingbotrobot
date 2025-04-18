import os
import time
from telegram_report import send_report

print("[START] AutoFarmBot — запуск усіх напрямків")

modules = [
    "modules/crypto/galxe_farm.py",
    "modules/crypto/zealy_farm.py",
    "modules/clickfarm/smart_click_farm_v2.py",
    "modules/youtube/youtube_smart_bot_v3.py",
    "modules/nft/nft_monitor.py"
]

for module in modules:
    print(f"[RUN] {module}")
    os.system(f"python {module}")

# Надсилання звіту в Telegram
try:
    with open("youtube_view_log.txt", "r") as f:
        log_content = f.read()
except:
    log_content = "Лог перегляду YouTube відсутній або порожній."

send_report(f"Звіт AutoFarmBot:

{log_content}")

print("[WAIT] Чекаємо 6 годин до наступного запуску...")
time.sleep(21600)
