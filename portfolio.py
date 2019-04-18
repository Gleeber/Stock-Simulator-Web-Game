from typing import Tuple

from custom_types import JSONDict


class Portfolio():
    def __init__(self, cash: float, stocks: JSONDict) -> None:
        self.cash = cash
        self.stocks = stocks

    def __str__(self) -> str:
        string = f"${self.cash}, Holdings: "
        string += str(self.stocks)
        return string

    def buyStock(self, ticker: str) -> None:
        stockData, stockPrice = self.parseAPIData(ticker)
        if ticker not in self.stocks:
            self.stocks[ticker] = {'count': 1, 'data': stockData}
        else:
            self.stocks[ticker]['count'] += 1
        self.cash -= stockPrice

    def sellStock(self, ticker: str) -> None:
        stockData, stockPrice = self.parseAPIData(ticker)
        if ticker not in self.stocks:
            raise Exception('No matching stocks in portfolio')
        elif self.stocks[ticker]['count'] < 1:
            raise Exception('No matching stocks in portfolio')
        else:
            self.cash += stockPrice
            self.stocks[ticker]['count'] -= 1

    def parseAPIData(self, ticker: str) -> Tuple[JSONDict, float]:
        from api import getLatestStockData
        stockData = getLatestStockData(ticker)
        stockPrice = float(stockData['Global Quote']['05. price'])
        return stockData, stockPrice


def serialize(portfolio):
    return {'cash' : portfolio.cash, 'stocks' : portfolio.stocks}

def deserialize(portfolioJSON):
    return Portfolio(portfolioJSON['cash'], portfolioJSON['stocks'])
