# This code sends SMS to the user number if Apple stock has more then 3% change up or down.

import requests
from datetime import date, timedelta
from twilio.rest import Client

account_sid = 'AC43d33746c61b3124371833da9f4f85b5'
auth_token = '001d564321a27b13cabe7c13a168da7b'
fake_target = "write target number here"
phone_number = "+14845145064"

STOCK_NAME = "AAPL"
COMPANY_NAME = "Apple"
PRICE_CHANGE = 0

news_api = "f6a756692afd4356ba0497d413d51b40"

alphavantage_api = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": "3X7Z9ROJHY44LIXL",
}

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
# alphavantage_api_key = "BB6FVXS2SHFN2TOL"

response = requests.get(STOCK_ENDPOINT, params=alphavantage_api)
print(response)
today = date.today()  # today date
yesterday = today - timedelta(days=1)  # yesterday date
yesterday_date = "-".join(
    yesterday.strftime("%Y %m %d").split())  # convert var from datetime type to string with - as sep

yesterday = today - timedelta(days=2)  # day before yesterday date
before_yesterday_date = "-".join(
    yesterday.strftime("%Y %m %d").split())  # convert var from datetime type to string with - as sep

print(yesterday_date)
print(before_yesterday_date)

data = response.json()
print(data)
stock_yesterday_close_price = data['Time Series (Daily)'][yesterday_date]['4. close']
stock_before_yesterday_close_price = data['Time Series (Daily)'][before_yesterday_date]['4. close']
print(stock_yesterday_close_price)
print(stock_before_yesterday_close_price)

# calculate value for % check later
price_change = float(stock_yesterday_close_price) - float(stock_before_yesterday_close_price).__round__(2)
up_or_down = None
if price_change > 0:
    up_or_down = "🔺"
else:
    up_or_down = "🔻"

print(price_change)
price_percentage_change = (price_change / float(stock_before_yesterday_close_price) * 100).__round__(4)
print(price_percentage_change, "%")

if abs(price_percentage_change) >= PRICE_CHANGE: #check absolute value
    news_api = {
        "sortBy": "popularity",
        "language": "en",
        "qInTitle": COMPANY_NAME,
        "apikey": news_api,
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_api)
    news_data = news_response.json()['articles']
    top_three_art = news_data[:3]
    print(top_three_art)

    formatted_articles = [f"{STOCK_NAME}: {up_or_down}{price_change.__round__(2)}% \nHeadline: {article['title']}. \n\nBrief: {article['description']}" for article in
                          top_three_art]
    print(formatted_articles)
    #Send each article as a separate message via Twilio.
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body=formatted_articles[0],
        from_=phone_number,
        to=fake_target
    )
print(message.status)
