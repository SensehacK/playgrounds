//: Playground - noun: a place where people can play

import UIKit

var str = "Hello, playground"


var ten = "10"

var sse : String?
var requiredValue : String


print(ten)
//var optionalInt : Int? = ten.toInt()

//print(sse!)


sse = "A$$"

if let optionalChaining = sse {
    print(optionalChaining)
    print(sse)
}
else {
    print("Couldnt open a optional as it is nil")
}

var optionalInt : Int?

//guard let optChInt = optionalInt else {
//    print("Hello")
//}
