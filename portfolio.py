from typing import Tuple

from custom_types import JSONDict


class Portfolio:
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
        _, stockPrice = self.parseAPIData(ticker)
        if ticker not in self.stocks:
            pass
        elif self.stocks[ticker]['count'] < 1:
            pass
        else:
            self.cash += stockPrice
            self.stocks[ticker]['count'] -= 1

    def getTotalValue(self) -> float:
        cashSum = 0
        for stock in self.stocks:
            cashSum += stock.currentPrice
        return cashSum

    def parseAPIData(self, ticker: str) -> Tuple[JSONDict, float]:
        from api import getLatestStockData
        stockData = getLatestStockData(ticker)
        print(stockData)
        stockPrice = float(stockData['Global Quote']['05. price'])
        return stockData, stockPrice


def serialize(portfolio: Portfolio) -> JSONDict:
    return {'cash': portfolio.cash, 'stocks': portfolio.stocks}


def deserialize(portfolioJSON: JSONDict) -> Portfolio:
    return Portfolio(portfolioJSON['cash'], portfolioJSON['stocks'])
