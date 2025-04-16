from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

# Твій Telegram Token
BOT_TOKEN = "7626770291:AAG3UC1h3vt1aR9h0ALAg3oo9R1vsNGSzI"

# Ініціалізація бота і диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# Хендлер на /start
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer("Привіт, Тарас! Бот активний.")

# Запуск бота
if __name__ == '__main__':
    executor.start_polling(dp)
