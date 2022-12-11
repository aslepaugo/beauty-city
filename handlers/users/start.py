from aiogram import types
from loader import dp
from custom_keyboards.static_keyboards import *
from states.global_states import Global
from aiogram.dispatcher import FSMContext
from transitions.transitions import *
from orm_commands import is_user_registered

@dp.message_handler(commands='start')
async def command_start(message: types.Message):
    await message.answer(
        f'Вас приветствует электронный администратор салонов Beauty city!\n'
        f'Здесь Вы сможете записаться на наши услуги', reply_markup=st1_kb_menu
    )
@dp.message_handler(state=Global.start_bot)
async def handler_start(message: types.Message, state: FSMContext):
    await message.answer(
        f'Вас приветствует электронный администратор салонов Beauty city!\n'
        f'Здесь Вы сможете записаться на наши услуги', reply_markup=st1_kb_menu
    )
    await state.finish()

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
async def command_inline(message: types.Message, state: FSMContext):
    await message.answer('Добро пожаловать в личный кабинет!')
    user = is_user_registered(message.from_id)
    if user:
        await message.answer(
            f'Данные о регистрации\n'
            f'Имя: {user.get("fullname")}\n'
            f'Телефон: {user.get("phone_number")}\n'
            f'Telegram id: {user.get("telegram_id")}',
            reply_markup=personal_account_kb
        )
    else:
        await message.answer(
            'Нет данных о регистрации',
            reply_markup=personal_account_kb
        )

@dp.message_handler(text='Главное меню')
async def command_inline(message: types.Message, state: FSMContext):
   await goto_start(message, state)

      