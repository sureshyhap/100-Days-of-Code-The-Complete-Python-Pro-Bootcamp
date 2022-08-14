import datetime as dt
import pandas
import random
import smtplib

my_email = "sureshyhap@yahoo.com"
my_password = input("Enter your password")
now = dt.datetime.now()
this_month = now.month
this_day = now.day
birthdays = pandas.read_csv("my_birthdays.csv")
today_birthdays = birthdays[(birthdays.month == this_month) & (birthdays.day == this_day)]
for index, row in today_birthdays.iterrows():
    name = row["name"]
    email = row["email"]
    letter_choice_number = random.randint(1, 3)
    if letter_choice_number == 1:
        infile = open("letter_templates/letter_1.txt")
    elif letter_choice_number == 2:
        infile = open("letter_templates/letter_2.txt")
    elif letter_choice_number == 3:
        infile = open("letter_templates/letter_3.txt")
    contents = infile.read()
    contents = contents.replace("[NAME]", name)
    infile.close()
    with smtplib.SMTP("smtp.mail.yahoo.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs=email, msg=f"Subject:Happy Birthday!\n\n{contents}")
