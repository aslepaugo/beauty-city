from aiogram import types
from loader import dp
from custom_keyboards.text_keyboard import kb_menu


@dp.message_handler(commands='start')
async def command_start(message: types.Message):
    await message.answer(
        f'Привет {message.from_user.full_name}\n'   #это для удобства потом можно убрать
        f'Твой ID {message.from_user.id}\n\n', reply_markup=kb_menu
    )
      