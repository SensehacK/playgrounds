//: Playground - noun: a place where people can play

import UIKit

var str = "Hello, SensehacK."
print(str)

enum Step {
    case Left , Right , Up , Down
}
var map = (0,0)

/*
A step .Up will increase the y coordinate by 1.
A step .Down will decrease the y coordinate by 1.
A step .Right will increase the x coordinate by 1
A step .Left will decrease the x coordinate by 1.
*/

func move ( string : String) {

        var step = Step.Left

            switch string {
            case "left" :
                step = Step.Left
            
            case "right" :
                step = Step.Right
            
            case "up" :
                step = Step.Up
            
            case "down" :
                step = Step.Down

            default :
                print("Please enter proper command")
            }
    
            //print(step)
            switch step {
                
            case .Left :
                map.0 -= 1
                
            case .Right :
                map.0 += 1

            case .Up :
                map.1 += 1
                
             case .Down :
                map.1 -= 1
            }
}


func playerMoves () {
    
        move(string: "left")
        move(string: "left")
        move(string: "right")
        move(string: "right")
        move(string: "up")
        move(string: "up")
        move(string: "down")
        move(string: "right")
        move(string: "down")
        move(string: "down")
        move(string: "right")
        move(string: "up")
        move(string: "up")
        move(string: "left")
        move(string: "up")
        move(string: "left")
        move(string: "up")
        move(string: "up")
        move(string: "down")
        move(string: "down")
        move(string: "up")
        move(string: "up")
        move(string: "left")
        move(string: "up")
        move(string: "down")
        move(string: "left")
        move(string: "up")
        move(string: "up")
        move(string: "down")
        move(string: "down")
        move(string: "down")
        move(string: "left")
        move(string: "up")
        move(string: "right")
        move(string: "left")
        move(string: "down")
        move(string: "left")
        move(string: "up")
        move(string: "left")
    
}
//Calling Everthing
playerMoves()
print("The co ordinates of the User in the game are X,Y : \(map.0) ,\(map.1)")