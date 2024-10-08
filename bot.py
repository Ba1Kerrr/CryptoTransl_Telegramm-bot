import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram import F
import requests
from bs4 import BeautifulSoup
from parse import Bit,Eth
# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token="6434260055:AAE7JMZQZ45ijJAO2xYPChMnu3N35lhJ8Dk")
# Диспетчер
dp = Dispatcher()

# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text="bit"),
            types.KeyboardButton(text="eth") 
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выберите интересующую валюту (криптовалюту)"
    )
    await message.answer("Привет , Я бот для обмена криптовалютой.Я могу обменивать bitcoin и ethereum, если ты хочешь начать  обменивать валюту - просто напиши ее название - made by BA1KERRR  ↨",reply_markup=keyboard)


@dp.message(F.text.lower() == "eth")
async def with_puree(message: types.Message):
    await message.reply(Eth())

@dp.message(F.text.lower() == "bit")
async def without_puree(message: types.Message):
    await message.reply(Bit())
# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())