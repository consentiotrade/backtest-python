from flask import Flask, jsonify, request

from stock.model import Stock, Client, StockA

app = Flask(__name__)

stocks = []

clients = {}


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


@app.route("/client", methods=["POST"])
def load_client():
    data = request.get_json()
    c = Client(data["client_id"], data["name"])
    clients[c.client_id] = c
    result = {
        "client_id": c.client_id,
        "name": c.name,
        "portfolio": {k: v.serialize() for (k, v) in c.portfolio.items()},
    }
    return jsonify(result)


@app.route("/client/<a>/portfolio", methods=["POST"])
def add_portfolio(a):
    data = request.get_json()
    sa = StockA.parse(data)
    c = clients[a]
    c.add_to_portfolio(sa)
    clients[a] = c
    result = {
        "client_id": c.client_id,
        "name": c.name,
        "portfolio": {k: v.serialize() for (k, v) in c.portfolio.items()},
    }
    return jsonify(result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
