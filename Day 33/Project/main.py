import requests
import math
import datetime as dt
import smtplib
import time

MY_LAT = 40.715160
MY_LONG = -73.760269

sun_parameters = {
    "lat" : MY_LAT,
    "lng" : MY_LONG,
    "formatted" : 0
}

response_sun = requests.get(url="https://api.sunrise-sunset.org/json", params=sun_parameters)
response_sun.raise_for_status()
data_sun = response_sun.json()
sunrise_hour = int(data_sun["results"]["sunrise"].split("T")[1].split(":")[0])
sunset_hour = int(data_sun["results"]["sunset"].split("T")[1].split(":")[0])

username = input("Enter your email: ")
password = input("Enter your password: ")

while True:
    time.sleep(1)
    response_satellite = requests.get(url="http://api.open-notify.org/iss-now.json")
    response_satellite.raise_for_status()
    data_satellite = response_satellite.json()
    longitude_satellite = float(data_satellite["iss_position"]["longitude"])
    latitude_satellite = float(data_satellite["iss_position"]["latitude"])
    # If ISS Satellite is overhead
    if math.fabs(MY_LAT - latitude_satellite) < 5 and math.fabs(MY_LONG - longitude_satellite) < 5:
        now_time = dt.datetime.now().hour
        # If it is night time
        if now_time > sunset_hour or now_time < sunrise_hour:
            with smtplib.SMTP("smtp.mail.yahoo.com", port=587) as connection:
                connection.starttls()
                connection.login(user=username, password=password)
                connection.sendmail(from_addr=username, to_addrs="sureshyhap@gmail.com",
                                    msg="Subject:Satellite Notification\n\nLook up!")
                print("Email Sent!")
        else:
            print("It's above but you can't see it since it's not night!")
    else:
        print("Not yet!")