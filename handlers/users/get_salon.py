from aiogram import types
from states.global_states import Global_states
from aiogram.dispatcher import FSMContext

from bot_auxiliary.loader import dp, redis_cursor
from bot_custom_keyboards.static_keyboards import get_static_keyboard, ok_button_request_location
from transitions.transitions import *

import orm_commands


@dp.message_handler(state=Global_states.start_select_salon)
async def handler_from_salon(message: types.Message, state: FSMContext):
    if message.text == 'Выбрать салон из списка...':
        await goto_salons_from_list(message, state)
    elif message.text == 'Ближайший салон':
        #----------redis cache
        data = await state.get_data()
        redis_cursor.flushall()
        for key, value in data.items():
            redis_cursor.set(key, value)
        #---------------------
        await state.finish()
        await message.answer(
            'Будет определено Ваше местоположение, данная функция работает только на смартфонах',
            reply_markup=ok_button_request_location
        )

@dp.message_handler(text='Выбрать салон из списка...')
async def handle_location(message: types.Message, state: FSMContext):
    await goto_salons(message, state)
      #redis cache-----------
    redis_dict = {}
    for key in redis_cursor.keys():
        redis_dict[key.decode('utf-8')] = redis_cursor.get(key).decode('utf-8')
    redis_cursor.flushdb()    
    await state.update_data(redis_dict)
    #-----------------------
    


@dp.message_handler(content_types=['location'])
async def handle_location(message: types.Message, state: FSMContext):
    latitude = message.location.latitude
    longitude = message.location.longitude
    user_coords = {'lat': latitude, 'lon': longitude}
    nearest_salon = orm_commands.get_nearest_salon(user_coords)

    #redis cache-----------
    redis_dict = {}
    for key in redis_cursor.keys():
        redis_dict[key.decode('utf-8')] = redis_cursor.get(key).decode('utf-8')
    redis_cursor.flushdb()    
    await state.update_data(redis_dict)
    #-----------------------
    await state.update_data(selected_salon=nearest_salon['title'])
    reply = f"Ближайший салон: {nearest_salon['title']} ({nearest_salon['address']})"
    await message.answer(
        reply,
        reply_markup=await get_static_keyboard(['Подтвердить салон', 'Выбрать другой салон']))
    await Global_states.confirm_salon.set()  


@dp.message_handler(state=Global_states.select_salon)
async def command_select_salon(message: types.Message, state: FSMContext):
    selected_salon = message.text
    if selected_salon == 'Шаг назад':
        await goto_salons(message, state)
    else:    
        await state.update_data(selected_salon=selected_salon)
        await message.answer(
            f'Выбран салон: {selected_salon}',
            reply_markup=await get_static_keyboard(['Подтвердить салон', 'Выбрать другой салон'])
        )
        await Global_states.confirm_salon.set()

@dp.message_handler(state=Global_states.confirm_salon)
async def command_confirm_salon(message: types.Message, state: FSMContext):
    if message.text == 'Подтвердить салон':
        way = await state.get_data()
        if way['way'] == '1':
            await goto_services(message, state)

        if way['way'] == '2':
            await goto_masters(message, state)

        if way['way'] == '3':
            await goto_date(message, state)
            

    elif message.text == 'Выбрать другой салон':
        await goto_salons(message, state)