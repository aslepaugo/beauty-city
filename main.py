import os

from loguru import logger
from bot_auxiliary import on_startup_notify, set_default_commands


logger.add(
    os.path.join('log', 'debug.log'),
    format='{time}  {level}  {message}',
    level='DEBUG',
)

async def on_startup(dp):
    await on_startup_notify(dp)
    await set_default_commands(dp)
    logger.info('Бот запущен')
    
if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp
    
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
    