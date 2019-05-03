from typing import List, Tuple

from flask import Blueprint, render_template

from .custom_types import JSONDict


class Stock():
    def __init__(
            self,
            ticker: str,
            price: float,
            count: int = 1,
            name: str = "",
            region: str = "",
            currency: str = "",
            history: List[Tuple[str, float]] = []):
        self.ticker = ticker
        self.name = name
        self.region = region
        self.currency = currency
        self.currentPrice = price
        self.count = count
        self.priceHistory = history

    def __str__(self) -> str:
        return f"${self.ticker}: ${self.currentPrice}"


def serialize(stock: Stock) -> JSONDict:
    return {'ticker': stock.ticker,
            'price': stock.currentPrice,
            'count': stock.count,
            'history': stock.priceHistory}


def deserialize(stockJSON: JSONDict) -> Stock:
    return Stock(stockJSON['ticker'],
                 stockJSON['price'],
                 stockJSON['count'],
                 stockJSON['history'])


stockBlueprint = Blueprint('stock', __name__, url_prefix='/stock')


@stockBlueprint.route('/<tickerSymbol>')
def stockSummaryPage(tickerSymbol):
    return render_template('stockSummary.html', tickerSymbol=tickerSymbol)
