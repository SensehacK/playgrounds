/*:
 # Raw and Associated Values
 ---
 
 ## Topic Essentials
 Enumerations can be expanded to include raw values, which can store unique or sequential values, or associated values, which can capture case specific parameters for use in their respective code blocks.
 
 ### Objectives
 + Declare an enum with a raw value
 + Declare an enum with associated values
 + Add a method inside the enum to execute a switch statement for each case
 
 [Previous Topic](@previous)                                                 [Next Topic](@next)

 */
// Raw values
enum NPCs: String {
    case Village = "Not much useful for game"
    case Blacksmith = "Gives all of the quest info"
    case Merchant = "Unlimited number of users"
}


var blacksmith = NPCs.Blacksmith
print(blacksmith.rawValue)



// Associated values

enum PlayerState {
    case Alive
    case KO(level: Int)
    case Unknown(debugError: String)
    
    func evaluateState() {
        switch self {
        case .Alive:
            print("The player is kicking")
        case .KO(let restartLevel):
            print("Game Over! Back to level \(restartLevel)")
        case .Unknown(let errorStrg):
            print(errorStrg)
            
        default :
            print("Unknown state encountered")
        }
    }
}


PlayerState.KO(level: 3).evaluateState()
