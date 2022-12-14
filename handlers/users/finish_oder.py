from aiogram import types
from states.global_states import Global_states
from aiogram.dispatcher import FSMContext

from transitions.transitions import *
from bot_auxiliary.loader import dp
from bot_custom_keyboards.static_keyboards import *


@dp.message_handler(state=Global_states.finish_order)
async def handler_finish_order(message: types.Message, state: FSMContext):
    if message.text == 'Подтвердить заказ':
        data = await state.get_data()
        print(data)
        await message.answer(
            'Заказ принят!'
        )
        await goto_start(message, state)
    else:
        await goto_start(message, state)
        