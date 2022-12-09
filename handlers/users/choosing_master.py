from aiogram import types
from loader import dp
from custom_keyboards.static_keyboards import st3_kb_menu
from custom_keyboards.dynamic_keyboards import form_2_row_keyboard


# тестовые данные
masters = ['мастер1', 'Мастер2', 'мастер3', 'Мастер4', 'Мастер5', 'Мастер6', 'Мастер7', 'Мастер8']

    
@dp.message_handler(text='К мастеру...')
async def command_inline(message: types.Message):
    await message.answer('Выберите мастера:', reply_markup=form_2_row_keyboard(masters))
