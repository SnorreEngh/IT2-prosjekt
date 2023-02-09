import requests

url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={selskap}&interval=5min&apikey=D5E2JVERV0RPWC30'
r = requests.get(url)
data = r.json()


print(data)
