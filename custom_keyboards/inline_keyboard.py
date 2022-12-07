from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

inline_kb_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Записаться', callback_data='тыц'),
            InlineKeyboardButton(text='Личный кабинет', callback_data='тыц2')
        ]
    ]
)