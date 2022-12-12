from loader import dp
from aiogram import types
from aiogram.dispatcher import FSMContext
from states.global_states import Global
import transitions.transitions
from custom_keyboards.static_keyboards import clear_button
import orm_commands


def unify_phone(raw_input: str):
    only_numbers = [number for number in raw_input if number in '0123456789']
    only_numbers = ' '.join(only_numbers).split()

    if (11 >= len(only_numbers) >= 10) and (''.join(only_numbers[-10:-9]) in '789'):
        only_numbers = only_numbers[-10:]
        unified_phone_number = f"+7 ({''.join(only_numbers[:3])}) {''.join(only_numbers[3:6])}-{''.join(only_numbers[6:8])}-{''.join(only_numbers[8:10])}"
        return unified_phone_number
    else:
        return False


@dp.message_handler(state=Global.start_registration)
async def register(message: types.Message, state: FSMContext):
    if message.text == 'Согласен(на)':
        await message.answer(
            'Введите своё имя:',
            reply_markup=types.ReplyKeyboardRemove()
        )
        await Global.enter_name.set()
    else:
        await message.answer(
            'Для продолжения необходимо дать разрешение на обработку персональных данных',
            reply_markup=clear_button
        )
        await Global.cancel.set()

@dp.message_handler(state=Global.cancel)
async def handler_cancel(message: types.Message, state: FSMContext):
    await transitions.transitions.goto_registration(message, state) 

@dp.message_handler(state=Global.enter_name)
async def state_enter_name(message: types.Message, state: FSMContext):
    user_name = message.text
    await state.update_data(fullname=user_name)
    await message.answer('Введите номер телефона:')
    await Global.enter_phone_number.set()

@dp.message_handler(state=Global.enter_phone_number)
async def state_enter_phone_number(message: types.Message, state: FSMContext):
    phone_number = unify_phone(message.text)
    if phone_number:
        await state.update_data(phone_number=phone_number)
        registration_data = await state.get_data()
        registration_data['telegram_id'] = message.from_id
        await message.answer(
            f'Имя: {registration_data.get("fullname")}\n'
            f'Телефон: {phone_number}\n'
        )
        orm_commands.User.objects.get_or_create(
            telegram_id=registration_data['telegram_id'],
            fullname=registration_data.get("fullname"),
            phone_number=phone_number
            )
        await state.update_data(registration_data)
        await transitions.transitions.goto_finish_order(message, state)
    else:
        await message.answer(
            'Введен некорректный номер телефона, попробуйте еще раз'
        )