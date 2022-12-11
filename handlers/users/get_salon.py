from aiogram import types
from loader import dp, cursor
from custom_keyboards.dynamic_keyboards import form_2_row_keyboard
from custom_keyboards.static_keyboards import *
from states.global_states import Global
from aiogram.dispatcher import FSMContext
from transitions.transitions import *

import orm_commands
#from asgiref.sync import sync_to_async


@dp.message_handler(state=Global.start_select_salon)
async def handler_from_salon(message: types.Message, state: FSMContext):
    if message.text == 'Выбрать салон из списка...':
        await Global.select_salon.set()
        await message.answer(
            f'Выберите салон из списка:', reply_markup=form_2_row_keyboard(salons)
        )
    elif message.text == 'Ближайший салон':
        #redis cache
        data = await state.get_data()
        cursor.flushall()
        for key, value in data.items():
            cursor.set(key, value)
        #------------
        await state.finish()
        await message.answer(
            'Будет определено Ваше местоположение, данная функция работает только на смартфонах',
            reply_markup=ok_button
        )

@dp.message_handler(content_types=['location'])
async def handle_location(message: types.Message, state: FSMContext):
    latitude = message.location.latitude
    longitude = message.location.longitude
    user_coords = {'lat': latitude, 'lon': longitude}
    # nearest_salon = orm_commands.get_nearest_salon(user_coords)

    #redis cache-----------
    redis_dict = {}
    for key in cursor.keys():
        redis_dict[key.decode('utf-8')] = cursor.get(key).decode('utf-8')
    cursor.flushdb()    
    await state.update_data(redis_dict)
    #-----------------------
    await state.update_data(selected_salon=nearest_salon['title'])
    reply = f"Ближайший салон: {nearest_salon['title']} ({nearest_salon['address']})"
    await message.answer(reply, reply_markup=confirm_salon_kb)
    await Global.confirm_salon.set()  


@dp.message_handler(state=Global.select_salon)
async def command_select_salon(message: types.Message, state: FSMContext):
    selected_salon = message.text    
    await state.update_data(selected_salon=selected_salon)
    await message.answer(
        f'Выбран салон: {selected_salon}',
        reply_markup=confirm_salon_kb
    )
    await Global.confirm_salon.set()

@dp.message_handler(state=Global.confirm_salon)
async def command_confirm_salon(message: types.Message, state: FSMContext):
    if message.text == 'Подтвердить салон':
        way = await state.get_data()
        if way['way'] == '1':
            await goto_services(message, state)

        if way['way'] == '2':
            await goto_masters(message, state)

        if way['way'] == '3':
            await goto_date(message, state)
            

    elif message.text == 'Выбрать салон из списка...':
        await message.answer(
            f'Выберите салон из списка:', reply_markup=form_2_row_keyboard(salons)
        )
        await Global.select_salon.set()
