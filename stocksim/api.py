# api.py
# Defines several functions for retrieving financial data from AlphaVantage API

import json
from random import randint
from typing import cast

from flask import Blueprint, jsonify, session
import requests

from .custom_types import JSONDict
from .portfolio import deserialize, serialize

apiBlueprint = Blueprint('api', __name__, url_prefix='/api')

with open('config.json') as configFile:
    configJSON = json.load(configFile)
    # It seems that the Alpha Vantage API key can actually be any non-empty
    # string.
    apiURL = configJSON['apiURL']


def getApiKey() -> str:
    return ''.join(chr(randint(97, 122)) for _ in range(100))


@apiBlueprint.route('/intraday/<ticker>', methods=['GET'])
def intraday(ticker):
    intradayStockData = getIntradayStockData(ticker)
    return jsonify(intradayStockData)


@apiBlueprint.route('/daily/<ticker>', methods=['GET'])
def daily(ticker):
    dailyStockData = getDailyStockData(ticker)
    return jsonify(dailyStockData)


@apiBlueprint.route('/latest/<ticker>', methods=['GET'])
def latest(ticker):
    latestStockData = getLatestStockData(ticker)
    return jsonify(latestStockData)


@apiBlueprint.route('/search/<keyword>', methods=['GET'])
def searchStocks(keyword):
    searchResults = searchStockData(keyword)
    return jsonify(searchResults)


@apiBlueprint.route('/buy/<ticker>', methods=['POST'])
def buyStock(ticker):
    portfolio = deserialize(session['portfolio'])
    portfolio.buyStock(ticker)
    session['portfolio'] = serialize(portfolio)
    return str(session['portfolio'])


@apiBlueprint.route('/sell/<ticker>', methods=['POST'])
def sellStock(ticker):
    portfolio = deserialize(session['portfolio'])
    portfolio.sellStock(ticker)
    session['portfolio'] = serialize(portfolio)
    return str(session['portfolio'])

@apiBlueprint.route('/portfolio', methods=['GET'])
def getPortfolio():
    return jsonify(session['portfolio'])

@apiBlueprint.route('/totalValue', methods=['GET'])
def getTotalPortfolioValue():
    portfolio = deserialize(session['portfolio'])
    totalValue = portfolio.getTotalValue()
    return jsonify(totalValue)

# We must cast return values to JSONDict because requests.Response.json does
# not have a return type annotation. This does not actually check that the
# values satisfy the JSONDict type definition, it just stops mypy from
# complaining.


def getIntradayStockData(
        stockSymbol: str, dataType: str = 'json') -> JSONDict:
    paramsJSON = {
        'function': 'TIME_SERIES_INTRADAY',
        'symbol': stockSymbol,
        'interval': '1min',
        'outputsize': 'full',
        'datatype': dataType,
        'apikey': getApiKey()
    }
    dataRequestResponse = requests.get(apiURL, params=paramsJSON).json()
    return cast(JSONDict, dataRequestResponse)


def getDailyStockData(stockSymbol: str, dataType: str = 'json') -> JSONDict:
    paramsJSON = {
        'function': 'TIME_SERIES_DAILY',
        'symbol': stockSymbol,
        'outputsize': 'full',
        'datatype': dataType,
        'apikey': getApiKey()
    }
    dataRequestResponse = requests.get(apiURL, params=paramsJSON).json()
    return cast(JSONDict, dataRequestResponse)


def getLatestStockData(stockSymbol: str, dataType: str = 'json') -> JSONDict:
    paramsJSON = {
        'function': 'GLOBAL_QUOTE',
        'symbol': stockSymbol,
        'datatype': dataType,
        'apikey': getApiKey()
    }
    dataRequestResponse = requests.get(apiURL, params=paramsJSON).json()
    return cast(JSONDict, dataRequestResponse)


def searchStockData(keyword: str, dataType: str = 'json') -> JSONDict:
    paramsJSON = {
        'function': 'SYMBOL_SEARCH',
        'keywords': keyword,
        'datatype': dataType,
        'apikey': getApiKey()
    }
    dataRequestResponse = requests.get(apiURL, params=paramsJSON).json()
    return cast(JSONDict, dataRequestResponse)
