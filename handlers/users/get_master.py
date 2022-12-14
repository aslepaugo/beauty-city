from aiogram import types
from states.global_states import Global_states
from aiogram.dispatcher import FSMContext

from bot_auxiliary.loader import dp
from bot_custom_keyboards.static_keyboards import get_static_keyboard
from transitions.transitions import *


@dp.message_handler(state=Global_states.start_select_master)
async def handler_start_select_master(message: types.Message, state: FSMContext):
    selected_master = message.text
    if selected_master == 'Шаг назад':
        await goto_masters(message, state)
    else:
        await state.update_data(selected_master=selected_master)
        await message.answer(
            f'Выбран мастер: {selected_master}',
            reply_markup=await get_static_keyboard(['Подтвердить выбор мастера', 'Выбрать другого мастера'])
        )
        await Global_states.confirm_master.set()

@dp.message_handler(state=Global_states.confirm_master)
async def command_confirm_master(message: types.Message, state: FSMContext):
    if message.text == 'Подтвердить выбор мастера':
        way = await state.get_data()
        
        if way['way'] == '1':
            await goto_date(message, state)

        if way['way'] == '2':
            await goto_date(message, state)
            
        if way['way'] == '3':
            await goto_services(message, state)

    elif message.text == 'Выбрать другого мастера':
        await goto_masters(message, state)