import requests
import os
import datetime as dt
API_KEY = os.environ.get('SHEETY_API_KEY')
APP_ID = os.environ.get('SHEETY_APP_ID')
NLPEX_ENDPOINT = 'https://trackapi.nutritionix.com/v2/natural/exercise'
SHEETY_SECRET = os.environ.get('SHEETY_SECRET')
SHEETY_ENDPOINT = f'https://api.sheety.co/{SHEETY_SECRET}/workoutTracking/workouts'
GENDER = 'm'
WEIGHT_KG = 50
HEIGHT_CM = 180
AGE = 17
SHEETY_AUTH_TOKEN = os.environ.get('SHEETY_AUTH_TOKEN')


headers = {
    'Content-Type': 'application/json',
    'x-app-id': APP_ID,
    'x-app-key': API_KEY
}

params = {
    "query": input("How much did you workout today? "),
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
} 

response = requests.post(url=NLPEX_ENDPOINT, json=params, headers=headers)
exercise_data = response.json()['exercises']
date_str = dt.datetime.now().strftime('%d/%m/%Y')
time_str = dt.datetime.now().strftime('%X')

for exercise in exercise_data:
    name = exercise['name'].title()
    duration = exercise['duration_min']
    calories = exercise['nf_calories']
    data = {
        'workout': {
            "date": date_str,
            "time": time_str,
            "exercise": name,
            "duration": duration,
            "calories": calories
        }
    }
    headers = {
        "Authorization": SHEETY_AUTH_TOKEN
    }
    response = requests.post(url=SHEETY_ENDPOINT, json=data, headers=headers)

