
function buyStock(ticker){
    var request = new XMLHttpRequest();
    var url = "http://127.0.0.1:5000/api/buy/" + ticker;
    request.onreadystatechange = function() {
    };
    request.open('POST', url, false);
    request.send();
}

function sellStock(ticker){
    var request = new XMLHttpRequest();
    var url = "http://127.0.0.1:5000/api/sell/" + ticker;
    request.onreadystatechange = function() {
    };
    request.open('POST', url, false);
    request.send();
}