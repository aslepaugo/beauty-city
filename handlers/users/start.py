from aiogram import types
from loader import dp
from custom_keyboards.static_keyboards import *
from custom_keyboards.dynamic_keyboards import form_2_row_keyboard
from states.global_states import Global
from aiogram.dispatcher import FSMContext
from transitions.transitions import *

services = ['Парикмахерская', 'Маникюр', 'Педикюр']
masters = ['мастер1', 'Мастер2', 'мастер3', 'Мастер4', 'Мастер5', 'Мастер6', 'Мастер7', 'Мастер8']

@dp.message_handler(commands='start')
async def command_start(message: types.Message):
    await message.answer(
        f'Вас приветствует электронный администратор салонов Beauty city!\n'
        f'Здесь Вы сможете записаться на наши услуги', reply_markup=st1_kb_menu
    )

@dp.message_handler(text=['Записаться', 'Начать заново'])
async def command_start_oder(message: types.Message):
    await message.answer('Выберите способ записи:', reply_markup=st2_kb_menu)
    await Global.start_oder.set()

@dp.message_handler(state=Global.start_oder)
async def handler_start_oder(message: types.Message, state: FSMContext):
    if message.text == 'В салон...':
        await state.update_data(way='1')
        await goto_salons(message, state)

    if message.text == 'На услугу...':
        await state.update_data(way='2')
        await goto_services(message, state)

    if message.text == 'К мастеру...':
        await state.update_data(way='3')
        await goto_masters (message, state)

@dp.message_handler(text='Личный кабинет')
async def command_inline(message: types.Message):
    await message.answer('Добро пожаловать в личный кабинет!')
    await message.answer('Данные о регистрации(имя, телефон)', reply_markup=personal_account_kb)
      