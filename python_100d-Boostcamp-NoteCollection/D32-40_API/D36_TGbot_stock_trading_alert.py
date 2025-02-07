STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
MY_ALPHA_API_KEY= 'OPYDZ24SBSBXWNTS'
MY_NEWSAPI = '5d951fd2b623427f8035dd483c29b699'
bot_token = '6355492896:AAH8ffnob2_ibRMh3Jnjy-2QqXW4WHUCDvg'
chat_id='1387810108'

import requests
import random

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
def get_news(num):
    news_parameter = {
        'q': 'tesla',
        'from': day2_date,
        'to': day1_date,
        'sortBy': 'popularity',
        'apiKey': {MY_NEWSAPI},
    }
    news_response = requests.get(url=f'https://newsapi.org/v2/everything', params=news_parameter)
    news_response.raise_for_status()
    news_data = news_response.json()

    aritle1=news_data['articles'][num]
    headline1=aritle1['title']
    press1=aritle1['source']['name']
    brief1=aritle1['description']
    url1=aritle1['url']
    return (f'Headline: {headline1}\n\nBrief: {brief1}\n\nReport by: {press1}\n\nMore info: {url1}')


    ## METHOD2: if going with first 3 articles, then loop through the formatted list to send each article:
    # three_article = news_data['articles'][:3]
    # formatted_article_list = [f"Headline: {article['title']}. \nBrief:{article['description']" for article in three_articles]



## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.
#Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

# I'm using a TG bot
# TG_endpoint = f'https://api.telegram.org/bot{bot_token}/METHOD_NAME'
def telegram_bot_sendtext(message, token,id):
    token = token
    parameters = {
        'chat_id': id,
        'text': message,
    }
    TG_endpoint = f'https://api.telegram.org/bot{token}/sendMessage'

    TG_response = requests.get(url=TG_endpoint, params=parameters)
    TG_response.raise_for_status()


## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
# i'm using TIME_SERIES_DAILY API
# parameter={ ##compact returns only the latest 100 data points; full returns the full-length time series of 20+ years of historical data
#     'outputsize': 'compact',
#     'function': 'TIME_SERIES_DAILY',
#     'symbol': STOCK,
#     'apikey': MY_ALPHA_API_KEY,
# }

alpha_response = requests.get(url=f'https://www.alphavantage.co/query', params=parameter)
alpha_response.raise_for_status()
stock_data = alpha_response.json()



data = stock_data['Time Series (Daily)']
date_list =[key for (key,value) in data.items()] ##防止出现不定期休市：只取dict中前两个值


day1_date = date_list[0] ##type: string; '2024-05-28'
day2_date = date_list[1]
day1_close = float(stock_data['Time Series (Daily)'][day1_date]['4. close'])
day2_close = float(stock_data['Time Series (Daily)'][day2_date]['4. close'])

day1_high = float(stock_data['Time Series (Daily)'][day1_date]['2. high'])
day2_high = float(stock_data['Time Series (Daily)'][day2_date]['2. high'])

close_diffe = (day1_close-day2_close)/day2_close
high_diffe = (day1_high-day2_high)/day2_high

symbol = ('📈', '📉')
if close_diffe != abs(close_diffe):
    trend =1
else:
    trend =0

if abs(close_diffe) > 0.01:
    num_message = (f'TSLA: {symbol[trend]}{round(close_diffe*100,2)}% \n\nTime: from {day2_date} to {day1_date}\n\n')
    pick=random.randint(0,5)
    news_message = get_news(pick)
    telegram_bot_sendtext(message=num_message+news_message, token=bot_token, id=chat_id)
