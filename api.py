# api.py
# Defines several functions for retrieving financial data from AlphaVantage API

import json
import requests
from typing import cast
from flask import Blueprint, jsonify, request, session
from portfolio import deserialize, serialize
from custom_types import JSONDict

apiBlueprint = Blueprint('api', __name__, url_prefix='/api')

with open('config.json') as configFile:
    configJSON = json.load(configFile)
    apiKey = configJSON['apiKey']
    apiURL = configJSON['apiURL']
print(apiKey)


@apiBlueprint.route('/intraday', methods=['GET'])
def intraday():
    ticker = request.args['ticker']
    intradayStockData = getIntradayStockData(ticker)
    return jsonify(intradayStockData)


@apiBlueprint.route('/daily', methods=['GET'])
def daily():
    ticker = request.args['ticker']
    dailyStockData = getDailyStockData(ticker)
    return jsonify(dailyStockData)


@apiBlueprint.route('/latest', methods=['GET'])
def latest():
    ticker = request.args['ticker']
    latestStockData = getLatestStockData(ticker)
    return jsonify(latestStockData)


@apiBlueprint.route('/search', methods=['GET'])
def searchStocks():
    keyword = request.args['keyword']
    searchResults = searchStockData(keyword)
    return jsonify(searchResults)


@apiBlueprint.route('/buy/<ticker>', methods=['POST'])
def buyStock(ticker):
    portfolio = deserialize(session['portfolio'])
    portfolio.buyStock(ticker)
    session['portfolio'] = serialize(portfolio)
    return 'OK'


@apiBlueprint.route('/sell/<ticker>', methods=['POST'])
def sellStock(ticker):
    portfolio = deserialize(session['portfolio'])
    try:
        portfolio.sellStock(ticker)
        session['portfolio'] = serialize(portfolio)
        return 'OK'
    except Exception as e:
        raise e


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
        'apikey': apiKey
    }
    dataRequestResponse = requests.get(apiURL, params=paramsJSON).json()
    return cast(JSONDict, dataRequestResponse)


def getDailyStockData(stockSymbol: str, dataType: str = 'json') -> JSONDict:
    paramsJSON = {
        'function': 'TIME_SERIES_DAILY',
        'symbol': stockSymbol,
        'outputsize': 'full',
        'datatype': dataType,
        'apikey': apiKey
    }
    dataRequestResponse = requests.get(apiURL, params=paramsJSON).json()
    return cast(JSONDict, dataRequestResponse)


def getLatestStockData(stockSymbol: str, dataType: str = 'json') -> JSONDict:
    paramsJSON = {
        'function': 'GLOBAL_QUOTE',
        'symbol': stockSymbol,
        'datatype': dataType,
        'apikey': apiKey
    }
    dataRequestResponse = requests.get(apiURL, params=paramsJSON).json()
    return cast(JSONDict, dataRequestResponse)


def searchStockData(keyword: str, dataType: str = 'json') -> JSONDict:
    paramsJSON = {
        'function': 'SYMBOL_SEARCH',
        'keywords': keyword,
        'datatype': dataType,
        'apikey': apiKey
    }
    dataRequestResponse = requests.get(apiURL, params=paramsJSON).json()
    return cast(JSONDict, dataRequestResponse)


if __name__ == '__main__':
    data = getDailyStockData('MSFT')
    print(json.dumps(data, indent=2))
