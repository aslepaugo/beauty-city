from aiogram import types
from states.global_states import Global_states
from aiogram.dispatcher import FSMContext

from bot_auxiliary.loader import dp
from bot_custom_keyboards.static_keyboards import get_static_keyboard
from transitions.transitions import *

    
@dp.message_handler(state=Global_states.start_select_slot)
async def handler_start_select_slot(message: types.Message, state: FSMContext):
    selected_slot = message.text
    if selected_slot == 'Шаг назад':
        await goto_slot(message, state)
    else:
        await state.update_data(selected_slot=selected_slot)
        await message.answer(
            f'Выбрано время: {selected_slot}',
            reply_markup=await get_static_keyboard(['Подтвердить время', 'Выбрать другое время'])
        )
        await Global_states.confirm_slot.set()

@dp.message_handler(state=Global_states.confirm_slot)
async def command_confirm_slot(message: types.Message, state: FSMContext):
    if message.text == 'Подтвердить время':
        await goto_registration(message, state)

    elif message.text == 'Выбрать другое время':
        await goto_slot(message, state)
