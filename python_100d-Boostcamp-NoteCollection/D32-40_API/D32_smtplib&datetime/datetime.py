import datetime as dt #<MODUEL>
# from datetime<MODUEL> import datetime<CLASS>


# TAP INTO CURRENT DATETIME

now = dt.datetime.now() ##obj
year = now.year ##Atribute; type: int
month = now.month
hour = now.hour
    ## dt.datetime() --> obj.
    ## dt.datetime.now() # 2024-04-26 20:44:19.168236
    ## now's type: <'datetime.datetime'> --> obj
day_of_week = now.weekday() ##Method; 从0开始: 星期一


#CREATE YOUR OWN DATETIME OBJ

date_of_birth = dt.datetime(year =1997, month=3, day=29, hour=13)  ##->obj.
## output: 1997-03-29 13:00:00



# -----------------2 CLASSES
# datetime.now() -- datetime Class
timenow = dt.datetime.now() ##output:2024-06-05 15:33:36.313356; type: <class 'datetime.datetime'>
year = timenow.year  ##output 2024; type: int.
today_tuple = (timenow.month, timenow.day)


# date.today() -- date Class
today = dt.date.today() ##output: 2024-06-05; type: <class 'datetime.date'>
weekday = today.weekday()

# TODO output: today's date in yyyymmdd
## METHOD 1: str.replace(old,new,count)
today_formatted = str(today).replace('-','') ##output: 20240605

## METHOD 2: strftime
## more info: https://www.w3schools.com/python/python_datetime.asp
today2 = dt.datetime(year=2024, month=6, day=5)
today_formatted2 = today2.strftime('%Y-%m-%d') ##output: 2024-06-05


# YESTERDAY

from datetime import date
from datetime import timedelta

today = date.today() ## 2024-06-05
yesterday = today - timedelta(day=1)
day_before_yesterday = today - timedelta(day=2)


