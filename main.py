import logging
import aiogram.utils.markdown as md
from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import Message, ParseMode, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
import csv

BOT_TOKEN = "5959278377:AAGv9u-0MPyOBUntGyOwLTh0Oiz1nhqdv3M"
logging.basicConfig(level=logging.INFO)

bot = Bot(BOT_TOKEN)
storage = MemoryStorage()

dp = Dispatcher(bot, storage=storage)


@dp.message_handler(commands=['start'])
async def start_menu(message: Message):
    await message.answer('Xush kelibsiz\n😉👇👇👇👇👇👇👇👇👇👇')


@dp.message_handler()
async def anything_handler(message: Message):
    vovl = 'aeouiAEIOU'
    s = 0
    for i in message.text:
        if i in vovl:
            s += 1
    if s > 5:
        await message.delete()
    else:
        pass


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
