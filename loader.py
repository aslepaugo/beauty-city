from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from os import getenv

load_dotenv()

TG_BOT_TOKEN = getenv('TG_BOT_TOKEN')

bot = Bot(TG_BOT_TOKEN)

dp = Dispatcher(bot)
