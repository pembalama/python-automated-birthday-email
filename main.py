import datetime as dt
import smtplib
import random
import pandas
import os

month = dt.datetime.now().month
day = dt.datetime.now().day

data = pandas.read_csv("birthdays.csv")
birthdays = data.to_dict(orient="records")

MY_EMAIL = "test@gmail.com"
MY_PASSWORD = "abcdtest"

for birthday in birthdays:
    if birthday["month"] == month and birthday["day"] == day:
        random_email = random.choice(os.listdir("letter_templates"))
        with open(f"letter_templates/{random_email}") as my_file:
            email_to_send = my_file.read().replace("[NAME]", birthday["name"])

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=birthday["email"],
                                msg=f"Subject:Happy Birthday!\n\n{email_to_send}")





