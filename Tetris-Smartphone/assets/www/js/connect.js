var sock = null;
var wsuri = "ws://localhost:9000";
var ip = null;
var currIP = null;
var currCmd = null;
var nickname = null;
var readyvalue = false;

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
            case "attacker":
                $.mobile.changePage("attacker.html");
                break;
            case "defender":
                $.mobile.changePage("defender.html");
                startWatch();
                break;
            case "GAME_START":
                    //game start signal
                break;
            case "DISC_CLNT":
                    //kick client
                break;
            case "dropBlock":
                    console.log("TickList. Proceed.");
                    tickList();    
                break;
            case "GAME_PAUSE":
                    //pauses the game
                break;
            case "cube":
                document.getElementById('CurrBlock').innerHTML = '<img src="img/Circle.png">';    
                break;
            case "I":
                document.getElementById('CurrBlock').innerHTML = '<img src="img/I-Shape.png">';
                break;
            case "L":
                document.getElementById('CurrBlock').innerHTML = '<img src="img/L-Shape.png">';
                break;
            case "reverseL":
                document.getElementById('CurrBlock').innerHTML = '<img src="img/Inv-L-Shape.png">';
                break;
            case "reverseZ":
                document.getElementById('CurrBlock').innerHTML = '<img src="img/S-Shape.png">';
                break;
            case "Z":
                document.getElementById('CurrBlock').innerHTML = '<img src="img/Z-Shape.png">';
                break;
            case "cross":
                document.getElementById('CurrBlock').innerHTML = '<img src="img/T-Shape.png">';
                break;
            case "notRdy":
                resetReady();
                break;
            case "NXT_BLOCK":
                    tickList();
                    break;
            case "unlockRightFreeze":
                    $('#frzRight').removeClass('ui-disabled');
                    break;
            case "unlockLeftFreeze":
                    $('#frzLeft').removeClass('ui-disabled');
                    break;
            case "unlockRotateFreeze":
                    $('#frzRotate').removeClass('ui-disabled');
                    break;
            case "unlockNoPoints":
                    $('#noPts').removeClass('ui-disabled');
                    break;
            case "unlockInverseControl":
                    $('#invControl').removeClass('ui-disabled');
                    break;
            case "unlockBlockInvisible":
                    $('#invBlock').removeClass('ui-disabled');
                    break;
            case "unlockSpeedUp":
                    $('#spdUp').removeClass('ui-disabled');
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
        
    }

    function send(e) {
        var msg = e;
        sock.send(msg);
    }

    function transmitNickname(){
        console.log("Transmitting command:"+ ip+"###nickname:"+nickname);
        if(nickname.length > 10){
            nickname = nickname.substr(0,10);
        }
        if(nickname.length == 0){
            nickname = "Anonymous"
        }
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
};

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
    $('#readybutton').addClass('ui-disabled');
    send(ip+"###rdy");
    readyvalue = true;
    console.log("sent ready.");
};

function disconnect(){
 send(ip+"###disconnect"); 
 ip = null;
 sock.close();
 $.mobile.changePage("connect.html");
};

function softDrop(){
    send(ip+"###speedDown");
};

function resetReady(){
    $('#readybutton').removeClass('ui-disabled');
    readyvalue = false;
    console.log("Reversed ready.");
}