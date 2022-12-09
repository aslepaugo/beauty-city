from aiogram import types
from loader import dp
from custom_keyboards.static_keyboards import st3_kb_menu
from custom_keyboards.dynamic_keyboards import form_2_row_keyboard

import orm_commands
#from asgiref.sync import sync_to_async
# тестовые данные
nearest_salon = 'Салон "Ближайший" Адрес самый близкий 12'


@dp.message_handler(text='В салон...')
async def command_inline(message: types.Message):
    await message.answer('Вы можете выбрать ближайший к Вам салон,\n либо выбрать салон из списка:', reply_markup=st3_kb_menu)

@dp.message_handler(text='Выбрать салон из списка...')
async def command_inline(message: types.Message):
    salons = orm_commands.get_all_salons()
    await message.answer('Выберите нужный салон:', reply_markup=form_2_row_keyboard(salons))

@dp.message_handler(text='Ближайший салон')
async def command_inline(message: types.Message):
    await message.answer(f'Ближайший салон: {nearest_salon}')

@dp.message_handler(content_types=['location'])
async def handle_location(message: types.Message):
    latitude = message.location.latitude
    longitude = message.location.longitude
    user_coords = {'lat': latitude, 'lon': longitude}
    await message.answer(user_coords, reply_markup=types.ReplyKeyboardRemove())