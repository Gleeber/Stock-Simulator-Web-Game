from typing import Tuple, List

from . import stock
from .custom_types import JSONDict


class Portfolio():
    def __init__(self, cash: float, stocks: JSONDict) -> None:
        self.cash = cash
        self.stocks = stocks

    def __str__(self) -> str:
        string = f"${self.cash}, Holdings: "
        string += str(self.stocks)
        return string

    def buyStock(self, ticker: str) -> None:
        stockPrice = self.parseLatestPrice(ticker)
        priceHistory = self.parsePriceHistory(ticker)
        for stockItem in self.stocks:
            if stockItem.ticker == ticker:
                stockItem.count += 1
                stockItem.currentPrice = stockPrice
                self.cash -= stockPrice
                return
        self.stocks.append(stock.Stock(ticker, stockPrice, 1, priceHistory))
        self.cash -= stockPrice

    def sellStock(self, ticker: str) -> None:
        stockPrice = self.parseLatestPrice(ticker)
        for stockItem in self.stocks:
            if stockItem.ticker == ticker:
                stockItem.count -= 1
                if stockItem.count == 0:
                    self.stocks.remove(stockItem)
                self.cash += stockPrice
                break

    def getTotalValue(self) -> float:
        cashSum = 0
        for stockItem in self.stocks:
            cashSum += stockItem.currentPrice
            cashSum *= stockItem.count
        return cashSum

    def parseLatestPrice(self, ticker: str) -> float:
        from .api import getLatestStockData
        stockData = getLatestStockData(ticker)
        stockPrice = float(stockData['Global Quote']['05. price'])
        return stockPrice

    def parsePriceHistory(self, ticker: str) -> List[Tuple[str, float]]:
        from .api import getDailyStockData
        stockData = getDailyStockData(ticker)['Time Series (Daily)']
        historyList = []
        for day in stockData.keys():
            historyList.append((day, stockData[day]['2. high']))
        print('\n', historyList[0:5], '\n')
        return historyList


def serialize(portfolio: Portfolio) -> JSONDict:
    return {'cash': portfolio.cash,
            'stocks': [stock.serialize(item) for item in portfolio.stocks]}


def deserialize(portfolioJSON: JSONDict) -> Portfolio:
    return Portfolio(
        portfolioJSON['cash'],
        [stock.deserialize(item) for item in portfolioJSON['stocks']]
    )
