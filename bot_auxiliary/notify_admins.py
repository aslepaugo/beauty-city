
from aiogram import Dispatcher

from bot_auxiliary.config import admin_ids


async def on_startup_notify(dp: Dispatcher):
    for admin in admin_ids:
        text = 'Бот запущен и готов к работе'
        await dp.bot.send_message(chat_id=admin, text=text)
