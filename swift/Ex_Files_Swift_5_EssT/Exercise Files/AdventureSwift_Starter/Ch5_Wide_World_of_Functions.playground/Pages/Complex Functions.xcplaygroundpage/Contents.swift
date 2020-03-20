/*:
 # Complex Functions
 ---
 
 ## Topic Essentials
 Functions in Swift can go from simple to complex very quickly with multiple return types, optionals, and even default values.
 
 ### Objectives
 + Create a new function with an optinal return type
 + Create a an overloaded function with two return values
 + Create another overloaded function with two parameters, both with default values
 
 [Previous Topic](@previous)                                                 [Next Topic](@next)

 */
// Optional return value
func setupArenaMatch() -> Bool? {
    return nil
}

if let initSuccess = setupArenaMatch() {
    print("Level initialized: \(initSuccess)")
} else {
    print("Something went terribly wrong...")
}

// Multiple return values
func setupArenaMatch(levelName: String) -> (success: Bool, secretItem: String) {
    print("\(levelName) initialized")
    return (true, "Dinosaur")
}

var levelDetails = setupArenaMatch(levelName: "DoomsDay")
levelDetails.secretItem
levelDetails.success


// Default values
func setupDefaultMatch(levelName: String = "Godly Arena", opponents: Int = 3) {
    print("The match is gonna conduct at \(levelName) with \(opponents) players")
}

setupDefaultMatch()
setupDefaultMatch(levelName: "Heavens Arena", opponents: 5)
