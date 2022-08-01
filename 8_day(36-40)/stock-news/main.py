import requests
from twilio.rest import Client
from datetime import datetime, timedelta
import sys
sys.stdin.reconfigure(encoding='utf-8') # fix the UnicodeEncodeError because news can be written in many languages
sys.stdout.reconfigure(encoding='utf-8')

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

account_sid = "ACddae4be71f292bfaab501a697d7b9e9d"
auth_token = "1cb1353de176b3549ec450f5ea929853"
client = Client(account_sid, auth_token)

# Get the stock information

parameters_stock = {
    "function": "TIME_SERIES_INTRADAY",
    "symbol": STOCK,
    "interval": "60min",
    "apikey": "WGMFOBNM68VU25WM",
}

response = requests.get(url=STOCK_ENDPOINT, params=parameters_stock)
response.raise_for_status()
stock_price = response.json()

time_yesterday = datetime.strftime(datetime.now() - timedelta(2),'%Y-%m-%d')
time_bf_yesterday = datetime.strftime(datetime.now() - timedelta(3),'%Y-%m-%d')
time_now = datetime.now().hour

close_yesterday = float(stock_price["Time Series (60min)"][f"{time_yesterday} 20:00:00"]["4. close"])
close_bf_yesterday = float(stock_price["Time Series (60min)"][f"{time_bf_yesterday} 20:00:00"]["4. close"])

price_difference = round(abs(close_bf_yesterday - close_yesterday), 3)

percentage_difference = round(abs(close_yesterday / close_bf_yesterday)*100-100, 0)

# Get the news

parameters_com = {
    "apiKey": "3589f24e62ab40fcb4d8d3eba92efc98",
    "q": "tesla",
    "from": "2022-07-26",
    "sortBy": "publishedAt",
    }

response = requests.get(url=NEWS_ENDPOINT, params=parameters_com)
response.raise_for_status()
com_news = response.json()

text = ""
for i in range(0, 3):
    a = com_news["articles"][i]["title"]
    b = com_news["articles"][i]["url"]
    text += f"Headlines: {a}.\n"
    text += f"Link: {b}.\n"

if percentage_difference >= 0:
    message_content = f"TSLA 🔺{percentage_difference}%\n" + text
else:
    message_content = f"TSLA 🔻{percentage_difference}%\n" + text

message = client.messages \
.create(
     body=message_content,
     from_="+17432008088",
     to="+84963425495"
 )
print(message.status)