# import smtplib
#
# my_email = "gargavishka@gmail.com"
# password = "avishka3456"
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     # securing connection
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="avishka0452.cse19@chitkara.edu.in",
#         msg="Subject : Hello\n\n\n\nThis is the body of my email"
#     )

import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
days_of_week = now.weekday()
print(type(year))
print(now)

date_of_birth = dt.datetime(year=1995, month=12, day=15, hour=4)
print(date_of_birth)