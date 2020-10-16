import unittest

import main
from stock.model import Stock


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


if __name__ == "__main__":
    unittest.main()