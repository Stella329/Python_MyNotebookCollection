import smtplib
import datetime as dt

import random


#---------SMTPLIB--------#
def send_email():
    receiver_email='xx@163.com'
    sender_email= 'xx@gmail.com'
    sender_password = 'xxxxxxx'


    with open ('quotes.txt') as quotes_file:
        line_list = [line.strip() for line in quotes_file.readlines()]
        line = random.choice(line_list)
    email_subject = 'Motivational Quote'
    email_body = 'Motivational Quote for Today:\n'+ line


    with smtplib.SMTP(host='smtp.gmail.com',port=587) as connection:
        connection.starttls()
        connection.login(user=sender_email, password=sender_password)
        connection.sendmail(from_addr=sender_email,
                            to_addrs=receiver_email,
                            msg=f'Subject:{email_subject} \n\n{email_body}')


#---------DATIME--------#
today = dt.datetime.today()
weekday = today.weekday()
if weekday == 4:
    send_email()