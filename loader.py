from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from dotenv import load_dotenv
from os import getenv

load_dotenv()

TG_BOT_TOKEN = getenv('TG_BOT_TOKEN')

bot = Bot(TG_BOT_TOKEN)

storage = MemoryStorage()

dp = Dispatcher(bot, storage=storage)


