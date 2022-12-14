from aiogram import types
from states.global_states import Global_states
from aiogram.dispatcher import FSMContext

from bot_auxiliary.loader import dp
from bot_custom_keyboards.static_keyboards import *
from transitions.transitions import *
from transitions.check_date import check_date


@dp.message_handler(state=Global_states.start_select_date)
async def handler_start_select_date(message: types.Message, state: FSMContext):
    selected_date = message.text
    is_valid_date = await check_date(selected_date, state)
    if is_valid_date[0]:
        await state.update_data(selected_date=is_valid_date[1])
        await message.answer(f'Выбрана дата:{selected_date}')
        await goto_slot(message, state)
    else:
        await goto_date(message, state, is_valid_date[1])


