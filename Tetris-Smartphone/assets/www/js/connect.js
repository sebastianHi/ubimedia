var sock = null;
var wsuri = "ws://localhost:9000";
var ip = null;

function buildHost() {
    sock = new WebSocket(wsuri);
    
    sock.onopen = function () {
        console.log("connected to " + wsuri);
        send("Test");
    };
    sock.onclose = function (e) {
        console.log("connection closed (" + e.code + ")");
        document.getElementById('connection').innerHTML += '<br>connection closed (' + e.code + ')';
       
    };
    sock.onmessage = function (e) {
        //Decide how the incomming message is interpreted
        //We use an generic simple parser to decode the message
        //The messages are composed in the following scheme:
        // "IP###COMMAND", e.g. "192.168.0.2###Test".
        
        var {currIP, currCmd} = parse(e.data);
        
        if (currIP != ip){
        //do nothing, as this cmd does not concern us
        }else{
            switch(currCmd) {
                case "Test":
                    //test cmd
                    break;
                case "SWP_POS":
                    //change team-role
                    break;
                case "CHK_RDY":
                    //Ready-Check
                    break;
                case "SWP_TEAM":
                    //swap team
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
            }
        
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

function parse(e) {
    //Get us some basic variables for iteration
    //The messages are composed in the following scheme:
    // "IP###COMMAND", e.g. "192.168.0.2###Test".
    var count = 0;
    //Split our Message in pieces
    var splitArr=e.split("");
    //our current cmd states
    var ip = "";
    var cmd = "";
    
    //Iterate through code Array and grab the cmds
    for (var i = 0; i < splitArr.length; i++) {
           if (splitArr[i] == "#" && count != 3){
               //if we have a #, then we need to count to 3 before we can assume to interpret a cmd
                count += 1;
            } else {
        if (count =! 3 && splitArr[i] != "#") {
            ip.concat(splitArr[i]);
        } else {
        if (count == 3 && splitArr[i] != "#") {
            cmd.concat(splitArr[i]); 
        } 
    }
    return {currIp: ip, currCmd: cmd};           
}
