from bs4 import BeautifulSoup
import requests
import smtplib

my_email = "nguyennam2741@yahoo.com"
my_password = "your password"

URL = f"https://www.amazon.com/Kindle-Paperwhite-Essentials-Bundle-including/dp/B09FBXR5Q8/ref=sr_1_3?crid=1KAVVINZLWW7F&keywords=kindle&qid=1659596710&sprefix=kindl%2Caps%2C713&sr=8-3"

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
    "Accept-Language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
}

response = requests.get(URL, headers=header)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")#.encode("utf-8")
price = soup.find(name="span", class_="a-offscreen").getText().split("$")
if float(price[1]) < 150:
    with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs="ntguppy13@gmail.com", msg="HOT HOT\n\nThe price had dropped below your buy price!")
