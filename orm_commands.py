import os
import django
from beauty_city.settings import *

os.environ['DJANGO_SETTINGS_MODULE'] = 'bot_settings'
django.setup()


from timetable.models import (
    User,
    Master,
    Saloon,
    Service
)


def get_list():
    saloon = Saloon.objects.all()
    return saloon


if __name__ == '__main__':
    print(get_list())
