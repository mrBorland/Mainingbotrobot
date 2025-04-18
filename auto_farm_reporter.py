import json
import os
from telegram_report import send_report

# Шлях до логів та акаунтів
crypto_file = "data/accounts_crypto.json"
youtube_file = "data/accounts_youtube.json"
log_file = "logs/farm_log.txt"

def count_accounts(filepath):
    if not os.path.exists(filepath):
        return 0
    with open(filepath, "r") as f:
        try:
            data = json.load(f)
            return len(data.get("accounts", []))
        except:
            return 0

def parse_profit(log_path):
    total = 0
    if not os.path.exists(log_path):
        return 0
    with open(log_path, "r") as f:
        for line in f:
            if "Зароблено" in line:
                parts = line.strip().split()
                for p in parts:
                    if "USDT" in p or "$" in p:
                        try:
                            num = float(p.replace("USDT", "").replace("$", "").replace(",", ""))
                            total += num
                        except:
                            continue
    return total

def main():
    crypto_count = count_accounts(crypto_file)
    youtube_count = count_accounts(youtube_file)
    profit = parse_profit(log_file)

    message = (
        f"[Звіт AutoFarmBot]\n"
        f"- Крипто акаунтів: {crypto_count}\n"
        f"- YouTube акаунтів: {youtube_count}\n"
        f"- Загальний прибуток: {profit:.2f} USDT"
    )

    print(message)
    send_report(message)

if __name__ == "__main__":
    main()
