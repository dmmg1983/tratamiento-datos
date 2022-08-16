from flask import Flask, Response, request

import json

from yahoo import search_in_yahoo_finance
import pprint
app = Flask(__name__)


@app.route("/")
def main():
    return "Hola Mundo"

@app.route("/api/search/")
def search():
    ticker = request.args.get("params")
    financial_info = search_in_yahoo_finance(ticker=ticker)
    return Response(json.dumps({
        "ticker": ticker,
        "name": financial_info["quotes"][0]["shortname"],
        "exchange": financial_info["quotes"][0]["exchange"],
        "sector": financial_info["quotes"][0]["sector"],
        "symbol": financial_info["quotes"][0]["symbol"],
        "industry": financial_info["quotes"][0]["industry"],
        "score": financial_info["quotes"][0]["score"],
        "isYahooFinance": financial_info["quotes"][0]["isYahooFinance"],
    }), status=200, mimetype="application/json")

@app.route ("/api/current-price")
def current_price():
    return "Hello, Jose Nice 2me2"

    #http://127.0.0.1:5000/api/search/?params=ko
