from aiogram import types
from loader import dp
from custom_keyboards.static_keyboards import *
from custom_keyboards.dynamic_keyboards import form_2_row_keyboard
from states.global_states import Global
from aiogram.dispatcher import FSMContext
from transitions.transitions import *


@dp.message_handler(state=Global.start_select_master)
async def handler_start_select_master(message: types.Message, state: FSMContext):
    selected_master = message.text
    await state.update_data(selected_master=selected_master)
    await message.answer(
        f'Выбран мастер: {selected_master}',
        reply_markup=confirm_master_kb
    )
    await Global.confirm_master.set()

@dp.message_handler(state=Global.confirm_master)
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
        await message.answer(
                'Выберите нужную процедуру:',
                reply_markup=form_2_row_keyboard(masters)
            )
        await Global.start_select_master.set()