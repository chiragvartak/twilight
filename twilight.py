"""A small Python script that gives sunrise, sunset and dusk times and also the
duration of the day"""

import urllib2
import json
import sys
from datetime import datetime, timedelta


def to_time(timestring):
    """Returns a datetime.datetime object, given a string representing time in
    the format "HH:MM:SS AM/PM", e.g. "11:23:27 PM" or "12:14:46 AM"."""
    return datetime.strptime(timestring, "%I:%M:%S %p")


def local_time(t):
    """Returns the string representing the time in the format "HH:MM:SS AM/PM";
    given a datetime.datetime object t."""
    return datetime.strftime(t, "%I:%M:%S %p")


# IIIT Hyderabad Latitude-Longitude (in degrees)
# date format: "YYYY-MM-DD"
lat = 17.4472
lng = 78.3488
timezone = "UTC+5:30"
date = "today"

# # London Latitude-Longitude (in degrees)
# lat = 36.720160
# lng = -4.420340
# timezone = "UTC+00:00"
# date = "today"

# Formatting date to be suitable for the GET request
date_suffix = ""
if date == "today":
    date_suffix = "&date=" + datetime.strftime(datetime.today(), "%Y-%m-%d")
else:
    date_suffix = "&date=" + date

# Creating the timedelta object that denotes the difference from UTC time
time_diff = ''.join(timezone.split())  # Remove all whitespace from timezone
hrs, mins = time_diff.split("UTC")[1].split(':')
hrs = int(hrs)
mins = int(mins)
td = timedelta(hours=hrs, minutes=mins)

# http://api.sunrise-sunset.org/json?lat=36.7201600&lng=-4.4203400

get_request_url = "http://api.sunrise-sunset.org/json?" + \
    "lat=" + str(lat) + "&lng=" + str(lng) + date_suffix
contents = urllib2.urlopen(get_request_url).read()
contents = json.loads(contents)

if contents['status'] == "INVALID_REQUEST":
    print "INVALID_REQUEST: Check lat and lng parameters"
    sys.exit(1)
elif contents['status'] == "INVALID_DATE":
    print "INVALID_DATE: Check data parameter"
    sys.exit(1)
elif contents['status'] == "UNKNOWN_ERROR":
    print "UNKNOWN_ERROR: Maybe try checking your Internet connection?"
    sys.exit(1)
else:  # contents['status'] == "OK"
    pass

r = contents['results']

# Print the results
print
print "Astronomical Twilight Begins:\t\t" + \
    local_time(to_time(r['astronomical_twilight_begin']) + td)
print "Nautical Twilight Begins:\t\t" + \
    local_time(to_time(r['nautical_twilight_begin']) + td)
print "Civil Twilight Begins:\t\t\t" + \
    local_time(to_time(r['civil_twilight_begin']) + td)
print "Sunrise:\t\t\t\t" + \
    local_time(to_time(r['sunrise']) + td)
print
print "Solar Noon:\t\t\t\t" + \
    local_time(to_time(r['solar_noon']) + td)
print "Day Length:\t\t\t\t" + r['day_length'] + ' hours'
print
print "Sunset:\t\t\t\t\t" + \
    local_time(to_time(r['sunset']) + td)
print "Civil Twilight Ends:\t\t\t" + \
    local_time(to_time(r['civil_twilight_end']) + td)
print "Nautical Twilight Ends:\t\t\t" + \
    local_time(to_time(r['nautical_twilight_end']) + td)
print "Astronomical Twilight Ends:\t\t" + \
    local_time(to_time(r['astronomical_twilight_end']) + td)
