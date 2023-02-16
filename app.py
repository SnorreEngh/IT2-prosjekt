from flask import Flask, render_template
from api import kurs, gaarsdagens_kurs

app = Flask(__name__)

@app.route("/")

def hjem():

    kurs_selskap = kurs("IBM")
    kurs_selskap_gaar = gaarsdagens_kurs("IBM")

    return render_template("index.html", kurs_selskap=kurs_selskap, kurs_selskap_gaar=kurs_selskap_gaar)

@app.route("/selskaper")
def selskaper():

    kurs_selskap = kurs("IBM")
    kurs_selskap_gaar = gaarsdagens_kurs("IBM")

    return render_template("selskaper.html", kurs_selskap=kurs_selskap, kurs_selskap_gaar=kurs_selskap_gaar)

app.run(debug=True)