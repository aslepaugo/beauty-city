from aiogram import types
from custom_keyboards.dynamic_keyboards import form_2_row_keyboard
from custom_keyboards.static_keyboards import *
from states.global_states import Global
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove


async def check_date(date: str):
    pass #проверка даты на корректность в широком смысле
# - Правильный формат, - не в прошлом - есть свободные места на эту дату
    if True:
        return date
    else:
        return 'Описание что не так'