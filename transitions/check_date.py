from datetime import datetime, date
from aiogram.dispatcher import FSMContext


async def check_date(selected_date: str, state: FSMContext):
    now = date.today()
    error = False
    try:
        valid_date = datetime.strptime(selected_date, '%d/%m/%Y').date()
        if valid_date < now:
            raise TypeError
        
    except ValueError:
        error = "Некорректный формат, введите дату в формате dd/mm/YYYY"
    except TypeError:
        error = "Выбрана дата в прошлом, выберите другую дату"

    if error:
        return [False, error]
    else:
        return [True, valid_date]

# дописать проверку даты на занятость слотов