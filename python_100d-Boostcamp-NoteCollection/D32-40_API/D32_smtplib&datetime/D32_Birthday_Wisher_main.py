##################### Extra Hard Starting Project ######################
import pandas
import random

import smtplib
import datetime as dt


def prepare_email(name):
    """3. pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv"""
    letter_no = random.randint(1,3)

    with open(f'letter_templates/letter_{letter_no}.txt') as file: ##read and repalce name
        letter = file.read()
        letter = letter.replace('[NAME]', name.strip())
        return (letter)

        # with open(f'letter_to_send/letter_to_{name}','w') as ready_file:  ##save as new file这里不需要
        #     final_letter = ready_file.write(new_letter)



# 1. Update the birthdays.csv

birthday_df = pandas.read_csv('birthdays.csv') # df_columns: name,email,year,month,day

new_row = ['Jane', 'stella33299@163.com', '1995', '4', '27']
birthday_df.loc[len(birthday_df)] = new_row ## add the row to the last
# birthday_df.to_csv('birthdays.csv', index=False) ## save to the CSV （一次就够了）
print(birthday_df) #test



# 2. Check if today matches a birthday in the birthdays.csv

# TODAY
today = dt.datetime.today() #obj
t_month = today.month #attribute
t_date =today.day

#DF dates
for index, row in birthday_df.iterrows(): # df.iterrows(index, row_content)
    df_month = int(row['month'])
    df_day = int(row['day'])

    # 3. pick letter
    if t_month == df_month and t_date == df_day:
        birthday_name = row['name']
        letter = prepare_email(birthday_name)
        print(letter) #test



# 4. Send the letter generated in step 3 to that person's email address.

receiver_email = row['email']
sender_email = 'stella33299@gmail.com'
sender_password = 'bpik kfpl mcjh eijy'

with smtplib.SMTP(host='smtp.gmail.com', port=587) as connection:
    connection.starttls()
    connection.login(user=sender_email, password=sender_password)
    connection.sendmail(from_addr=sender_email,
                        to_addrs=receiver_email,
                        msg=f'Subject: Happy Birthday {birthday_name}!!! \n\n{letter}')







# ANGELA'S METHODS: re-frame df into dict(using dict comprehension) and use tuples as dict key

from datetime import datetime
import pandas
import random
import smtplib

MY_EMAIL = "YOUR EMAIL"
MY_PASSWORD = "YOUR PASSWORD"

today = datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("YOUR EMAIL PROVIDER SMTP SERVER ADDRESS") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{contents}"
        )
