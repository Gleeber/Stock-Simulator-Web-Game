var tickerSymbol = document.getElementById('tickerHeader').innerText;
var latestPriceRequest = new XMLHttpRequest();
var latestPriceURL = 'http://127.0.0.1:5000/api/latest/' + tickerSymbol;
latestPriceRequest.onreadystatechange = function() {
     document.getElementById('stockSummary').innerHTML = this.responseText;
}
latestPriceRequest.open('GET', latestPriceURL, true);
latestPriceRequest.send();
var dailyPriceHistoryRequest = new XMLHttpRequest();
dailyPriceHistoryRequest.responseType = 'json';
var dailyPriceURL = 'http://127.0.0.1:5000/api/daily/' + tickerSymbol;
dailyPriceHistoryRequest.onreadystatechange = function() {
    var dailyPriceHistory = this.response;
    var graphElement = document.getElementById('priceHistoryGraph');
    var config = {
        type: 'line',
        data: [1,2,3,4,5],
        options: {}
    }
    new Chart(graphElement, config);
}
dailyPriceHistoryRequest.open('GET', dailyPriceURL, true);
dailyPriceHistoryRequest.send();