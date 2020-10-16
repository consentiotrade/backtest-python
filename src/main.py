from flask import Flask, jsonify, request

from stock.model import Stock

app = Flask(__name__)

stocks = []


@app.route("/", methods=["GET"])
def index():
    return "Hello, world!"


@app.route("/stock", methods=["GET"])
def get_stocks():
    return jsonify([st.serialize() for st in stocks])


@app.route("/stock", methods=["POST"])
def load_stocks():
    st = Stock.parse(request.get_json())
    stocks.append(st)
    return jsonify(st.serialize())


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
