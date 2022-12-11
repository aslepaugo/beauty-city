from aiogram import types
from custom_keyboards.dynamic_keyboards import form_2_row_keyboard
from custom_keyboards.static_keyboards import *
from states.global_states import Global
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove


nearest_salon = {'title': 'nсалон1', 'address': 'nАдрес 1'}
salons = ['Салон1','Салон2', 'Салон3', 'Салон4', 'Салон5']
services = ['Парикмахерская', 'Маникюр', 'Педикюр'] 
masters = ['мастер1', 'Мастер2', 'мастер3', 'Мастер4', 'Мастер5', 'Мастер6', 'Мастер7', 'Мастер8']

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
        f'Пока все', reply_markup=ReplyKeyboardRemove()
    )
    await state.finish()
    pass # дописать
