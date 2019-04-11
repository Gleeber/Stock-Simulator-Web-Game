# api.py
# Defines several functions for retrieving financial data
import requests, json
from flask import current_app, g

with open('config.json') as configFile:
    configJSON = json.load(configFile)
    apiKey = configJSON['apiKey']
    apiURL = configJSON['apiURL']

def getIntradayStockData(stockSymbol:str, timeInterval:str, dataType:str='json'):
    paramsJSON = {
            'function' : 'TIME_SERIES_INTRADAY',
            'symbol' : stockSymbol,
            'interval' : timeInterval,
            'outputsize' : 'full',
            'datatype' : dataType,
            'apikey' : apiKey
            }
    dataRequestResponse = requests.get(apiURL, params=paramsJSON)
    return dataRequestResponse

def getDailyStockData(stockSymbol:str, dataType:str='json'):
    paramsJSON = {
            'function' : 'TIME_SERIES_DAILY',
            'symbol' : stockSymbol,
            'outputsize' : 'full',
            'datatype' : dataType,
            'apikey' : apiKey
            }
    dataRequestResponse = requests.get(apiURL, params=paramsJSON)
    return dataRequestResponse

def getLatestStockData(stockSymbol:str, dataType:str='json'): 
    paramsJSON = {
            'function' : 'GLOBAL_QUOTE',
            'symbol' : stockSymbol,
            'datatype' : dataType,
            'apikey' : apiKey
            }
    dataRequestResponse = requests.get(apiURL, params=paramsJSON)
    return dataRequestResponse

def searchStockData(keyword:str, dataType:str='json'):
    paramsJSON = {
            'function' : 'SYMBOL_SEARCH',
            'keywords' : keyword,
            'datatype' : dataType,
            'apikey' : apiKey
            }
    dataRequestResponse = requests.get(apiURL, params=paramsJSON)
    return dataRequestResponse

if __name__ == '__main__':
    response = getDailyStockData('MSFT')
    print(json.dumps(response.json(), indent=2))
