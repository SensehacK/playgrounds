/*:
 # Understanding Closures
 ---
 
 ## Topic Essentials
 Like functions, closures are enclosed blocks of functionality but with more concise syntax. In Swift closures act like blocks or lambda expressions in other programming languages, allowing us to pass function-like operations around like variables.
 
 ### Objectives
 + Write an empty closure declaration
 + Create a closure that takes in an `Int` parameter and returns an `Int` value
 + Update the closure to use type inference and shorthand
 
 [Previous Topic](@previous)                                                 [Next Topic](@next)

 */
// Defining closures
var closure:() -> () = {}

// Initializing closures
var computeBonusDamage: (Int) -> Int = { (base: Int) -> Int in
    return base * 4
}

// Type inference
var computeBonusDamagev2 = { (base: Int) -> Int in
    return base * 4
}

// Advanced Type Inference
var computeBonusDamagev3 = { base in
    return base * 4
}

computeBonusDamage(25)
computeBonusDamagev2(20)
computeBonusDamagev3(30)
