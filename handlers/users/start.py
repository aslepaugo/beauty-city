from aiogram import types
from  states.global_states import Global_states
from aiogram.dispatcher import FSMContext

from bot_auxiliary.loader import dp
from bot_custom_keyboards.static_keyboards import get_static_keyboard
from transitions.transitions import *

from orm_commands import is_user_registered

@dp.message_handler(commands='start')
async def command_start(message: types.Message):
    await message.answer(
        f'Вас приветствует электронный администратор салонов Beauty city!\n'
        f'Здесь Вы сможете записаться на наши услуги',
        reply_markup=await get_static_keyboard(['Записаться', 'Личный кабинет'])
    )
@dp.message_handler(state=Global_states.start_bot)
async def handler_start(message: types.Message, state: FSMContext):
    await message.answer(
        f'Вас приветствует электронный администратор салонов Beauty city!\n'
        f'Здесь Вы сможете записаться на наши услуги',
        reply_markup=await get_static_keyboard(['Записаться', 'Личный кабинет'])
    )
    await state.finish()

@dp.message_handler(text=['Записаться', 'Начать заново'])
async def command_start_oder(message: types.Message):
    await message.answer(
        'Выберите способ записи:',
        reply_markup=await get_static_keyboard(['В салон...', 'На услугу...', 'К мастеру...'])
    )
    await Global_states.start_oder.set()

@dp.message_handler(state=Global_states.start_oder)
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
async def command_inline(message: types.Message, state: FSMContext):
    await message.answer('Добро пожаловать в личный кабинет!')
    user = is_user_registered(message.from_id)
    if user:
        await message.answer(
            f'Данные о регистрации\n'
            f'Имя: {user.get("fullname")}\n'
            f'Телефон: {user.get("phone_number")}\n'
            f'Telegram id: {user.get("telegram_id")}',
            reply_markup=await get_static_keyboard(['Главное меню'])
        )
    else:
        await message.answer(
            'Нет данных о регистрации',
            reply_markup=await get_static_keyboard(['Главное меню'])
        )

@dp.message_handler(text='Главное меню')
async def command_inline(message: types.Message, state: FSMContext):
   await goto_start(message, state)

      