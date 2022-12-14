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
    ServiceType,
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
        pass

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


def get_master_filtered(salon_title=None, service_name=None):
    if not service_name and not salon_title:
        return [master.fullname for master in Master.objects.all()]
    elif not service_name and salon_title:
        return [master.fullname for master in Master.objects.filter(saloon__title__contains=salon_title).distinct()]
    elif service_name and not salon_title:
        return [master.fullname for master in Master.objects.filter(speciality__name__contains=service_name).distinct()]
    elif service_name and salon_title:
        return [master.fullname for master in Master.objects.filter(speciality__name__contains=service_name, saloon__title__contains=salon_title).distinct()]


def get_service_filtered(salon_title=None, master=None):
    if not salon_title and not master:
        return [master.speciality.name for master in Master.objects.all()]
    elif not salon_title and master:
        return [master.speciality.name for master in Master.objects.filter(fullname__contains=master).distinct()]
    elif salon_title and not master:
        return [master.speciality.name for master in Master.objects.filter(saloon__title__contains=salon_title).distinct()]
    elif salon_title and master:
        return [master.speciality.name for master in Master.objects.filter(saloon__title__contains=salon_title, fullname__contains=master).distinct()]


def get_salons_filtered(service_name=None, master=None):
    print(service_name, master)
    if not service_name and not master:
        return [salon.title for salon in Saloon.objects.all()] 
    elif not service_name and master:
        return [salon.title for salon in Saloon.objects.filter(master__name__contains=master).distinct()] 
    elif service_name and not master:
        return [salon.title for salon in Saloon.objects.filter(master__speciality__name__contains=service_name).distinct()] 
    elif service_name and master:
        return [salon.title for salon in Saloon.objects.filter(master__name__contains=master, master__speciality__name__contains=service_name).distinct()]


def get_nearest_salon(user_coordinates):
    if len(user_coordinates) != 2:
        return Saloon.objects.first().title
    else:
        saloons = Saloon.objects.values()
        closest_salon = find_closest_lat_lon(user_coordinates, saloons)
        return closest_salon


if __name__ == '__main__':
    get_all_services()
