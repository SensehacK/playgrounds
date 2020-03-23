/*:
 # Chaining Optionals
 ---
 
 ## Topic Essentials
 Optional chaining allows you to unwrap an optional type that has optional properties of its own. This is most common in classes or structs that contain optional custom types. It’s handy to think of optional chains in a very literal sense, like a chain link. If all the links are present and strong, the chain continues, but if one link fails, the chain breaks.
 
 ### Objectives
 + 
 
 [Previous Topic](@previous)                                                 [Next Topic](@next)

 */
// Test classes
struct Item {
    var description: String
    var previousOwner: Owner?
}

struct Owner {
    var name: String
    
    func returnOwnerInfo() -> String {
        return "\(name) is the current owner"
    }
}

var questDirectory = [
    "Fetch Gemstones": [
        "Objective": "Retrieve 5 gemstones",
        "Secret": "Complete in under 5 minutes"
    ],
    "Defeat Big Boss": [
        "Objective": "Beat the ultimate boss",
        "Secret": "Win with 50% health left"
    ]
]

// Creating the chain
var rareDagger = Item(description: "Unique dagger", previousOwner: nil)

var ownerName = Owner(name: "Kautilya")

rareDagger.previousOwner = ownerName
// Object needs to be initialized to work for optionals to go through next property : ?.name



if let owner = rareDagger.previousOwner?.name {
    print("The item used to be owned by \(owner)")
} else {
    print("The items history is not known")
}

rareDagger.previousOwner?.name = "Sensehack"

if let ownerInfo = rareDagger.previousOwner?.returnOwnerInfo() {
    print(ownerInfo)
} else {
    print("The owner is no where to be found.")
}


// Optional unwrapping dictionary

if let gemstoneObjective = questDirectory["Fetch Gemstones"]?["Objective"] {
    print(type(of: gemstoneObjective))
    print(gemstoneObjective)
    // Only if we wanted to directly get the object and then force unwrap optionals
//    print(gemstoneObjective["Objective"])
} else {
    print("No gemstones objective found")
}
