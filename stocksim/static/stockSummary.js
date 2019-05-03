
function updateLatestPrice(){
    var tickerSymbol = document.getElementById('tickerHeader').innerText;
    var latestPriceRequest = new XMLHttpRequest();
    latestPriceRequest.responseType = 'json';
    var latestPriceURL = 'http://127.0.0.1:5000/api/latest/' + tickerSymbol;
    latestPriceRequest.onreadystatechange = function() {
        if(latestPriceRequest.readyState === 4 
            && latestPriceRequest.status === 200){
            var stockSummary = this.response;
            if(stockSummary.Note === undefined){
                stockSummary = stockSummary['Global Quote']
                console.log(stockSummary)
                document.getElementById('stockPrice').innerHTML =
                    stockSummary['05. price'];
                document.getElementById('stockHigh').innerHTML =
                    stockSummary['03. high'];
                document.getElementById('stockLow').innerHTML =
                    stockSummary['04. low'];
                document.getElementById('stockChange').innerHTML =
                    stockSummary['10. change percent'];
            }
        }
    }
    latestPriceRequest.open('GET', latestPriceURL, true);
    latestPriceRequest.send();
}

function graphPriceHistory(){
    var tickerSymbol = document.getElementById('tickerHeader').innerText;
    var dailyPriceHistoryRequest = new XMLHttpRequest();
    dailyPriceHistoryRequest.responseType = 'json';
    var dailyPriceURL = 'http://127.0.0.1:5000/api/daily/' + tickerSymbol;
    dailyPriceHistoryRequest.onreadystatechange = function() {
        if(dailyPriceHistoryRequest.readyState === 4 
            && dailyPriceHistoryRequest.status === 200){
            var dailyPriceHistory = dailyPriceHistoryRequest.response;
            if (dailyPriceHistory.Note === undefined){
                var prices = [];
                var dates = [];
                Object.keys(dailyPriceHistory["Time Series (Daily)"]).forEach( key => {
                    var openPrice = 
                        dailyPriceHistory["Time Series (Daily)"][key]["2. high"];
                    dates.push(key);
                    prices.push(openPrice);
                });
                var graphElement = document.getElementById('priceHistoryGraph');
                var config = {
                    type: 'line',
                    data: {
                        labels: dates,
                        datasets: [{
                            label: "USD",
                            data: prices,
                            fill: true,
                        }]
                    },
                    options: {
                        responsive: true
                    }
                };
                new Chart(graphElement, config);
            }
        }
    }
    dailyPriceHistoryRequest.open('GET', dailyPriceURL, true);
    dailyPriceHistoryRequest.send();
}

window.onload = () => {
    updateLatestPrice();
    graphPriceHistory();
}