from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def form_2_row_keyboard(buttons: list):
    first_row_buttons = []
    i = len(buttons)
    formed_buttons = []
    for button in buttons:
        first_row_buttons.append(KeyboardButton(button))
        i -= 1
        if len(first_row_buttons) == 2:
            formed_buttons.append(first_row_buttons)
            first_row_buttons = []
        if i == 0:
            formed_buttons.append(first_row_buttons)

    dynamic_kb_menu = ReplyKeyboardMarkup(
        keyboard=formed_buttons,
        resize_keyboard=True
    )
    return dynamic_kb_menu

