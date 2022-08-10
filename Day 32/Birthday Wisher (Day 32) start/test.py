"""
import smtplib

my_email = "sureshyhap@yahoo.com"
my_password = "pparacolbumfhszd"

connection = smtplib.SMTP("smtp.mail.yahoo.com", port=587)
connection.starttls()
connection.login(user=my_email, password=my_password)
connection.sendmail(from_addr=my_email,
                    to_addrs="sureshyhap2@gmail.com",
                    msg="Subject:Hello\n\nThis is the body of the message")
connection.close()
"""



"""
import datetime as dt

now = dt.datetime.now()
print(now.month)
"""

import smtplib
import datetime as dt
import random

with open("quotes.txt", mode="r") as quotes_file:
    quotes = quotes_file.readlines()
    quote = random.choice(quotes)

my_email = "sureshyhap@yahoo.com"
my_password = "pparacolbumfhszd"

with smtplib.SMTP("smtp.mail.yahoo.com", port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    now = dt.datetime.now()
    # Wednesday
    if now.weekday() == 2:
        connection.sendmail(from_addr=my_email, to_addrs="sureshyhap2@gmail.com", msg=f"Subject:Daily Quote\n\n{quote}")
