from aiogram import types
from states.global_states import Global_states
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove

from bot_custom_keyboards.dynamic_keyboards import form_2_row_keyboard
from bot_custom_keyboards.static_keyboards import get_static_keyboard
from orm_commands import *
from handlers.users.user_registration import unify_phone


slots = [
    '8:00 - 9:45',
    '10:00 - 11:45',
    '14:00 - 15:45',
    '16:00 - 17:45',
    '18:00 - 19:45'
    ] # реализовать функцию в зависимости от наполнения await state.get_data()

async def goto_masters(message: types.Message, state: FSMContext):
    current_state =  await state.get_data() 
    masters = get_master_filtered(
        salon_title=current_state.get('selected_salon'),
        service_name=current_state.get('selected_service')
        )
    await Global_states.start_select_master.set()

    await message.answer(
        'Выберите мастера',
        reply_markup=form_2_row_keyboard(masters)
    )

async def goto_services(message: types.Message, state: FSMContext):
    current_state =  await state.get_data() 
    services = get_service_filtered(salon_title=current_state.get('selected_salon'), master=current_state.get('master'))
    
    await Global_states.start_select_service.set()
    await message.answer(
        'Выберите нужную процедуру:',
        reply_markup=form_2_row_keyboard(services)
    )

async def goto_salons(message: types.Message, state: FSMContext):
    await Global_states.start_select_salon.set()

    await message.answer(
        f'Вы можете выбрать ближайший к Вам салон,\n'
        f'либо выбрать салон из списка:',
        reply_markup=await get_static_keyboard(['Ближайший салон', 'Выбрать салон из списка...']))

async def goto_salons_from_list(message: types.Message, state: FSMContext):
    current_state =  await state.get_data() 
    salons = get_salons_filtered(master=current_state.get('master'), service_name=current_state.get('selected_service'))

    await Global_states.select_salon.set()
    await message.answer(
        f'Выберите салон из списка:', reply_markup=form_2_row_keyboard(salons)
    )


async def goto_date(message: types.Message, state: FSMContext, error=None):
    
    if error is None:
        await Global_states.start_select_date.set()
        await message.answer(
            f'Введите дату в формате (dd/mm/yyyy)',
            reply_markup=ReplyKeyboardRemove()
        )
        
    else:
        await Global_states.start_select_date.set()
        await message.answer(
            error,
            reply_markup=ReplyKeyboardRemove()
        )

async def goto_slot(message: types.Message, state: FSMContext):
    await Global_states.start_select_slot.set()
    await message.answer(
        'Выберите удобное время:',
        reply_markup=form_2_row_keyboard(slots)
    )

async def goto_registration(message: types.Message, state: FSMContext):
    user = is_user_registered(message.from_id)
    
    if user:
        await state.update_data(user)
        await goto_finish_order(message, state)

    else:
        await message.answer('Вы первый раз делаете заказ, необходимо пройти регистрацию')
        document_path = os.path.join('documents', "private_policy.pdf")
        await message.answer_document(
            open(document_path, "rb"),
            reply_markup=await get_static_keyboard(['Согласен(на)', 'Отказ']),
            caption='Просим дать согласие на обработку персональных данных'
            )
        await Global_states.start_registration.set()

async def goto_finish_order(message: types.Message, state: FSMContext):
    order_data = await state.get_data()

    await Global_states.finish_order.set()
    await message.answer(
        f"Данные заказа\n"
        f"Ваше имя: {order_data.get('fullname')}\n"
        f"Телефон: {unify_phone(str(order_data.get('phone_number')))}\n"
        f"Салон: {order_data.get('selected_salon')}\n"
        f"Мастер: {order_data.get('selected_master')}\n"
        f"Услуга: {order_data.get('selected_service')}\n"
        f"Дата: {order_data.get('selected_date')}\n"
        f"Время: {order_data.get('selected_slot')}\n",
        reply_markup=await get_static_keyboard(['Подтвердить заказ', 'Начать сначала'])
    )

async def goto_start(message: types.Message, state: FSMContext):
    await Global_states.start_bot.set()
    await message.answer(
        'Спасибо, что воспользовались электронным администратором',
        reply_markup=await get_static_keyboard(['OK'])
    )
