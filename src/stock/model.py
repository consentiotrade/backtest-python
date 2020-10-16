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