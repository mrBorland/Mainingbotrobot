
#!/usr/bin/env python3
import json
import subprocess
import time
from datetime import datetime

MAIN_WALLET = "0xf75137f855377b37d79fa8e470d2f6512361f2e6"
WALLETS_FILE = "wallets_bnb.json"
WITHDRAW_SCRIPT = "withdraw_all_bnb_nolib.py"

def run_farm():
    print("===== Старт фарму Galxe =====")
    result = subprocess.run(["python3", "modules/crypto/galxe_farm.py"], capture_output=True, text=True)
    print(result.stdout)
    with open("logs/farm_log.txt", "a") as log:
        log.write(f"
[{datetime.now()}] Galxe farm result:
{result.stdout}")

def send_funds():
    print("\n===== Вивід BNB на головний гаманець =====")
    result = subprocess.run(["python3", WITHDRAW_SCRIPT], capture_output=True, text=True)
    print(result.stdout)
    with open("logs/withdraw_log.txt", "a") as log:
        log.write(f"
[{datetime.now()}] Withdraw result:
{result.stdout}")

def main():
    run_farm()
    time.sleep(5)
    send_funds()
    print("\n===== Завершено =====")

if __name__ == "__main__":
    main()
