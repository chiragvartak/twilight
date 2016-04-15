
import googlemaps
import json

# Import Google Maps API key from data.py in parent folder
import sys
import os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from data import MY_GOOGLE_API_KEY

MY_API_KEY = MY_GOOGLE_API_KEY

def getlatlng(place, API_KEY=MY_API_KEY):
    """Returns the latitude and longitude of 'place'. You need to provide a
    Google Maps API key in as 'API_KEY'."""

    gmaps = googlemaps.Client(key=API_KEY)
    geocode_result = gmaps.geocode(place)
    lat1 = geocode_result[0]['geometry']['viewport']['northeast']['lat']
    lat2 = geocode_result[0]['geometry']['viewport']['southwest']['lat']
    lng1 = geocode_result[0]['geometry']['viewport']['northeast']['lng']
    lng2 = geocode_result[0]['geometry']['viewport']['southwest']['lng']
    lat = lat1 + (lat2 - lat1) / 2
    lng = lng1 + (lng2 - lng1) / 2
    return (lat, lng)
