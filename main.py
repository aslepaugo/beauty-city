from loguru import logger

logger.add(
    'debug.log',
    format='{time}  {level}  {message}',
    level='DEBUG',
)


async def on_startup(dp):
    from utils.notify_admins import on_startup_notify
    await on_startup_notify(dp)
    logger.info('Бот запущен')
    
if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp
    
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
    