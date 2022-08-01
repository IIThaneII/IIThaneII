from datetime import datetime
from requests.auth import HTTPBasicAuth
import requests

basic = HTTPBasicAuth('Thane45638', 'niue/dahw&Bawdh')

API_KEY = "7661d3ad8b8ba*************98b4"
API_ID = "ff6***86"

headers = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY,
}

parameters = {
#  "query":input("Which exercise you did?: "),
 "gender":"male",
 "weight_kg":60,
 "height_cm":174,
 "age":19
}

# response = requests.get(url="https://trackapi.nutritionix.com/v2/natural/exercise", params=parameters, headers=headers)
# response.raise_for_status() #The url had been broken so the code cannot run.
# data = response.json()

sheety_get_post_url = "https://api.sheety.co/5187d5e2d94173524a084b3d76bb6cc9/thane'sWorkout/workouts"
sheety_put_delete_url = "https://api.sheety.co/5187d5e2d94173524a084b3d76bb6cc9/thane'sWorkout/workouts/[Object ID]"

time_now = datetime.now()

row = {
    "workout": {
        "date": time_now.strftime('%Y%m%d'),
        "time": time_now.strftime('%H:%M:%S'),
        "exercise": "Running",
        "duration": "30",
        "calories": "167",
    }
}

header = {
    "Authorization": "Basic VGhhbmU0NTYzODpu********QmF3ZGg=",
}

response = requests.get(url=sheety_get_post_url, auth=basic, headers=header)
response.raise_for_status()
data = requests.post(sheety_get_post_url, json=row) # Add data to the workouts sheet.

sheet_response = requests.post(
    sheety_get_post_url, 
    json=row, 
    auth=basic,
    headers=header
)

response = requests.get(url=sheety_get_post_url, auth=basic, headers=header)
print(response.text)