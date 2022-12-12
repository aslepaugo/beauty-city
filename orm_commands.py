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
    Service,
    ServiceType
)


from timetable.utils.geo_helper import find_closest_lat_lon

def is_user_registered(telegram_id):
    user = {}
    try:
        user_object = User.objects.get(telegram_id=telegram_id)
        if user_object:
            user = {
                'telegram_id': user_object.telegram_id,
                'fullname': user_object.fullname,
                'phone_number': user_object.phone_number
            }
        
    except User.DoesNotExist:
        print('нет пользователя')

    if user:
        return user
    else:
        return False
        

def delete_all_User():
    User.objects.all().delete()


def get_all_salons():
    return [salon.title for salon in Saloon.objects.all()] 

def get_all_services():
    return [f'{service.name} {str(service.price)} руб.' for service in ServiceType.objects.all()]

def get_all_masters():
    return [master.fullname for master in Master.objects.all()]


def get_nearest_salon(user_coordinates):
    if len(user_coordinates) != 2:
        return Saloon.objects.first().title
    else:
        saloons = Saloon.objects.values()
        closest_salon = find_closest_lat_lon(user_coordinates, saloons)
        return closest_salon


if __name__ == '__main__':
    my_location = {'lat':55.72, 'lon': 37.62}
    saloons = Saloon.objects.values()  
    print(saloons)
    print(find_closest_lat_lon(my_location, saloons))
