from aiogram import types
from loader import dp
from custom_keyboards.static_keyboards import *
from states.global_states import Global
from aiogram.dispatcher import FSMContext
from transitions.transitions import *
from transitions.check_date import check_date