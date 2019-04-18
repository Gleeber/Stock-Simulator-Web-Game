class Portfolio():
    def __init__(self, cash: float, stocks: dict):
        self.cash = cash
        self.stocks = stocks

    def __str__(self) -> str:
        string = f"${self.cash}, Holdings: "
        string += str(self.stocks)
        return string

    def buyStock(self, ticker: str):
        from api import getLatestStockData
        stockData = getLatestStockData(ticker)
        print(stockData)
        stockPrice = float(stockData['Global Quote']['05. price'])
        if ticker not in self.stocks:
            self.stocks[ticker] = {'count': 1, 'data': stockData}
        else:
            self.stocks[ticker]['count'] += 1
        self.cash -= stockPrice
        print(self)


def serialize(portfolio):
    return {
            'cash': portfolio.cash,
            'stocks': portfolio.stocks
            }


def deserialize(portfolioJSON):
    return Portfolio(portfolioJSON['cash'], portfolioJSON['stocks'])
