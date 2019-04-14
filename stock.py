from flask import Blueprint, render_template

class Stock():
    def __init__(self, ticker, price, history):
        self.ticker = ticker
        self.currentPrice = price
        self.priceHistory = history

    def __str__():
        return f"${ticker}: ${price}"

stockBlueprint = Blueprint('stock', __name__, url_prefix = '/stock')

@stockBlueprint.route('/<tickerSymbol>')
def stockSummaryPage(tickerSymbol):
    return render_template('stockSummary.html', tickerSymbol=tickerSymbol)
