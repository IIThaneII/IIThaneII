import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 10.863731
MY_LONG = 106.779495

my_email = "nguyennam2741@yahoo.com"
my_password = "G-5*EqpY!mLrijH"

response = requests.get(url=f"https://api.ipgeolocation.io/astronomy?apiKey=060cd24fcbb24ee1abbfa04b0a8d5e18&lat=10.863731&long=106.779495")
response.raise_for_status()
data = response.json()

sunrise = data["sunrise"].split(":")
sunset = data["sunset"].split(":")

response = requests.get(url='http://api.open-notify.org/iss-now.json')
response.raise_for_status()
data = response.json()

longtitude = float(data["iss_position"]["longitude"])
latitude = float(data["iss_position"]["latitude"])

time_now = datetime.now()
hour = time_now.hour
minute = time_now.minute

day_minute = hour*60 + minute
day_minute_sunrise = int(sunrise[0])*60 + int(sunrise[1])
day_minute_sunset = int(sunset[0])*60 + int(sunset[1])

while True:
    time.sleep(60)
    if day_minute < day_minute_sunrise or day_minute > day_minute_sunset:
        if (MY_LONG - 5 < longtitude < MY_LONG + 5) and ( MY_LAT - 5 < latitude < MY_LAT + 5):
            with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
                connection.starttls()
                connection.login(user=my_email, password=my_password)
                connection.sendmail(from_addr=my_email, to_addrs="ntguppy13@gmail.com", msg=f"Subject:ISS is going through\n\nLook up!")