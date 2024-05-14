# this code runs from tuesday till saturday and reports on 15:00

import requests
from datetime import date, timedelta
from twilio.rest import Client
import os


account_sid = os.environ.get('SID')
auth_token = os.environ.get('AUTHTOKEN')
news_api = os.environ.get('NEWSAPI')
#news_api = '0e96d6648fff43f988f6fad0c707e43c'
fake_target = os.environ.get('MYPHONE')
phone_number = "+14062296126"

PRICE_CHANGE = 3  # absolute change to check for

holdings = [
    {
        'STOCK_NAME': "AAPL",
        'COMPANY_NAME': "Apple"
    },
    {
        'STOCK_NAME': "AMZN",
        'COMPANY_NAME': "Amazon"
    },
    {
        'STOCK_NAME': "BRK.B",
        'COMPANY_NAME': "Brekshire Hathaway"
    },
    {
        'STOCK_NAME': "DHT",
        'COMPANY_NAME': "DHT holdings"
    },
    {
        'STOCK_NAME': "GOOGL",
        'COMPANY_NAME': "Google"
    },
    {
        'STOCK_NAME': "META",
        'COMPANY_NAME': "Meta"
    },
    {
        'STOCK_NAME': "MSFT",
        'COMPANY_NAME': "Microsoft"
    }
]

for stock in holdings:
    STOCK_NAME = stock['STOCK_NAME']
    COMPANY_NAME = stock['COMPANY_NAME']
    alphavantage_api = {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK_NAME,
        "apikey": 'E9R1PEEGUJ85N9ZU'
    } # older key = 3X7Z9ROJHY44LIXL

    STOCK_ENDPOINT = "https://www.alphavantage.co/query"
    NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

    try:
        response = requests.get(STOCK_ENDPOINT, params=alphavantage_api)
        print(response)
        today = date.today()  # today date
        yesterday = today - timedelta(days=1)  # yesterday date
        yesterday_date = yesterday.strftime("%Y-%m-%d")  # convert var from datetime type to string

        b_last_trade_day = 4 if date.weekday(today) == 1 else 2 # if its tuesday shows monday vs friday change

        byesterday = today - timedelta(days=b_last_trade_day)  # trade day before yesterday trade date
        before_yesterday_date = byesterday.strftime("%Y-%m-%d")  # convert var from datetime type to string

        data = response.json()  # save data from stock API
        # gets closing price of yesterday and the day before
        stock_yesterday_close_price = data['Time Series (Daily)'][yesterday_date]['4. close']
        stock_before_yesterday_close_price = data['Time Series (Daily)'][before_yesterday_date]['4. close']

        # calculate value for % check later
        price_change = float(stock_yesterday_close_price) - float(stock_before_yesterday_close_price).__round__(2)
        up_or_down = None
        if price_change > 0:
            up_or_down = "🔺"
        else:
            up_or_down = "🔻"

        price_percentage_change = (price_change / float(stock_before_yesterday_close_price) * 100).__round__(4)
        # print(price_percentage_change, "%")

        if abs(price_percentage_change) >= PRICE_CHANGE:  # check absolute value
            news_param = {
                "sortBy": "popularity",
                "language": "en",
                "qInTitle": COMPANY_NAME,
                "apikey": news_api,
            }
            news_response = requests.get(NEWS_ENDPOINT, params=news_param)
            print(newsdata := news_response.json())
            news_data = news_response.json()['articles']
            top_three_art = news_data[:3] # only top 3 from the list

            formatted_articles = [
                f"{STOCK_NAME}: {up_or_down}{price_change.__round__(2)}% \nHeadline: {article['title']}. \n\nBrief: {article['description']}\nLink: {article['url']}"
                for article in
                top_three_art]
            # Send each article as a separate message via Twilio.
            client = Client(account_sid, auth_token)
            message = client.messages \
                .create(
                body=formatted_articles[0],
                from_=phone_number,
                to=fake_target
            )
            # print(message.status)
    except requests.RequestException as e:
        print(f"Error making API request for {STOCK_NAME}: {e}")
