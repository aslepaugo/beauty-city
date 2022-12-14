from aiogram import types
from states.global_states import Global_states
from aiogram.dispatcher import FSMContext

from bot_auxiliary.loader import dp
from bot_custom_keyboards.static_keyboards import get_static_keyboard
from transitions.transitions import *


    
@dp.message_handler(state=Global_states.start_select_service)
async def handler_start_select_service(message: types.Message, state: FSMContext):
    selected_service = message.text
    if selected_service == 'Шаг назад':
        await goto_services(message, state)
    else:
        await state.update_data(selected_service= selected_service)
        await message.answer(
            f'Выбрана услуга: {selected_service}',
            reply_markup=await get_static_keyboard(['Подтвердить выбор услуги', 'Выбрать другую услугу'])
        )
        await Global_states.confirm_service.set()

@dp.message_handler(state=Global_states.confirm_service)
async def command_confirm_service(message: types.Message, state: FSMContext):
    if message.text == 'Подтвердить выбор услуги':
        way = await state.get_data()
        
        if way['way'] == '1':
            await goto_masters(message, state)
            
        if way['way'] == '2':
            await goto_salons(message, state)

        if way['way'] == '3':
            await goto_salons(message, state)

    elif message.text == 'Выбрать другую услугу':
        await goto_services(message, state)


