from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import os

bot = Bot(token="7626770291:AAG3UC1h3vt1aR9h0ALAqg3oo9RlvsMGSzI")
dp = Dispatcher(bot)

menu = ReplyKeyboardMarkup(resize_keyboard=True)
menu.add(KeyboardButton("🚀 Фармити"))
menu.row(KeyboardButton("💰 Баланс"), KeyboardButton("📤 Вивести"))
menu.row(KeyboardButton("📊 Статистика"), KeyboardButton("⚙️ Статус акаунтів"))
menu.row(KeyboardButton("🔁 Перезапуск"), KeyboardButton("📂 Експорт логів"))

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer("Привіт, Тоні! Обери дію:", reply_markup=menu)

@dp.message_handler(lambda message: message.text == "🚀 Фармити")
async def farm(message: types.Message):
    os.system("python3 main.py")

@dp.message_handler(lambda message: message.text == "💰 Баланс")
async def balance(message: types.Message):
    os.system("python3 check_balance.py")

@dp.message_handler(lambda message: message.text == "📤 Вивести")
async def withdraw(message: types.Message):
    os.system("python3 withdraw.py")

if __name__ == "__main__":
    executor.start_polling(dp)
