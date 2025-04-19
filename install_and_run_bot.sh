
#!/data/data/com.termux/files/usr/bin/bash

# Створення робочої директорії
mkdir -p ~/fixbot/Mainingbotrobot && cd ~/fixbot/Mainingbotrobot

# Завантаження архіву з GitHub
curl -L -o Mainingbotrobot_package.zip "https://github.com/mrBorland/Mainingbotrobot/raw/main/Mainingbotrobot_package.zip"

# Розпакування
unzip -o Mainingbotrobot_package.zip

# Видалення архіву після розпакування
rm Mainingbotrobot_package.zip

# Встановлення залежностей (за наявності requirements.txt)
if [ -f "requirements.txt" ]; then
  pip install -r requirements.txt
fi

# Запуск основного скрипта (якщо є farm_launcher.py)
if [ -f "farm_launcher.py" ]; then
  python3 farm_launcher.py
else
  echo "[!] Файл farm_launcher.py не знайдено"
fi
