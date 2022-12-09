from aiogram import types
from loader import dp
from custom_keyboards.static_keyboards import st3_kb_menu
from custom_keyboards.dynamic_keyboards import form_2_row_keyboard

# тестовые данные
nearest_salon = 'Салон "Ближайший" Адрес самый близкий 12'
salons = ['Салон1 Адрес1','Салон2 Адрес2', 'Салон3 Адрес3', 'Салон4 Адрес4', 'Салон5 Адрес5', 'Салон6 Адрес6']

    
@dp.message_handler(text='В салон...')
async def command_inline(message: types.Message):
    await message.answer('Вы можете выбрать ближайший к Вам салон,\n либо выбрать салон из списка:', reply_markup=st3_kb_menu)

@dp.message_handler(text='Выбрать салон из списка...')
async def command_inline(message: types.Message):
    await message.answer('Выберите нужный салон:', reply_markup=form_2_row_keyboard(salons))

@dp.message_handler(text='Ближайший салон')
async def command_inline(message: types.Message):
    await message.answer(f'Ближайший салон: {nearest_salon}')