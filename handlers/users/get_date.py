from aiogram import types
from loader import dp
from custom_keyboards.static_keyboards import *
from states.global_states import Global
from aiogram.dispatcher import FSMContext
from transitions.transitions import *
from transitions.check_date import check_date


@dp.message_handler(state=Global.start_select_date)
async def handler_start_select_date(message: types.Message, state: FSMContext):
    selected_date = message.text
    if await check_date(selected_date) == selected_date:
        await state.update_data(selected_date=selected_date)
        await message.answer(f'Выбрана дата:{selected_date}')
        await goto_slot(message, state)

