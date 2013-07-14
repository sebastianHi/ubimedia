//The Coordinate IDs
    var xacc = 0;
    var yacc = 0;

// The watch id references the current `watchAcceleration`
    var watchID = null;

    // Wait for Cordova to load
    //
    document.addEventListener("deviceready", onDeviceReady, false);

    // Cordova is ready
    //
    function onDeviceReady() {
        //....
    }

    // Start watching the acceleration
    //
    function startWatch() {

        // Update acceleration every 3 seconds
        var options = { frequency: 100 };

        watchID = navigator.accelerometer.watchAcceleration(onSuccess, onError, options);
    }

    // Stop watching the acceleration
    //
    function stopWatch() {
        if (watchID) {
            navigator.accelerometer.clearWatch(watchID);
            watchID = null;
        }
    }

    // onSuccess: Get a snapshot of the current acceleration
    //
    function onSuccess(acceleration) {
        xacc = acceleration.x;
        yacc = acceleration.y;
        
        if(yacc<(-4)){
            send(ip+"###RotateL");
        } else {
            if(yacc>4){
            send(ip+"###RotateR");
            } else { }
        }
        
    }

    // onError: Failed to get the acceleration
    //
    function onError() {
        alert('onError!');
    }

function skipBlock(){
    send(ip+"###skipBlock");
};

function slowPace(){
    send(ip+"###slowPace");
};

function bomb(){
    send(ip+"###orderBomb");
};

function reduceTime(){
    send(ip+"###reduceTime");
};