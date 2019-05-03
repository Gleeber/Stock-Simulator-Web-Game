function updateTotalValue(){
    var request = new XMLHttpRequest();
    var url = "http://127.0.0.1:5000/api/totalValue";
    request.onreadystatechange = function() {
        document.getElementById('totalValue').innerHTML = this.responseText;
    };
    request.open('GET', url, false);
    request.send();
}
function updatePortfolio(){
    var request = new XMLHttpRequest();
    var url = "http://127.0.0.1:5000/api/portfolio";
    request.onreadystatechange = function() {
        document.getElementById('portfolio').innerHTML = this.responseText;
    };
    request.open('GET', url, false);
    request.send();
}

function updateAllUserInfo(){
    updateTotalValue();
    updatePortfolio();
}