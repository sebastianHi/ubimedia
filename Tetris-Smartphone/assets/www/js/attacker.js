//Initialize Queue
var queue = [];

function addI(){
    addToQueue("I-Shape");
};

function addCircle(){
    addToQueue("Circle");
};

function addL(){
    addToQueue("L-Shape");
};

function addInvL(){
    addToQueue("Inv-L-Shape");   
};

function addS(){
    addToQueue("S-Shape");
};

function addZ(){
    addToQueue("Z-Shape");
};

function addT(){
    addToQueue("T-Shape");
};

function addToQueue (item){
    queue.push(item);
    console.log("Pushed " + item + " to Queue.");
    updateQueueList();
};

function updateQueueList(){
    //This is where da magic happens.
    //Powered by Erdinger Weißbier
    //'n Shit!
     $('ul').empty();
    for(var i = (queue.length)-1; i >= 0; i--){
    $('ul').append('<li>'+'<br>'+'<img src='+'"'+'img/'+queue[i]+'.png"'+'</li>').listview('refresh');
    }
};

function tickList(){
    var next = queue.shift();
    console.log("Shifted Next Element, which is: "+next);
    switch(next){
        case "I-Shape":
            send(ip+"###I");
            console.log("Sending Signal to Server.");
            break;
        case "Circle":
            send(ip+"###cube");
            console.log("Sending Signal to Server.");
            break;
        case "L-Shape":
            send(ip+"###L");
            console.log("Sending Signal to Server.");
            break;
        case "Inv-L-Shape":
            send(ip+"###reverseL");
            console.log("Sending Signal to Server.");
            break;
        case "S-Shape":
            send(ip+"###reverseZ");
            console.log("Sending Signal to Server.");
            break;
        case "Z-Shape":
            send(ip+"###Z");
            console.log("Sending Signal to Server.");
            break;
        case "T-Shape":
            console.log("Sending Signal to Server.");
            send(ip+"###cross");
        
    }
    updateQueueList();
    document.getElementById('nextblock').innerHTML = '<img src="'+'img/'+next+'.png">';
};

function checkLength(){
if(queue.length > 4){
//Disable all Buttons while Queue is bigger than 5
    $('#bt1').addClass('ui-disabled');
    $('#bt2').addClass('ui-disabled');
    $('#bt3').addClass('ui-disabled');
    $('#bt4').addClass('ui-disabled');
    $('#bt5').addClass('ui-disabled');
    $('#bt6').addClass('ui-disabled');
    $('#bt7').addClass('ui-disabled');
} else { 
    $('#bt1').removeClass('ui-disabled');
    $('#bt2').removeClass('ui-disabled');
    $('#bt3').removeClass('ui-disabled');
    $('#bt4').removeClass('ui-disabled');
    $('#bt5').removeClass('ui-disabled');
    $('#bt6').removeClass('ui-disabled');
    $('#bt7').removeClass('ui-disabled');
}
};

function inverseControl(){
    send(ip+"###inverseControl");
};

function leftFreeze(){
    send(ip+"###freezeRight");
};

function rightFreeze(){
    send(ip+"###freezeLeft");
};

function rotateFreeze(){
    send(ip+"###freezeRotate");
};

function speedUp(){
    send(ip+"###speedUp");
};

function invisBlock(){
    send(ip+"###makeBlockInvisible");
};

function noPoints(){
    send(ip+"###noPoints");
};

function superBlock(){
    send(ip+"###orderSuperBlock");
};

function rainOfBlocks(){
    send(ip+"###orderRainOfBlocks");
};

function callThunder(){
    send(ip+"###orderThunder");
};