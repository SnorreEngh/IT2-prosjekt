import requests

url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=D5E2JVERV0RPWC30'
# apikey = D5E2JVERV0RPWC30
r = requests.get(url, headers = {"User-agent": "Snorres mac"})
data = r.json()

print(data["Meta Data"]["2. Symbol"])

# def IBM(selskap):
#     url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={selskap}&interval=5min&apikey=demo'
#     r = requests.get(url, headers = {"User-agent": "Snorres mac"})
#     data = r.json()
#     print(data["Meta Data"]["2. Symbol"])
#     return r

# def kurs(selskap):
    # url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={selskap}&interval=5min&apikey=demo'
    # r = requests.get(url, headers = {"User-agent": "Snorres mac"})
    # data = r.json()
    # print(data["Time Series (5min)"]["2023-02-08 20:00:00"])
    # return r



def kurs(selskap):
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={selskap}&interval=5min&apikey=D5E2JVERV0RPWC30'
    r = requests.get(url, headers = {"User-agent": "Snorres mac"})
    data = r.json()

    timeseries = data["Time Series (5min)"]
    time_list_innhold = list(timeseries.values())
    time_list_dato = list(timeseries)
    time_list_dato[0]
    print(time_list_dato[0], time_list_innhold[0]['1. open'])

    return r

kurs("IBM")