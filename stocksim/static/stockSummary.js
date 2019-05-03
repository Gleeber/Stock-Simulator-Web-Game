
function updateLatestPrice(){
    var tickerSymbol = document.getElementById('tickerHeader').innerText;
    var latestPriceRequest = new XMLHttpRequest();
    var latestPriceURL = 'http://127.0.0.1:5000/api/latest/' + tickerSymbol;
    latestPriceRequest.onreadystatechange = function() {
        document.getElementById('stockSummary').innerHTML = this.responseText;
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
        if(dailyPriceHistoryRequest.readyState ==4 && dailyPriceHistoryRequest.status ==200){
            var dailyPriceHistory = dailyPriceHistoryRequest.response;
            var prices = [];
            var dates = [];
            Object.keys(dailyPriceHistory["Time Series (Daily)"]).forEach( key => {
                var openPrice = dailyPriceHistory["Time Series (Daily)"][key]["2. high"];
                dates.push(key);
                prices.push(openPrice);
            });
            console.log(dates);
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
    dailyPriceHistoryRequest.open('GET', dailyPriceURL, true);
    dailyPriceHistoryRequest.send();
}

window.onload = () => {
    updateLatestPrice();
    graphPriceHistory();
}