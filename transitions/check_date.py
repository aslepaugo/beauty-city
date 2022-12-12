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




# input_dates=['11/12/2022', '12/12/2022', '12/13/2022', '6zds54szdf']

# for input_date in input_dates:
#     print(check_date(input_date))