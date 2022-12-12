from aiogram import types
from custom_keyboards.dynamic_keyboards import form_2_row_keyboard
from custom_keyboards.static_keyboards import *
from states.global_states import Global
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove
from orm_commands import is_user_registered
from handlers.users.user_registration import unify_phone


salons = ['Салон1','Салон2', 'Салон3', 'Салон4', 'Салон5']  # реализовать функцию в зависимости от наполнения await state.get_data()
services = ['Парикмахерская', 'Маникюр', 'Педикюр'] # реализовать функцию в зависимости от наполнения await state.get_data()
masters = ['мастер1', 'Мастер2', 'мастер3', 'Мастер4', 'Мастер5', 'Мастер6', 'Мастер7', 'Мастер8']# реализовать функцию в зависимости от наполнения await state.get_data()
slots = [
    '8:00 - 9:45',
    '10:00 - 11:45',
    '14:00 - 15:45',
    '16:00 - 17:45',
    '18:00 - 19:45'
    ] # реализовать функцию в зависимости от наполнения await state.get_data()

async def goto_masters(message: types.Message, state: FSMContext):
    await message.answer(
        f'DATA для тестирования {await state.get_data()}'
    )
    await Global.start_select_master.set()
    await message.answer(
        'Выберите мастера',
        reply_markup=form_2_row_keyboard(masters)
    )

async def goto_services(message: types.Message, state: FSMContext):
    await message.answer(
        f'DATA для тестирования {await state.get_data()}'
    )
    await message.answer(
        'Выберите нужную процедуру:',
        reply_markup=form_2_row_keyboard(services)
    )
    await Global.start_select_service.set()

async def goto_salons(message: types.Message, state: FSMContext):
    await message.answer(
        f'DATA для тестирования {await state.get_data()}'
    )
    await message.answer(
        f'Вы можете выбрать ближайший к Вам салон,\n'
        f'либо выбрать салон из списка:', reply_markup=st3_kb_menu)
    await Global.start_select_salon.set()

async def goto_date(message: types.Message, state: FSMContext):
    await message.answer(
        f'DATA для тестирования {await state.get_data()}'
    )
    await message.answer(
        f'Введите дату',
        reply_markup=ReplyKeyboardRemove()
    )
    await Global.start_select_date.set()

async def goto_slot(message: types.Message, state: FSMContext):
    await message.answer(
        f'DATA для тестирования {await state.get_data()}'
    )
    await message.answer(
        'Выберите удобное время:',
        reply_markup=form_2_row_keyboard(slots)
    )
    await Global.start_select_slot.set()

async def goto_registration(message: types.Message, state: FSMContext):
    user = is_user_registered(message.from_id)
    
    if user:
        await state.update_data(user)
        await goto_finish_order(message, state)

    else:
        await message.answer(
            f'DATA для тестирования {await state.get_data()}'
        )
        await message.answer('Вы первый раз делаете заказ, необходимо пройти регистрацию')
        await message.answer_document(
            open("private_policy.pdf", "rb"),
            reply_markup=approval_kb,
            caption='Просим дать согласие на обработку персональных данных'
            )
        await Global.start_registration.set()

async def goto_finish_order(message: types.Message, state: FSMContext):
    order_data = await state.get_data()
    await message.answer(
        f'DATA для тестирования {await state.get_data()}'
    )
    await message.answer(
        f"Данные заказа\n"
        f"Ваше имя: {order_data.get('fullname')}\n"
        f"Телефон: {unify_phone(str(order_data.get('phone_number')))}\n"
        f"Салон: {order_data.get('selected_salon')}\n"
        f"Мастер: {order_data.get('selected_master')}\n"
        f"Услуга: {order_data.get('selected_service')}\n"
        f"Дата: {order_data.get('selected_date')}\n"
        f"Время: {order_data.get('selected_slot')}\n",
        reply_markup=finish_order_kb
    )
    await Global.finish_order.set()


async def goto_start(message: types.Message, state: FSMContext):
    await Global.start_bot.set()
    await message.answer(
        'Спасибо, что воспользовались электронным администратором',
        reply_markup=ok_button
    )

