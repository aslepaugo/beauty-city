from aiogram import types
from loader import dp
from custom_keyboards.static_keyboards import *
from states.global_states import Global
from aiogram.dispatcher import FSMContext
from transitions.transitions import *

    
@dp.message_handler(state=Global.start_select_slot)
async def handler_start_select_slot(message: types.Message, state: FSMContext):
    selected_slot = message.text
    await state.update_data(selected_slot=selected_slot)
    await message.answer(
        f'Выбрано время: {selected_slot}',
        reply_markup=confirm_slot_kb
    )
    await Global.confirm_slot.set()

@dp.message_handler(state=Global.confirm_slot)
async def command_confirm_slot(message: types.Message, state: FSMContext):
    if message.text == 'Подтвердить время':
        await goto_registration(message, state)

    elif message.text == 'Выбрать другое время':
        await goto_slot(message, state)
