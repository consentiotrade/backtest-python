from datetime import datetime


class Stock:
    symbol = None
    price = 0.0
    currency = "EUR"
    created_at = None

    def __init__(self, symbol, price, currency="EUR"):
        self.symbol = symbol
        self.price = price
        self.currency = currency
        self.created_at = datetime.now()

    @staticmethod
    def parse(data):
        """
        parse a dict and return a Stock instance
        """
        return Stock(data["symbol"], data["price"], data["currency"])

    def serialize(self):
        return {
            "symbol": self.symbol,
            "price": self.price,
            "currency": self.currency,
            "created_at": self.created_at,
        }


class StockA:
    """
    same as stock but with amount
    """

    def __init__(self, s, a):
        self.stock = s
        self.amount = a

    @staticmethod
    def parse(data):
        """
        parses data
        """
        return StockA(
            Stock(
                data["stock"]["symbol"],
                data["stock"]["price"],
                data["stock"]["currency"],
            ),
            data["amount"],
        )

    def serialize(self):
        return {
            "stock": {
                "symbol": self.stock.symbol,
                "price": self.stock.price,
                "currency": self.stock.currency,
                "created_at": self.stock.created_at,
            },
            "amount": self.amount,
        }


class Client:
    def __init__(self, client_id, name):
        self.client_id = client_id
        self.name = name
        self.portfolio = {}

    def add_to_portfolio(self, s):
        self.portfolio[s.stock.symbol] = s

    @staticmethod
    def parse(data):
        return Client(data["client_id"], data["name"])

    def serialize(self):
        return {
            "client_id": self.client_id,
            "name": self.name,
            "portfolio": {k: v.serialize() for (k, v) in self.portfolio.items()},
        }
