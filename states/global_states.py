from aiogram.dispatcher.filters.state import State, StatesGroup


class Global(StatesGroup):
    start_oder = State()

    start_select_salon = State()
    select_salon = State()
    confirm_salon = State()

    start_select_service = State()
    confirm_service = State()
    
    start_select_master = State()
    confirm_master = State()

    start_select_date = State()

    start_select_slot = State()
    confirm_slot = State()

    start_registration = State()
    enter_name = State()
    enter_phone_number = State()
    cancel = State()

    finish_order = State()