from aiogram.dispatcher.filters.state import State, StatesGroup


class User_registration(StatesGroup):
    enter_name = State()
    enter_phone_number = State()

