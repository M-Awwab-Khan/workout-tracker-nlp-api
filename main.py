import requests
API_KEY = 'dec357edc5b3bbc7985cbb7c1ee9fa32'
APP_ID = 'dc9070c6'
NLPEX_ENDPOINT = 'https://trackapi.nutritionix.com/v2/natural/exercise'
SHEETY_SECRET = '529ce7c9efde4081a07dcb7b5b9da419'
SHEETY_ENDPOINT = f'https://api.sheety.co/{SHEETY_SECRET}/workoutTracking/workouts'

headers = {
    'Content-Type': 'application/json',
    'x-app-id': APP_ID,
    'x-app-key': API_KEY
}

params = {
    "query": input("How much did you workout today? ")
} 

response = requests.post(url=NLPEX_ENDPOINT, json=params, headers=headers)
exercise_data = response.json()

