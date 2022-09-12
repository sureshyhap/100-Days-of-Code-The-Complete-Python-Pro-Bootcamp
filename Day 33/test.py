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
sunrise_time = data["results"]["sunrise"]
sunset_time = data["results"]["sunset"]

print(sunrise_time)
print(sunset_time)

now = dt.datetime.now()