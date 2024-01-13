# Sends SMS to user phone number if its going to rain in TLV today

import requests
from twilio.rest import Client

# Running Python 3.10 doesn't work with higher bc Twilio
tlv_params = {
    "lat": 32.029302,
    "lon": 34.834780,
    "appid": "e8b3a2f2f5dd2bec5711e1b8e2aae8af",
    "cnt": 4,
}

account_sid = 'AC43d33746c61b3124371833da9f4f85b5'
auth_token = '001d564321a27b13cabe7c13a168da7b'
endpoint = "https://api.openweathermap.org/data/2.5/forecast"

response = requests.get(endpoint, params=tlv_params) #get data from api request
response.raise_for_status() # check for status errors
weather_data = response.json() # save data as json
fake_target = "write target number here" # the phone that will get the SMS
phone_number = "+14845145064" # twilio number, the sender

will_rain = False # place holder
for hour_data in weather_data["list"]: # to get all hours codes for weather
    condition_code = hour_data["weather"][0]["id"] # The API returns codes between 100-800, below 700 that a chance for rain
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token) # Twilio template to sends SMS
    message = client.messages \
        .create(
        body="It's going to rain today, remember to bring an umbrella",
        from_=phone_number,
        to=fake_target
    )
print(message.status) # if queue printed, the message got printed
