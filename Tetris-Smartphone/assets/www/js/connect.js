var sock = null;
var wsuri = "ws://localhost:9000";
var ip = null;
var currIP = null;
var currCmd = null;
var nickname = null;
var ready = false;

function buildHost() {
    sock = new WebSocket(wsuri);
    
    sock.onopen = function () {
        console.log("connected to " + wsuri);
    };
    sock.onclose = function (e) {
        console.log("connection closed (" + e.code + ")");
        document.getElementById('connection').innerHTML += '<p>connection closed (' + e.code + ')';
       
    };
    sock.onmessage = function (e) {
        //Decide how the incomming message is interpreted
        //We use an generic simple parser to decode the message
        //The messages are composed in the following scheme:
        // "IP###COMMAND", e.g. "192.168.0.2###Test".
        if(ip == null){
            ip = e.data;
            console.log("IP Regocnized and transmitted.");
            transmitNickname();
        } else {
            console.log("Parsed other data: " +e.data + "however ip: " +ip);
        parse(e.data);
        
        if (currIp != ip) {
            //Nothing to do here
        } else {
            switch (currCmd) {
            case "Test":
                    console.log("Got Test Signal. Parser seems to work.");
                break;
            case "CHK_RDY":
                    if(ready){  send(ip+"###rdy"); } else { send(ip+"###notRdy"); }
                break;
            case "attacker":
                $.mobile.changePage("attacker.html");
                break;
            case "defender":
                $.mobile.changePage("defender.html");
                break;
            case "GAME_START":
                    //game start signal
                break;
            case "DISC_CLNT":
                    //kick client
                break;
            case "GAME_PAUSE":
                    //pauses the game
                break;
            case "GAME_RESUME":
                    //resumes the game
                break;
            case "NXT_BLOCK":
                    tickList();
                    break;
            case "gamestart":
                    if(role == 0){ $.mobile.changePage("defender.html"); }
                    else { $.mobile.changePage("attacker.html"); }
                break;
            }
        }
        }
        console.log("message received: " + e.data);
        document.getElementById('connection').innerHTML = '<p>' + e.data + '</p>';
    }
   };

    function prepareSocket(){
        buildHost();
        updateRole();
        
    }

    function send(e) {
        var msg = e;
        sock.send(msg);
    }

    function transmitNickname(){
        console.log("Transmitting command:"+ ip+"###nickname:"+nickname);
        send(ip+"###nickname:"+nickname);
    }
		
    function setIp() {
        wsuri = "ws://" + document.getElementById('ipinput').value + ":55555";
    }
         
    function getIp() {
        document.getElementById('connectto').innerHTML = document.getElementById('ipinput').value;
    }

 function parse(e){
	var count = 0;
    //Split the Array to operate character-wise.
	var splitArr = e.split("");
	
    //Define two arrays
	var ip = [];
    var cmd = [];
	
	for (var i = 0; i < splitArr.length; i++){
		if(splitArr[i] == "#" && count != 3){
            //If we encounter 3 #'s we can assume that the next characters are commando characters
			count +=1;
		} else {
			if (count != 3 && splitArr[i] != "#"){
                //As long as we haven't computed three #, we get a ip address.
				ip.push(splitArr[i]);
			} else {
				if (count == 3 && splitArr[i] != "#"){
                    //If we have parsed 3x #, we can assume we have a cmd.
					cmd.push(splitArr[i]);
				}
			}
		}
	}
    //Compute the character arrays to strings and give it to the current Signals.
     currIp = ip.join("");
     currCmd = cmd.join("");
}

function getNickname(){
     document.getElementById('nick2').innerHTML = document.getElementById('nick').value;
}

function setNickname(){
    nickname = document.getElementById('nick').value;
    console.log("Nickname set as: "+ nickname);
};

function moveLeft(){
    send(ip+"###moveLeft");
};

function moveRight(){
    send(ip+"###moveRight");
};

function ready(){
send(ip+"###nickname:"+rdy);
};

function disconnect(){
 ip = null;
 sock.close();
 $.mobile.changePage("connect.html");
}