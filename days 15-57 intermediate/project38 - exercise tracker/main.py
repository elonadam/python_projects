import requests
import os
from datetime import datetime

URL = "https://trackapi.nutritionix.com/v2/natural/exercise" #website that does natural language processing
NUTRIT_KEY ="0f19628df221350af20fc3f1d9321c69" 
APP_ID = "d81371e0"

sheet_url = "https://api.sheety.co/84d665c812a62c08c15ad2c0f81a0f65/myWorkouts/workouts" # url for API that updates google sheets files

workout = input("\nwhat exercise you did today ?  ") # e.g run 3km and walked one hour

data = {
    "query" : workout
}

headers = {
        'x-app-id': APP_ID,
        'x-app-key': NUTRIT_KEY,
}

bearer_headers = {
    "Authorization": "Bearer workoutUpdateTable"
}

response = requests.post(url= URL,json=data, headers=headers) #get data from nutrit, e.g calories duration ...
response.raise_for_status()
plain_data = response.json()
date = datetime.date(datetime.today()).strftime("%d.%m.%Y") 
current_time = datetime.now().strftime("%H:%M:%S")

for exercise_type in plain_data['exercises']: #each different exercise inserting to a new row
    duration = exercise_type["duration_min"]
    cal = exercise_type["nf_calories"]
    exercise_type = exercise_type["name"]

    body = {
        "workout" : {
            "date" : date,
            "time" : current_time,
            "exercise" : exercise_type,
            "duration" : duration,
            "calories" : cal,
        }
    }
    send_response = requests.post(url=sheet_url,json=body,headers=bearer_headers) # sending the data to sheety API
    print(send_response.text)
