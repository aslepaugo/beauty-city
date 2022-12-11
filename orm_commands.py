import os
import django
from beauty_city.settings import *

os.environ['DJANGO_SETTINGS_MODULE'] = 'bot_settings'
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
django.setup()


from timetable.models import (
    User,
    Master,
    Saloon,
    Service
)

from timetable.utils.geo_helper import find_closest_lat_lon

def is_user_registration(): #реализовать функцию запроса данных пользователя
    # есть регистрация
    return {'telegram_id': 55555555, 'fullname': 'Роман', 'phone_number':'9876543211'}
    # нет регистрации
    # return False

def get_all_salons():
    return [salon.title for salon in Saloon.objects.all()] 


def get_nearest_salon(user_coordinates):
    if len(user_coordinates) != 2:
        return Saloon.objects.first().title
    else:
        saloons = Saloon.objects.values()
        closest_salon = find_closest_lat_lon(user_coordinates, saloons)
        return closest_salon


def get_list():
    saloon = Saloon.objects.all()
    return saloon


if __name__ == '__main__':
    my_location = {'lat':55.72, 'lon': 37.62}
    saloons = Saloon.objects.values()  
    print(saloons)
    print(find_closest_lat_lon(my_location, saloons))