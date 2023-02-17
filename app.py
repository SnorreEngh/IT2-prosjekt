from flask import Flask, render_template
from api import kurs, gaarsdagens_kurs
from test import aapl_historical, data, hent_info

app = Flask(__name__)

@app.route("/")
def hjem():

    kurs_selskap = kurs("IBM")
    kurs_selskap_gaar = gaarsdagens_kurs("IBM")

    return render_template("index.html", kurs_selskap=kurs_selskap, kurs_selskap_gaar=kurs_selskap_gaar)

@app.route("/selskaper")
def selskaper():
    apple = hent_info("AAPL")

    return render_template("selskaper.html", aapl_historical=aapl_historical, data=data, apple=apple)

app.run(debug=True)