# 5d weather forecast API: https://openweathermap.org/forecast5
#Twilio API (send SMS): https://www.twilio.com/docs/messaging/quickstart/python

import requests
import telegram
import asyncio


ENDPOINT = 'https://api.openweathermap.org/data/2.5/forecast'
API_KEY = 'efa96b0cd19d37ab04f441396d5b0dec'
Weining_Road = (31.216347, 121.382646)
Petropavlovsk_Kamchatsky = (53.065319, 158.625732)

LOC = Petropavlovsk_Kamchatsky
LOC_NAME = 'Petropavlovsk_Kamchatsky'



# TODO OWM API
parameters = {
    'lat': LOC[0],
    'lon': LOC[1],
    'appid': API_KEY,
    'cnt': 4, ##tailor to a number of timestamps 4 == 12 hours (3hrs per timestamps)
}

response = requests.get(url=ENDPOINT, params=parameters)
response.raise_for_status()
# print(response.status_code) #test

forecast_data = response.json()
# print(forecast_data) #test


# TODO if weather condition codes <= 700: Bring an Umbrella; weather window = next 12hrs
will_rain = False
rain_data_list = []
num = 0
for hour_data_dict in forecast_data['list']:
    weather = hour_data_dict['weather']
    time = hour_data_dict['dt_txt']

    weather_description_list =[]
    for sub_weather_dict in weather: ##防止出现多于一种的天气
        weather_ID = int(sub_weather_dict['id'])
        weather_description = sub_weather_dict['description']
        weather_description_list.append((weather_description))
    weather_reformat= ''.join([(str(describes)) for describes in weather_description_list]) # ''.join([list_comprehension])

    if weather_ID <= 700:
        will_rain = True
        rain_day = {'time': time, 'weather_reformat': weather_reformat}
        rain_data_list.append(rain_day)


# print(rain_data_list) #test

if will_rain == True:
    final_message = ''
    for pair in rain_data_list:
        message = f'At {pair['time']}, Weather will be {pair['weather_reformat']}. \n'
        final_message += message

    bot_message =  f'My location is {LOC_NAME}\n\n{final_message}\n🌂Oh Dear~ Remember to bring an Umbrella🌂 ~💖'



# TODO TELEGRAM BOT API using Python (国内网需要全局：tun mode +service mode）

bot_token= '7177385584:AAFufEwZt8mAPnxrKg2nIDZnTSMWKtCXKhU'
chat_id = '1387810108'

# METHOD 0 with API (TG BOT API):
# TG_endpoint = f'https://api.telegram.org/bot{bot_token}/METHOD_NAME'
def telegram_bot_sendtext(message, token,id):
    token = token
    parameters = {
        'chat_id': id,
        'text': message,
    }
    TG_endpoint = f'https://api.telegram.org/bot{token}/sendMessage'

    TG_response = requests.get(url=TG_endpoint, params=parameters)
    print(TG_response.status_code)
    TG_response.raise_for_status()

telegram_bot_sendtext(message=bot_message, token=bot_token, id=chat_id)


# #METHOD 1 with TELEGRAM moduel:
# bot = telegram.Bot(token=bot_token)
# asyncio.run(bot.send_message(chat_id=chat_id, text=bot_message))

# #METHOD 2 with TELEGRAM moduel:
# import telegram
# import asyncio

# async def send_telegram_message(bot_token, chat_id, message_text):
#     bot = telegram.Bot(token=bot_token)
#     await bot.send_message(chat_id=chat_id, text=message_text)
#     print("Message sent successfully!")
#
# # Run the coroutine asynchronously
# asyncio.run(send_telegram_message(bot_token, chat_id, bot_message))




# TODO SEND SMS using Twilio API: guide=programmable SMS Quickstart----
# from twilio.rest import Client ## install twilio module
#
# account_sid = 'your account id'
# auth_token = 'find on dashboard'
# client = client(account_sid, auth_token) # setup Twilio client
#
# message = client.message \   #creat the message to be sent
#     .create(
#     body='your message to be sent',
#     from='sender: trial num',
#     to='receiver: need verifier'
# )
#
# print(message.status) ##==print(message.sid): once the message has an ID printed, meaning it is sent successfully

