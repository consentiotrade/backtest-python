import unittest

from stock import Stock
from stock.service import StockService


class TestStock(unittest.TestCase):
    def setUp(self):
        self.service = StockService()

    def test_add_stock(self):
        new_stock = Stock("AAPL", 12.2, currency="AUD")
        self.service.add(new_stock)
        another_stock = Stock("GOGG", 10.1)
        self.service.add(another_stock)

    def test_get_stocks(self):
        new_stock = Stock("AAPL", 12.2, currency="AUD")
        self.service.add(new_stock)
        another_stock = Stock("GOGG", 10.1)
        self.service.add(another_stock)
        stocks = self.service.get_all()
        self.assertEqual(len(stocks), 2)


if __name__ == "__main__":
    unittest.main()