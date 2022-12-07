from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


kb_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Записаться'),
            KeyboardButton(text='Личный кабинет'),
        ],
        [
            KeyboardButton(text='Инлайн клавиатура')
        ]
    ],
    resize_keyboard=True
)