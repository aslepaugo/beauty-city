from geopy.geocoders import Nominatim

def get_lat_lon(address):
    geolocator = Nominatim(user_agent='BeautyCity Test')
    location = geolocator.geocode(address)
    return (location.latitude, location.longitude)
