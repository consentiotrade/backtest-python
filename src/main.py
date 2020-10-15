from flask import Flask, jsonify, request

from stock import Stock
from stock.service import StockService


app = Flask(__name__)

stock_service = StockService()


@app.route("/", methods=["GET"])
def index():
    return "Hello, world!"


@app.route("/stock", methods=["GET"])
def get_stocks():
    return jsonify([st.serialize() for st in stock_service.get_all()])


@app.route("/stock", methods=["POST"])
def load_stocks():
    st = Stock.parse(request.get_json())
    stock_service.add(st)
    return jsonify(st.serialize())


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
