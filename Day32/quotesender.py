import smtplib
import datetime as dt
import random

my_email = "gargavishka@gmail.com"
my_password = "abc123"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 1:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="avishka0452.cse19@chitkara.edu.in",
            msg=f"Subject: Monday Motivation \n\n{quote}"
        )