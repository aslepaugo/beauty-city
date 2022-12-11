from aiogram import types
from loader import dp
from custom_keyboards.static_keyboards import *
from states.global_states import Global
from aiogram.dispatcher import FSMContext
from transitions.transitions import *


@dp.message_handler(state=Global.finish_order)
async def handler_finish_order(message: types.Message, state: FSMContext):
    if message.text == 'Подтвердить заказ':
        # занести заказ в базу
        await message.answer(
            'Заказ принят!'
        )
        await goto_start(message, state)
    else:
        await goto_start(message, state)
        