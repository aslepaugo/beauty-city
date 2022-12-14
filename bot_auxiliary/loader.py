from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from dotenv import load_dotenv
from os import getenv
import redis

load_dotenv()

TG_BOT_TOKEN = getenv('TG_BOT_TOKEN')

bot = Bot(TG_BOT_TOKEN)

storage = MemoryStorage()

pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
redis_cursor = redis.Redis(connection_pool=pool, charset='utf-8', decode_responses=True)

dp = Dispatcher(bot, storage=storage)


