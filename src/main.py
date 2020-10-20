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
    c = Client.parse(data)
    clients[c.client_id] = c
    return jsonify(c.serialize())


@app.route("/client/<client_id>/portfolio", methods=["POST"])
def add_portfolio(client_id):
    sa = StockA.parse(request.get_json())
    c = clients[client_id]
    c.add_to_portfolio(sa)
    clients[client_id] = c
    return jsonify(c.serialize())


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
