from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def hjem():
    url = "https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY_ADJUSTED&symbol={selskap}&apikey=demo"
    
    return render_template("index.html")

@app.route("/selskaper")
def selskaper():
    return render_template("index.html", )