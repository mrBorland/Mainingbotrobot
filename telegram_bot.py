from aiogram import Bot, Dispatcher, types, executor
from aiogram.dispatcher.filters import Command

# Твій токен і chat_id
API_TOKEN = "7567566641:AAGKaV2Qx5GrhXx_a2Ju_h7KrlvJIRVRX1M8"
OWNER_ID = 6821675571  # Taras

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start_handler(message: types.Message):
    if message.from_user.id == OWNER_ID:
        await message.reply("Привіт, Тоні! Бот активний.")
    else:
        await message.reply("Доступ заборонено.")

@dp.message_handler(commands=["stats"])
async def stats_handler(message: types.Message):
    if message.from_user.id == OWNER_ID:
        await message.reply("Статистика: 250 акаунтів, 5 платформ, USDT прибуток за сьогодні: $42.60")
    else:
        await message.reply("Доступ заборонено.")

@dp.message_handler(commands=["farm"])
async def farm_handler(message: types.Message):
    if message.from_user.id == OWNER_ID:
        await message.reply("Фарм запущено. Перевіряю акаунти...")
        # Тут буде реальна логіка фарму
    else:
        await message.reply("Доступ заборонено.")

@dp.message_handler(commands=["withdraw"])
async def withdraw_handler(message: types.Message):
    if message.from_user.id == OWNER_ID:
        await message.reply("Вивід коштів розпочато...")
        # Тут буде логіка виводу
    else:
        await message.reply("Доступ заборонено.")

if __name__ == "__main__":
    executor.start_polling(dp)
