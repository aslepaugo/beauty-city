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

from timetable.utils.geo_helper import find_closest_lat_lon

def get_list():
    saloon = Saloon.objects.all()
    return saloon


if __name__ == '__main__':
    my_location = {'lat':55.72, 'lon': 37.62}
    saloons = Saloon.objects.values()  
    print(saloons)
    print(find_closest_lat_lon(my_location, saloons))