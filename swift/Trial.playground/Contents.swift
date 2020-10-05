//: Playground - noun: a place where people can play

import UIKit

var str = "Hello, playground"

var name1 = "Kautilya"


//for i in name1.characters {
//    print(i)
//}

for i in 1...5 {
    print(i)
}


var apples = 12
var lemons = 13

var willEat = (apples == lemons) ? true : false

if apples == lemons {
    print("We love fruits")
    
}
else {
    print("We Hate fruits")
}

// Range inclusive & exclusive
print("rangeInclusive")
for i in 1..<3 {
    print(i)
}

print("rangeExclusive")

for i in 1...3 {
    print(i)
}
