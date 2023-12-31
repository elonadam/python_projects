# this program sending email when the 2 conditions are true:
# 1. the ISS is passing in the sky near the location of the user
# 2. its night time therefore the ISS is visible 


import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 32.083459  # latitude
MY_LONG = 34.796472  # longitude
gmail_smtp = "smtp.gmail.com"
my_email = "beeragain3@gmail.com"
my_password = "icpnrfjkarctgedo"
target_email = "Janecustom24@gmail.com"

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
    "tzId": "Asia/Tel_Aviv"
}


def iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json", params=parameters)
    response.raise_for_status()
    iss_data = response.json()

    iss_latitude = float(iss_data["iss_position"]["latitude"])
    iss_longitude = float(iss_data["iss_position"]["longitude"])

    # if my position is within +5 or -5 degrees of the ISS position.
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True
    return False


def nighttime():
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour
    if sunset <= time_now or time_now <= sunrise:
        return True


def iss_in_the_sky():
    with smtplib.SMTP(gmail_smtp) as connection:
        connection.starttls()
        connection.login(my_email, my_password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=target_email,
                            msg=f"Subject:ISS in the sky!\n\nLook up ! the ISS is right over your head")
        print("sent email")


while True:
    time.sleep()
    if nighttime() and iss_overhead():
        iss_in_the_sky()

