"""
import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = response.json()
print(data)
longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

iss_position = (longitude, latitude)
print(iss_position)
"""

import requests
import datetime as dt

LATITUDE = 40.715160,
LONGITUDE = -73.760270

parameters = {
    "lat" : LATITUDE,
    "lng" : LONGITUDE,
    "formatted" : 0
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

data = response.json()
sunrise_ = data["results"]["sunrise"]
sunset_ = data["results"]["sunset"]

print(sunrise_)
print(sunset_)

sunrise = sunrise_.split("T")
sunrise_date = sunrise[0].split("-")
sunrise_time = sunrise[1].split(":")
sunset = sunset_.split("T")
sunset_date = sunset[0].split("-")
sunset_time = sunset[1].split(":")

print(sunrise_date)
print(sunrise_time)
print()
print(sunset_date)
print(sunset_time)

now_ = dt.datetime.now()
now = str(now_).split(" ")
now_date = now[0].split("-")
now_time = now[1].split(":")

print()
print(now_date)
print(now_time)