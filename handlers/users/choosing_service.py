from aiogram import types
from loader import dp
from custom_keyboards.dynamic_keyboards import form_2_row_keyboard

# тестовые данные
services = ['Парикмахерская', 'Маникюр', 'Педикюр'] 

    
@dp.message_handler(text='На услугу...')
async def command_inline(message: types.Message):
    await message.answer('Выберите нужную процедуру:', reply_markup=form_2_row_keyboard(services))
