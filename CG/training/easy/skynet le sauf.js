/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/

var road = parseInt(readline()); // the length of the road before the gap.
var gap = parseInt(readline()); // the length of the gap.
var platform = parseInt(readline()); // the length of the landing platform.

var jump = false

while (true) {
    var speed = parseInt(readline()); // the motorbike's speed.
    var coordX = parseInt(readline()); // the position on the road of the motorbike.
    
    if (speed > gap+1){
        print("SLOW")
    }
    
    if (speed <= gap && jump === false){
        print("SPEED")
    }
    
    if (speed == gap+1 && road-coordX>=speed && jump === false){
        print("WAIT")
    }
    
    if (road-coordX<=speed && jump === false){
        print("JUMP")
        jump= true
    }
        
    if (jump === true){
        print("SLOW")
    }
    // To debug: printErr('Debug messages...');
}







    
    