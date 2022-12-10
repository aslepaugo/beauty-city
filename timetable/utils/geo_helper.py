from geopy.geocoders import Nominatim
from math import asin, cos, radians, sin, sqrt


RADIUS_EARTH = 6378

def get_lat_lon(address):
    geolocator = Nominatim(user_agent='BeautyCity Test')
    location = geolocator.geocode(address)
    return (location.latitude, location.longitude)


def get_distance_between_lat_lon(*args):
    lat1, lat2, long1, long2 = map(radians, args)
    dist_lats = abs(lat2 - lat1) 
    dist_longs = abs(long2 - long1) 
    a = sin(dist_lats/2)**2 + cos(lat1) * cos(lat2) * sin(dist_longs/2)**2
    c = asin(sqrt(a)) * 2
    return c * RADIUS_EARTH


def find_closest_lat_lon(location, places):
    try:
        return min(places, key=lambda place: get_distance_between_lat_lon(location['lat'],place['lat'],location['lon'],place['lon']))
    except TypeError:
        print('Not a list or not a number.')
