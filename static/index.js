function buyMSFT(){
    var request = new XMLHttpRequest();
    var url = "http://127.0.0.1:5000/api/buy/MSFT";
    request.onreadystatechange = function() {
        document.getElementById('portfolio').innerHTML = this.responseText;
    };
    request.open('POST', url, false);
    request.send();
    updateTotalValue();
}

function sellMSFT(){
    var request = new XMLHttpRequest();
    var url = "http://127.0.0.1:5000/api/sell/MSFT";
    request.onreadystatechange = function() {
        document.getElementById('portfolio').innerHTML = this.responseText;
    };
    request.open('POST', url, false);
    request.send();
    updateTotalValue();
}

function updateTotalValue(){
    var request = new XMLHttpRequest();
    var url = "http://127.0.0.1:5000/api/totalValue";
    request.onreadystatechange = function() {
        document.getElementById('totalValue').innerHTML = this.responseText;
    };
    request.open('GET', url, false);
    request.send();
}
updateTotalValue();
