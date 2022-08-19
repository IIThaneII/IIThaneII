import requests
from twilio.rest import Client

parameters = {
    "key": "9352fbbf5af64df5b0e162302222807",
    "q": "125.212.247.135",
    "days": 2,
}

account_sid = "ACddae4be71f292bfaab501a697d7b9e9d"
auth_token = "f0d7e790244e92aa132321d5c6cd2b39"
client = Client(account_sid, auth_token)

response = requests.get(url="https://api.weatherapi.com/v1/forecast.json", params=parameters)
response.raise_for_status()
data = response.json()
weather_slice = data["forecast"]["forecastday"][1]["hour"][:25]
i = -1
for hour in weather_slice:
    i += 1
    if int(hour["chance_of_rain"]) > 50:
        message = client.messages \
    .create(
         body=f"It may rain at: {i}h",
         from_="+17432008088",
         to="+84963425495"
     )
        print(message.status)