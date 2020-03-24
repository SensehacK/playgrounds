/*:
 # Swift Enumerations
 ---
 
 ## Topic Essentials
 Swift enumerations allow you to put related values together into a group that you can use and access. Like switch statements, each value in an enum is considered a different case, which is one of the many reasons they go so well together.
 
 ### Objectives
 + Declare a basic enum called **GameState**
 + Store an enum case as a variable and print out its value
 + Use a switch statement to define actions for each enum case
 + Understand default cases and the **@unknown** keyword
 
 [Next Topic](@next)
 
 */
// Declaring an enum
enum GameState {
    case Completed
    case Initialized
    case Loading
    case Downloading
}

// Storing and switching on an enum value

var currentState = GameState.Initialized
print("Current state is \(currentState)")

switch currentState {
case .Completed:
    print("The game is completed..")
case .Initialized:
    print("the game is initialized")
case .Loading:
    print("The game is been loaded..")
@unknown default:
    print("Unknown case added")
}
