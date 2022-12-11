from aiogram import types
from loader import dp, cursor
from custom_keyboards.dynamic_keyboards import form_2_row_keyboard
from custom_keyboards.static_keyboards import *
from states.global_states import Global
from aiogram.dispatcher import FSMContext
from transitions.transitions import *