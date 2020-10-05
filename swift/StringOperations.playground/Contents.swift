//: Playground - noun: a place where people can play

import UIKit

var str = "Hello, playground"
var str1 = "Kautilya"

//str1.reversed()
var char = str1.characters
var rstr1 = char.reversed()

print(str1)
print(String(rstr1))
print(String(str.characters.reversed()))


// cases
print("Lowercase Name : \(str1.lowercased())"  )
print("UpperCase Name : \(str1.uppercased())"  )

//Count for str1
print("Count of \(str1) : \(str1.characters.count)")


if (str.range(of: "ell") != nil) {
    print("Yes it does have Hello")
}

//Prefix variables
if str1.hasPrefix("Ka") {
    print("Yes, there is")
}
else {
    print("Error!")
}


// Type printing for easy debugging.
let a = 1
print(type(of: a))
print("Hlello")

let b = "1"
print(type(of: b))
print("Hlelbbblo")

let c = 1.02
print(type(of: c))
print("Hlelbsafcbblo")

print(type(of:"Hello"))





let exampleString = "Example string"

//Solution suggested above in Swift 3.0
let stringToArray = exampleString.components(separatedBy: " ")
print(type(of : stringToArray))
let stringFromArray = stringToArray.joined(separator: "+")

//Swiftiest solution
let swiftyString = exampleString.replacingOccurrences(of: " ", with: "+")



