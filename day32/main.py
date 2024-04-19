import smtplib
import datetime as dt
import random
import pandas

my_email = "jnitu7227@gmail.com"
password = "zdherbajjbfxoypr"

today = dt.datetime.now().month, dt.datetime.now().day

data = pandas.read_csv("//santanu/PycpyhomethonProjectharmProjects//day32/birthdays.csv")
birthdays_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}
if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    file_path = f"/home/santanu/PycharmProjects/pythonProject/day32/letter/letter_{random.randint(1,3)}.txt"
    with open (file_path) as letter_file:
        content = letter_file.read()
        contents = content.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,to_addrs= "cushantanu@gmail.com",
                            msg=f"subject:Happy Birthday!\n\n{contents}")
