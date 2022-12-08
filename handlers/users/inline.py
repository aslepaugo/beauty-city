from aiogram import types
from loader import dp
from aiogram.types import ReplyKeyboardRemove
from custom_keyboards.inline_keyboard import inline_kb_menu


@dp.message_handler(text='Инлайн клавиатура')
async def command_inline(message: types.Message):
    await message.answer(
        'Дальше инлайн клавиатура',
        reply_markup=ReplyKeyboardRemove()
    )
    await message.answer('!', reply_markup=inline_kb_menu)