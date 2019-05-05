# app.py
# Stock Simulator
# Main executable for stock trading web app

import json

from flask import Flask, render_template, session, request

from .api import apiBlueprint, searchStockData
from .portfolio import Portfolio, serialize
from .stock import stockBlueprint


def create_app():
    app = Flask(__name__)
    app.config.from_mapping(SECRET_KEY='secretkey')
    app.register_blueprint(apiBlueprint)
    app.register_blueprint(stockBlueprint)

    @app.route('/')
    def index():
        if 'portfolio' not in session:
            session['portfolio'] = serialize(Portfolio(10000, []))
        return render_template('index.html')

    @app.route('/search', methods=['POST'])
    def search():
        ticker = request.form['searchString']
        searchResults = searchStockData(ticker)
        return render_template('search.html', searchResults=searchResults, ticker=ticker)

    @app.route('/about')
    def about():
        return """
            CS372 Project by Jason Herning, Jake Herrman, George Meier, Dylan Palmieri, Andrew Adler, and Noah Snelson.
            """

    return app
