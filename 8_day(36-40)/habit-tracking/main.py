import requests
from datetime import datetime, timedelta

pixela_endpoint = "https://pixe.la/v1/users"
TOKEN = "iuadhwugugaw"
USER_NAME = "thane"

user_params = {
    "token": TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Code Time",
    "Unit": "minutes",
    "type": "int",
    "color": "shibafu",
}

header = {
    "X-USER-TOKEN": TOKEN,
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=header)
# print(response.text)

# graph link https://pixe.la/v1/users/thane/graphs/graph1.html

time_now = datetime.now()

node_endpoint = f"{pixela_endpoint}/thane/graphs/graph1" #/{time_now.strftime('%Y%m%d')}

node_data = {
    "date": time_now.strftime('%Y%m%d'),
    "quantity": input("How many minutes you spent on your code excercise?: "),
}

response = requests.post(url=node_endpoint, json=node_data, headers=header)
# post is to add a pixel for the first time and get is to get the information of a pixel.
# post = /v1/users/<username>/graphs/<graphID>.
# put is to update a pixel and delete is to delete it.
# put = delete = get = /v1/users/<username>/graphs/<graphID>/<yyyyMMdd>. 
print(response.text)