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
    $('ul').append('<li>'+queue[i]+'</li>').listview('refresh');
    }
};

function tickList(){
    var next = queue.shift();
    switch(next){
        case "I-Shape":
            send(ip+"###I");
            break;
        case "Circle":
            send(ip+"###Circle");
            break;
        case "L-Shape":
            send(ip+"###L");
            break;
        case "Inv-L-Shape":
            send(ip+"###InvL");
            break;
        case "S-Shape":
            send(ip+"###S");
            break;
        case "Z-Shape":
            send(ip+"###Z");
            break;
        case "T-Shape":
            send(ip+"###T");
    }
    updateQueueList();
    document.getElementById('nextblock').innerHTML = next;
};