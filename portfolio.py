from typing import Tuple
import stock
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
        _, stockPrice = self.parseAPIData(ticker)
        for stockItem in self.stocks:
            if stockItem.ticker == ticker:
                stockItem.count += 1
                stockItem.currentPrice = stockPrice
                self.cash -= stockPrice
                return
        self.stocks.append(stock.Stock(ticker, stockPrice, 1))
        self.cash -= stockPrice

    def sellStock(self, ticker: str) -> None:
        _, stockPrice = self.parseAPIData(ticker)
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
            print('\n', stockItem.currentPrice, stockItem.count, cashSum, '\n')
            cashSum += stockItem.currentPrice
            cashSum *= stockItem.count
        return cashSum

    def parseAPIData(self, ticker: str) -> Tuple[JSONDict, float]:
        from api import getLatestStockData
        stockData = getLatestStockData(ticker)
        stockPrice = float(stockData['Global Quote']['05. price'])
        return stockData, stockPrice


def serialize(portfolio: Portfolio) -> JSONDict:
    return {'cash': portfolio.cash, 
            'stocks': [stock.serialize(item) for item in portfolio.stocks]}


def deserialize(portfolioJSON: JSONDict) -> Portfolio:
    return Portfolio(portfolioJSON['cash'], [stock.deserialize(item) for item in portfolioJSON['stocks']])
