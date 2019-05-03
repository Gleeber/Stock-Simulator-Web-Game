from typing import Tuple, List

from . import stock
from .custom_types import JSONDict
from .errors import APICallLimitError


API_CALL_LIMIT_MESSAGE_PREFIX = (
    'Thank you for using Alpha Vantage! Our standard API call frequency is'
)


class Portfolio():
    def __init__(self, cash: float, stocks: List[stock.Stock]) -> None:
        self.cash = cash
        self.stocks = stocks

    def __str__(self) -> str:
        string = f"${self.cash}, Holdings: "
        string += str(self.stocks)
        return string

    def buyStock(self, ticker: str) -> None:
        stockPrice = self.parseLatestPrice(ticker)
        # TODO why is priceHistory commented out?
        # priceHistory = self.parsePriceHistory(ticker)
        foundStock = False
        for stockItem in self.stocks:
            if stockItem.ticker == ticker:
                foundStock = True
                if self.cash >= stockPrice:
                    stockItem.count += 1
                    stockItem.currentPrice = stockPrice
                    self.cash -= stockPrice
        if not foundStock:
            self.stocks.append(stock.Stock(ticker, stockPrice, 1, []))
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
        cashSum = 0.
        for stockItem in self.stocks:
            cashSum += stockItem.currentPrice
            cashSum *= stockItem.count
        return cashSum

    def parseLatestPrice(self, ticker: str) -> float:
        from .api import getLatestStockData
        stockData = getLatestStockData(ticker)
        if 'Note' in stockData and stockData['Note'].startswith(
                API_CALL_LIMIT_MESSAGE_PREFIX):
            raise APICallLimitError()
        stockPrice = float(stockData['Global Quote']['05. price'])
        return stockPrice

    # Beware: Price history too large to store in session cookie.
    def parsePriceHistory(self, ticker: str) -> List[Tuple[str, float]]:
        from .api import getDailyStockData
        stockData = getDailyStockData(ticker)
        if 'Note' in stockData and stockData['Note'].startswith(
                API_CALL_LIMIT_MESSAGE_PREFIX):
            raise APICallLimitError()
        timeSeriesDaily = stockData['Time Series (Daily)']
        historyList = []
        for day in timeSeriesDaily.keys():
            historyList.append((day, timeSeriesDaily[day]['2. high']))
        return historyList


def serialize(portfolio: Portfolio) -> JSONDict:
    return {'cash': portfolio.cash,
            'stocks': [stock.serialize(item) for item in portfolio.stocks]}


def deserialize(portfolioJSON: JSONDict) -> Portfolio:
    return Portfolio(
        portfolioJSON['cash'],
        [stock.deserialize(item) for item in portfolioJSON['stocks']]
    )
