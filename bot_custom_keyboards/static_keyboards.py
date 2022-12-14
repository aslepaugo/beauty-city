from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

async def get_static_keyboard(buttons: list):
    formed_keyboard = []
    for button in buttons:
        formed_keyboard.append(KeyboardButton(text=button))
    return ReplyKeyboardMarkup(
        keyboard=[
            formed_keyboard
        ],
        resize_keyboard=True
    )

ok_button_request_location = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='OK', request_location=True),
            KeyboardButton(text='Выбрать салон из списка...')
            
        ]
    ],
    resize_keyboard=True
)
