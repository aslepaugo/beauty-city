from aiogram.dispatcher.filters.state import State, StatesGroup


class Global(StatesGroup):
    start_oder = State()

    start_select_salon = State()
    select_salon = State()
    select_nearest_salon = State()
    confirm_salon = State()

    start_select_service = State()
    confirm_service = State()
    
    start_select_master = State()
    confirm_master = State()

    