import requests
import json

fil = open("s&p.json", encoding="utf-8")
sp = json.load(fil)
fil.close()

def kurs(selskap):
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={selskap}&interval=5min&apikey=D5E2JVERV0RPWC30'
    r = requests.get(url, headers = {"User-agent": "Snorres mac"})
    data = r.json()

    timeseries = data["Time Series (5min)"]
    time_list_innhold = list(timeseries.values())
    time_list_dato = list(timeseries)
    time_list_dato[0]
    #print(data["Meta Data"]["2. Symbol"])
    #print(time_list_dato[0], time_list_innhold[0]['1. open'])

    return time_list_innhold[0]


def gaarsdagens_kurs(selskap):
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={selskap}&apikey=D5E2JVERV0RPWC30'
    r = requests.get(url, headers = {"User-agent": "Snorres mac"})
    data = r.json()

    timeseries = data["Time Series (Daily)"]
    time_list_innhold = list(timeseries.values())
    time_list_dato = list(timeseries)
    time_list_dato[1]

    # print(time_list_dato[1], time_list_innhold[1]['1. open'])
    return time_list_innhold[1]

