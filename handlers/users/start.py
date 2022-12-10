from aiogram import types
from loader import dp
from custom_keyboards.static_keyboards import st1_kb_menu, st2_kb_menu, personal_account_kb


@dp.message_handler(commands='start')
async def command_start(message: types.Message):
    await message.answer(
        f'Вас приветствует электронный администратор салонов Beauty city!\n'
        f'Здесь Вы сможете записаться на наши услуги', reply_markup=st1_kb_menu
    )

@dp.message_handler(text=['Записаться', 'Начать заново'])
async def command_inline(message: types.Message):
    await message.answer('Выберите способ записи:', reply_markup=st2_kb_menu)

@dp.message_handler(text='Личный кабинет')
async def command_inline(message: types.Message):
    await message.answer('Добро пожаловать в личный кабинет!')
    await message.answer('Данные о регистрации(имя, телефон)', reply_markup=personal_account_kb)
      