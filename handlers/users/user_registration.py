from loader import dp
from aiogram import types
from aiogram.dispatcher import FSMContext
from states.user_registration_states import User_registration
from custom_keyboards.static_keyboards import approval_kb


def unify_phone(raw_input: str):
    only_numbers = [number for number in raw_input if number in '0123456789']
    only_numbers = ' '.join(only_numbers).split()

    if (11 >= len(only_numbers) >= 10) and (''.join(only_numbers[-10:-9]) in '789'):
        only_numbers = only_numbers[-10:]
        unified_phone_number = f"+7 ({''.join(only_numbers[:3])}) {''.join(only_numbers[3:6])}-{''.join(only_numbers[6:8])}-{''.join(only_numbers[8:10])}"
        return unified_phone_number
    else:
        return False

@dp.message_handler(text=['Регистрация', 'Отказ'])
async def register(message: types.Message):
    await message.answer('Вы начали регистрацию')
    await message.answer_document(open("private_policy.pdf", "rb"), reply_markup=approval_kb, caption='Просим дать согласие на обработку персональных данных')


@dp.message_handler(text='Согласен(на)')
async def register(message: types.Message):
    await message.answer('Введите своё имя:', reply_markup=types.ReplyKeyboardRemove())
    await User_registration.enter_name.set()

@dp.message_handler(state=User_registration.enter_name)
async def state_enter_name(message: types.Message, state: FSMContext):
    user_name = message.text
    await state.update_data(fullname=user_name)
    await message.answer('Введите номер телефона:')
    await User_registration.enter_phone_number.set()

@dp.message_handler(state=User_registration.enter_phone_number)
async def state_enter_phone_number(message: types.Message, state: FSMContext):
    phone_number = unify_phone(message.text)
    if phone_number:
        await state.update_data(phone_number=phone_number)
        data = await state.get_data()
        data['telegram_id'] = message.from_id
        await message.answer(
            f'Имя: {data.get("fullname")}\n'
            f'Телефон: {phone_number}\n'
            f'Данные в базу:\n {data}'
        )
        await state.finish()
    else:
        await message.answer('Введен некорректный номер телефона, попробуйте еще раз')