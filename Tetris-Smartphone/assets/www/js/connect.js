//Socket initialisierung... Sorry fürs Denglisch xD
var sock = null;
var wsuri = "ws://localhost:9000";
var ip = null;
var currIP = null;
var currCmd = null;
var nickname = null;
var readyvalue = false;
var invControlUnlocked, leftFreezeUnlocked, rightFreezeUnlocked, rotateFreezeUnlocked, speedUPUnlocked, invisBlockUnlocked, noPointsUnlocked = false;
var solo = false;

//Bau den Host auf
function buildHost() {
    sock = new WebSocket(wsuri);
    
    sock.onopen = function () {
        console.log("connected to " + wsuri);
    };
    sock.onclose = function (e) {
        console.log("connection closed (" + e.code + ")");
        document.getElementById('connection').innerHTML += '<p>connection closed (' + e.code + ')';
        ip = null;
        $.mobile.changePage("connect.html");
       
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
        parse(e.data);
        
        if (currIp != ip) {
            //Nothing to do here
        } else {
            switch (currCmd) {
            case "Test":
                    console.log("Got Test Signal. Parser seems to work.");
                break;
            case "attacker":
                //Signal für Attacker, wenn 1vs1vs1 dann haben Spezials Cooldowns
                solo = false;
                $.mobile.changePage("attacker.html");
                break;
            case "defender":
                //Defender
                $.mobile.changePage("defender.html");
                startWatch();
                break;
            case "DISC_CLNT":
                    disconnect();
                break;
            case "dropBlock":
                    console.log("TickList. Proceed.");
                    tickList();    
                break;
            //Erkennung der cubes
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
            //Not ready signal
            case "notRdy":
                resetReady();
                break;
            //Spiel beenden
            case "gameEnds":
                disconnect();    
                break;
            //Nächster Block angefordert
            case "NXT_BLOCK":
                tickList();
                break;
            //Falls 1vs1vs1
            case "attackerSolo":
                solo = true;
                $.mobile.changePage("attacker.html");
                break;
            //Skill unlocks
            case "unlockRightFreeze":
                console.log("Skill unlocked!");
                if(kuhldown){ } else { unlockFreezeRight(); }
                rightFreezeUnlocked = true;
                break;
            case "unlockLeftFreeze":
                console.log("Skill unlocked!");
                if(kuhldown){ } else { unlockFreezeLeft(); }
                leftFreezeUnlocked = true;
                break;
            case "unlockRotateFreeze":
                console.log("Skill unlocked!");
                if(kuhldown){ } else { unlockFreezeRotate(); }
                rotateFreezeUnlocked = true;
                break;
            case "unlockNoPoints":
                console.log("Skill unlocked!");
                if(kuhldown){ } else { unlockNoPts(); }
                noPointsUnlocked = true;
                break;
            case "unlockInverseControl":
                console.log("Skill unlocked!");
                if(kuhldown){ } else { unlockInvControl(); }
                invControlUnlocked = true;
                break;
            case "unlockBlockInvisible":
                console.log("Skill unlocked!");
                if(kuhldown){ } else { unlockInvisBlock(); }
                invisBlockUnlocked = true;
                break;
            case "unlockSpeedUp":
                console.log("Skill unlocked!");
                if(kuhldown){ } else { unlockSpdUp(); }
                speedUPUnlocked = true;
                break;
            }
        }
        }
        console.log("message received: " + e.data);
        document.getElementById('connection').innerHTML = '<p>' + e.data + '</p>';
    }
   };
    //Socket bauen
    function prepareSocket(){
        buildHost();
        
    }
    //Socket send
    function send(e) {
        var msg = e;
        sock.send(msg);
    }
    //Transmit nickname
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
    //Set IP
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
//Get nickname
function getNickname(){
     document.getElementById('nick2').innerHTML = document.getElementById('nick').value;
};
//Set nickname
function setNickname(){
    nickname = document.getElementById('nick').value;
    console.log("Nickname set as: "+ nickname);
};
//Bewegungen
function moveLeft(){
    send(ip+"###moveLeft");
};

function moveRight(){
    send(ip+"###moveRight");
};
//Ready fuer loby
function ready(){
    $('#readybutton').addClass('ui-disabled');
    send(ip+"###rdy");
    readyvalue = true;
    console.log("sent ready.");
};
//Disconnect 
function disconnect(){
 send(ip+"###disconnect"); 
 ip = null;
 sock.close();
 $.mobile.changePage("connect.html");
};
//Soft Drop, steine nach unten fallen
function softDrop(){
    send(ip+"###speedDown");
};
//Setze Ready zurück
function resetReady(){
    $('#readybutton').removeClass('ui-disabled');
    readyvalue = false;
    console.log("Reversed ready.");
}