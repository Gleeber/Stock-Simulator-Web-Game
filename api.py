# api.py
# Defines several functions for retrieving financial data from AlphaVantage API

import json
import requests
from flask import Blueprint, jsonify, request

apiBlueprint = Blueprint('api', __name__, url_prefix='/api')

with open('config.json') as configFile:
    configJSON = json.load(configFile)
    apiKey = configJSON['apiKey']
    apiURL = configJSON['apiURL']


@apiBlueprint.route('/intraday', methods=['GET'])
def intraday():
    ticker = request.args.get('ticker')
    intradayStockData = getIntradayStockData(ticker)
    return jsonify(intradayStockData)


@apiBlueprint.route('/daily', methods=['GET'])
def daily():
    ticker = request.args.get('ticker')
    dailyStockData = getDailyStockData(ticker)
    return jsonify(dailyStockData)


@apiBlueprint.route('/latest', methods=['GET'])
def latest():
    ticker = request.args.get('ticker')
    latestStockData = getLatestStockData(ticker)
    return jsonify(latestStockData)


@apiBlueprint.route('/search', methods=['GET'])
def searchStocks():
    keyword = request.args.get('keyword')
    searchResults = searchStockData(keyword)
    return jsonify(searchResults)


def getIntradayStockData(stockSymbol: str, dataType: str = 'json'):
    paramsJSON = {
        'function': 'TIME_SERIES_INTRADAY',
        'symbol': stockSymbol,
        'interval': '1min',
        'outputsize': 'full',
        'datatype': dataType,
        'apikey': apiKey
    }
    dataRequestResponse = requests.get(apiURL, params=paramsJSON).json()
    return dataRequestResponse


def getDailyStockData(stockSymbol: str, dataType: str = 'json'):
    paramsJSON = {
        'function': 'TIME_SERIES_DAILY',
        'symbol': stockSymbol,
        'outputsize': 'full',
        'datatype': dataType,
        'apikey': apiKey
    }
    dataRequestResponse = requests.get(apiURL, params=paramsJSON).json()
    return dataRequestResponse


def getLatestStockData(stockSymbol: str, dataType: str = 'json'):
    paramsJSON = {
        'function': 'GLOBAL_QUOTE',
        'symbol': stockSymbol,
        'datatype': dataType,
        'apikey': apiKey
    }
    dataRequestResponse = requests.get(apiURL, params=paramsJSON).json()
    return dataRequestResponse


def searchStockData(keyword: str, dataType: str = 'json'):
    paramsJSON = {
        'function': 'SYMBOL_SEARCH',
        'keywords': keyword,
        'datatype': dataType,
        'apikey': apiKey
    }
    dataRequestResponse = requests.get(apiURL, params=paramsJSON).json()
    return dataRequestResponse


if __name__ == '__main__':
    response = getDailyStockData('MSFT')
    print(json.dumps(response.json(), indent=2))
