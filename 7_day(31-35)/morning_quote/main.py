import datetime as dt
import smtplib
import random

my_email = "nguyennam2741@yahoo.com"
my_password = "G-5*EqpY!mLrijH"

with open("/Users/ez/OneDrive/Máy tính/codeprojects/PYTHON/100_days_of_Py/7_day(31-35)/morning_quote/quotes.txt", mode="r") as quotes:
    quote = quotes.readlines()
    m_quote = random.choice(quote) 

now = dt.datetime.now()
day_of_week = now.weekday
if day_of_week == "Monday":
    with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs="ntguppy13@gmail.com", msg=f"Subject:Monday motivation\n\n{m_quote}")