import unittest

import main
import json
from stock.model import Stock, Client, StockA


class TestStock(unittest.TestCase):
    def setUp(self):
        main.app.config["TESTING"] = True
        self.client = main.app.test_client()

    def test_get_stocks(self):
        main.stocks = [
            Stock("APPL", 12.2, currency="AUD"),
            Stock("GOOG", 1.5),
        ]
        resp = self.client.get("/stock")
        data = resp.get_json()

        self.assertEqual(len(data), len(main.stocks))


class TestPortfolio(unittest.TestCase):
    def setUp(self):
        main.app.config["TESTING"] = True
        self.client = main.app.test_client()

    def test_get_stocks(self):
        """
        testing adding elements to portfolio
        """
        main.clients = {
            "foo": Client("foo", "Manolo"),
        }
        expected = {
            "amount": 13.3,
            "stock": {
                "symbol": "APPL",
                "price": 3.14,
                "currency": "USD",
            },
        }
        data = json.dumps(expected)
        resp = self.client.post(
            "/client/foo/portfolio",
            data=data,
            content_type="application/json",
        )
        data = resp.get_json()
        self.assertEqual(200, resp.status_code, str(resp))


if __name__ == "__main__":
    unittest.main()