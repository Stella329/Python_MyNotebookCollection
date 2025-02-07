# ABOUT API
# API endpoint: a url, the address where the API is (can be found)
# API: like a bank teller saying 'what can I help you?'
# API request: get and request
# API parameter: a way to allow inputs in your API requests, to get a specific piece of info instead of broad stroke answers -- NOT ALL API has parameters


#-------------NOTES AHEAD----------------
# HOW TO USE API: go to the endpint (url) -> get the responded data back

# import requests
response = request.get(url= '') #-- method: get data from the endpoint; print: <Responses [200]>
#
# # by printing the followings to get the actual codes:
response.status_code #--i.e.
# # if respond error codes:
if response.status_code == 404
    raise Exception ("That resource does not exist.")

# # using requests module: 不用手动列举所有error情况和raise all errors; This is equivilant to ==
response.rasie_for_statuse() #-- raise an HTTPError in HTTP returns an unsuccessful status codes
#
# # get hold of the actual data in api url: data = response.json()['key1']['key2']:
data_position = response.json()['iss_position']




#--------------------ISS PROJECT------------------------#
# sunrise&sunset API: https://sunrise-sunset.org/api
# ISS API: http://open-notify.org/Open-Notify-API/ISS-Location-Now/
# find lat and long: https://www.latlong.net/Show-Latitude-Longitude.html


import requests
import datetime as df  # OR from datetime import datetime
import smtplib
import time

MY_LAT = 31.230391 # Sh
MY_LONG = 121.473701

#----------------COMPARE
#If the ISS is close to my current position: Your position is within +5 or -5 degrees of the ISS position.
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

#--------------ISS API: International Space Station Current Location-----------
def is_ISS_overhead():

    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()  ## will raise the request status code if error
    data = response.json()  ## get the actual data

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Your position is within +5 or -5 degrees of the ISS position.
    if abs(iss_latitude - MY_LAT) <= 5 and abs(iss_longitude - MY_LONG) <= 5:
        return True


#--------------Sunset and sunrise times API-----------

def is_nighttime():
    time_now = df.datetime.now() ##print 2024-05-10 17:09:22.842652

    parameters = {
        'lat': MY_LAT,
        'lng': MY_LONG,
        'formatted': 0, ## 1=12小时制（default），0=24小时制
    }

    respond = requests.get('https://api.sunrise-sunset.org/json', params=parameters) ## parameters: lat and lng are required
    respond.raise_for_status()
    data = respond.json()   ##if 0, print: {'results': {'sunrise': '2024-05-09T21:00:16+00:00', 'sunset': '2024-05-10T10:40:45+00:00',...}}

    sunrise = data['results']['sunrise']   ## print: 2024-05-09T21:00:16+00:00
    sunrise_hour = int(sunrise.split('T')[1].split(':')[0])   ## print: 21

    sunset = data['results']['sunset']
    sunset_hour = int(sunset.split('T')[1].split(':')[0])

    if sunrise_hour <= time_now.hour <= sunset_hour:
        return True



#------------Run every 60s: checnk and send the email
while True:
    if is_ISS_overhead() and is_nighttime():

        time.sleep(60)  ##每60s 运行一次

        receiver_email = 'xx@163.com'
        sender_email = 'xx@gmail.com'
        sender_password = 'xxxxxxx'
        email_subject = 'LOOK UP IN THE SKY'
        email_body = 'Look up!! The ISS is above you in the sky!! '

        connection = smtplib.SMTP(host='smtp.gmail.com', port=587)
        connection.starttls()
        connection.login(user=sender_email, password=sender_password)
        connection.sendmail(from_addr=sender_email,
                            to_addrs=receiver_email,
                            msg=f'Subject:{email_subject} \n\n{email_body}')


