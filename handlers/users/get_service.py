from aiogram import types
from loader import dp
from custom_keyboards.static_keyboards import *
from states.global_states import Global
from aiogram.dispatcher import FSMContext
from transitions.transitions import *

    
@dp.message_handler(state=Global.start_select_service)
async def handler_start_select_service(message: types.Message, state: FSMContext):
    selected_service = message.text
    await state.update_data(selected_service= selected_service)
    await message.answer(
        f'Выбрана услуга: {selected_service}',
        reply_markup=confirm_service_kb
    )
    await Global.confirm_service.set()

@dp.message_handler(state=Global.confirm_service)
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


