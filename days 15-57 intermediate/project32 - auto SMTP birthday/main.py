import pandas
import smtplib
import datetime as dt
from random import randint

gmail_smtp = "smtp.gmail.com"
outlook_smtp = "smtp-mail.outlook.com"
my_email = "beeragain3@gmail.com" # change to your email to send from
my_password = "icpnrfjkarctgedo " # change to your app-password you got from your account 
now = dt.datetime.now()
today = now.day, now.month  # dd,mm tuple

birthday_data = pandas.read_csv("birthdays.csv")
bd_dict = {(row["day"], row["month"]): row for (index, row) in birthday_data.iterrows()}
print(bd_dict,"\n")

if today in bd_dict:
    target_email = bd_dict[today]["email"]
    with open(f"./letter_templates/letter_{randint(1, 3)}.txt") as file:
        templet = file.read()
        bd_card = templet.replace("[NAME]", bd_dict[today]["name"])

        with smtplib.SMTP(gmail_smtp) as connection: #if you wish to send from outlook or something else change the smtp format
            connection.starttls()
            connection.login(my_email,my_password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=target_email,
                                msg=f"Subject:Happy Birthday!\n\n{bd_card}")
