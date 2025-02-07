# NUTRITIONIX API PERSONAL: https://developer.nutritionix.com/admin/access_details
# API GUIDE: https://docx.syndigo.com/developers/docs/nutritionix-api-guide

# GG spreadsheet: SHEETY API PERSONAL: https://dashboard.sheety.co/
# API GUIDE: 1. https://funkytwig.com/2021/11/18/beginer-guide-sheety-python-api-update-goodle-sheets/
# 2. https://sheety.co/docs/authentication.html

import requests
import datetime as dt
import os


#--------NUTRITIONIX API: get calories

APPLICATION_ID= os.environ['APPLICATION_ID']
API_KEY = os.environ['API_KEY']
my_query = input('Tell me which exercises you did: ')

nutri_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'
API_headers = {
    'x-app-id': APPLICATION_ID,
    'x-app-key': API_KEY,
}
parameters = {
    'query': my_query,
    'weight_kg': 50,
    'height_cm': 160,
    'age':29
}

nutritionix_response = requests.post(url=nutri_endpoint, json=parameters, headers=API_headers)
print(nutritionix_response.status_code)

data = nutritionix_response.json()
print(data)


#--------SHEETY API: adding a new row
today_dt = dt.date.today()  ## 2024-06-12
today = today_dt.strftime('%d/%m/%Y') ##12/06/2024
time = dt.datetime.now().strftime('%X') ## 12:45:45


sheety_endpoint = os.environ['SHEETY_ENDPOINT'] ## 登陆后台查看，格式https://api.sheety.co/username/projectName/emails
sheety_params = {
    'workout': { ##The json code for the sheety payload, the root property by default is "workout", not "workouts", even though the endpoint is named workouts.
        'date': today,
        'time': time,
        'exercise': data["exercises"][0]['name'].title(),
        'duration': data["exercises"][0]['duration_min'],
        'calories': data["exercises"][0]['nf_calories'],
    }
}
# ## METHEOD 2: for loop
# for exercise in result["exercises"]:
#     sheet_inputs = {
#         "workout": {
#             "date": today_date,
#             "time": now_time,
#             "exercise": exercise["name"].title(),
#             "duration": exercise["duration_min"],
#             "calories": exercise["nf_calories"]
#         }
#     }

# WITHOUT TOKEN
# sheety_response = requests.post(url=sheety_endpoint,json=sheety_params)
# print(sheety_response.status_code)
# print(sheety_response.text)


# Basic Autentication: TOKEN
TOKEN = os.environ['TOKEN']
header = {'Authorization': f'Bearer {TOKEN}'}
sheety_response = requests.post(url=sheety_endpoint, headers=header, json=sheety_params)
print(sheety_response.status_code)


