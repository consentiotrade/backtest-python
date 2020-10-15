class StockService:
    stocks = []

    def __init__(self):
        self.stocks = []

    def add(self, st):
        self.stocks.append(st)

    def get(self, idx):
        return self.stocks[idx]

    def get_all(self):
        return self.stocks