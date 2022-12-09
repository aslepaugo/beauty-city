from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


personal_account_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Текущие записи'),
            KeyboardButton(text='Выполненные услуги'),
            KeyboardButton(text='Регистрация')  #для тестов
        ]
    ],
    resize_keyboard=True
)

st1_kb_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Записаться'),
            KeyboardButton(text='Личный кабинет'),
        ],
    ],
    resize_keyboard=True
)

st2_kb_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='В салон...'),
            KeyboardButton(text='На услугу...'),
            KeyboardButton(text='К мастеру...'),
        ],
    ],
    resize_keyboard=True
)
st3_kb_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Ближайший салон'),
            KeyboardButton(text='Выбрать салон из списка...'),
        ],
    ],
    resize_keyboard=True
)
confirm_oder_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Подтвердить заказ'),
            KeyboardButton(text='Начать заново')
        ]
    ],
    resize_keyboard=True
)

approval_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Согласен(на)'),
            KeyboardButton(text='Отказ')
        ]
    ],
    resize_keyboard=True
)

