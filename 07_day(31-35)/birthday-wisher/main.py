import datetime as dt
import smtplib
import random
import pandas

my_email = "nguyennam2741@yahoo.com"
my_password = "G-5*EqpY!mLrijH"

birthday = pandas.read_csv("/Users/ez/OneDrive/Máy tính/codeprojects/PYTHON/100_days_of_Py/7_day(31-35)/birthday-wisher/birthdays.csv")

now = dt.datetime.now()
birth_day = birthday[birthday.day == now.day].to_dict('records') #('records') is to remove the index from the dictionary
birth_month = birthday[birthday.month == now.month].to_dict('records')

# Check if today matches a birthday in the birthdays.csv
if birth_day == birth_month:
    for i in range(0, len(birth_day)): # still works if people have the same birthday
        a = random.randint(1, 3)
        with open(f"/Users/ez/OneDrive/Máy tính/codeprojects/PYTHON/100_days_of_Py/7_day(31-35)/birthday-wisher/letter_templates/letter_{a}.txt", mode="r") as letter:
            # pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
            birthday_letter = letter.read().replace("[NAME]", f"{birth_day[i]['name']}")
            print(birthday_letter)\
            # Send the letter generated to that person's email address.
            with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
                connection.starttls()
                connection.login(user=my_email, password=my_password)
                connection.sendmail(from_addr=my_email, to_addrs=birth_day[i]['email'], msg=birthday_letter)