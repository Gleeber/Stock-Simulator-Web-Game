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
    location.reload();
}

function updateAllUserInfo(){
    updateTotalValue();
    updatePortfolio();
}

window.onload = function(){
    updateTotalValue();
}