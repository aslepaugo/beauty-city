from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def form_2_row_keyboard(buttons: list):
    first_row_buttons = []
    i = 0
    formed_buttons = []
    for button in buttons:
        first_row_buttons.append(KeyboardButton(button))
        i+=1
        if i == 2:
            formed_buttons.append(first_row_buttons)
            i=0
            first_row_buttons = []

    dynamic_kb_menu = ReplyKeyboardMarkup(
        keyboard=formed_buttons,
        resize_keyboard=True
    )
    return dynamic_kb_menu
