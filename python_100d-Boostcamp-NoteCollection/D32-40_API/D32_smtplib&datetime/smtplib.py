# Ref.
## ServerDisconnection Error: https://www.udemy.com/course/100-days-of-code/learn/lecture/21712834#questions


import smtplib

receiver_email='@163.com'
sender_email= '@gmail.com'
sender_password = 'app token'
## What: the app password -> Change the security setting
## How: Go to account security -> 2-step verification -> Generate a new app password
## i.e. google: account setting -> Security -> App passwords (手动搜索，因为GG隐藏了）



# CREATE
# METHOD 1
# connection = smtplib.SMTP('info') ##--same with open file
# connection.close()


# METHOD 2 -- with
with smtplib.SMTP('smtp.gmail.com',587) as connection: ##create an object
## smtplib.SMPT(host, port): provider's SMTP server location -- SMTP Server info
    connection.starttls()
    ## -TLS(): Transport Layer Security --a way to secure(by encryping) connection from us to the email server
    connection.login(user=sender_email, password=sender_password)
    connection.sendmail(
        from_addr=sender_email,
        to_addrs=receiver_email,
        msg='Subject:xxx \n\n This is the body of my email'  ##Sub+Body一起
    )