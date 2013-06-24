var sock = null;
var wsuri = "ws://localhost:9000";

function buildHost() {
    sock = new WebSocket(wsuri);
    
    sock.onopen = function () {
        console.log("connected to " + wsuri);
        var message = "Test";
        send(message);
    };
    sock.onclose = function (e) {
        console.log("connection closed (" + e.code + ")");
        document.getElementById('connection').innerHTML += '<br>connection closed (' + e.code + ')';
    };
    sock.onmessage = function (e) {
        console.log("message received: " + e.data);
        document.getElementById('connection').innerHTML='<br>' + e.data;
    };
}

function send(e) {
    var msg = e;
    sock.send(msg);
}
		
function setIp() {
    wsuri = "ws://" + document.getElementById('ipinput').value + ":55555";
}
         
function getIp() {
    document.getElementById('connectto').innerHTML = document.getElementById('ipinput').value;
}