from flask import Flask, render_template
import requests
from api import kurs

app = Flask(__name__)

aksjeliste = kurs("IBM")

@app.route("/")
def hjem():
    url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={selskap}&interval=5min&apikey=D5E2JVERV0RPWC30"
    r = requests.get(url, headers = {"User-agent": "Snorres mac"})
    data = r.json()
    print(data)

    return render_template("index.html", aksjeliste=aksjeliste)

@app.route("/selskaper")
def selskaper():
    return render_template("selskaper.html")


# timeseries = data["timeseries (5min)"]

# time_list = list(timeseries)
# time_list[0]
# print(time_list)


# timeseries = {
#     "123": "hei"
#     "123": "hei"
#     "123": "hei"
#     "123": "hei"
# }

# time_list = list(timeseries.values())
