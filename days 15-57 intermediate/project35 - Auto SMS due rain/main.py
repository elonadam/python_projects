import os

import requests
from twilio.rest import Client

# running python 3.10 dont work with higher bc twilio
tlv_params = {
    "lat": 32.029302,
    "lon": 34.834780,
    "appid": "e8b3a2f2f5dd2bec5711e1b8e2aae8af",
    "cnt": 4,
}

# twilio recovery code Y6JQGX3UTMUG9S9DB9UV1YS5

account_sid = 'AC43d33746c61b3124371833da9f4f85b5'
auth_token = '001d564321a27b13cabe7c13a168da7b'


endpoint = "https://api.openweathermap.org/data/2.5/forecast"

response = requests.get(endpoint, params=tlv_params)
response.raise_for_status()
weather_data = response.json()
fake_target = "write target number here"
phone_number = "+14845145064"
# print(weather_data["list"][0]["weather"][0]["id"])

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="It's goiong to rain today, remember to bring an umbrella",
        from_=phone_number,
        to=fake_target
    )
print(message.status)
