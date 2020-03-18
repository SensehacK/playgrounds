/*:
 # Chapter Challenge: Game Logic
 ---
 ### Tasks
 1. Create two optional string variable called **lefthandWeapon** and **righthandWeapon**. Assigning them initial values is at your discretion.
 2. Use optional binding to unwrap both optionals in a single statement and debug both outcomes.
 3. Create a dictionary called **playerExp** and assign it some key-value pairs of type string and integer.
 4. Use a `for-in` loop to iterate over **playerExp** and capture the keys and values.
 5. Add a `guard` statement inside the `for-in` loop to make sure each player is at least level 1 to proceed. Don't forget to include the `continue` keyword.
 6. Use a switch statement to define the following cases:
    6a. exp is equal to 32
    6b. exp is between 200 and 500
    6c. Use value binding to store exp and check that it is greater than 500 using the `where` keyword
 
 [Previous Topic](@previous)
 
 */
// 1
var lefthandWeapon: String? = "Shield"
var righthandWeapon: String? = "Sword"

// 2

if let leftWeapon = lefthandWeapon, let rightWeapon = righthandWeapon {
    print("The user has two weapons particularly \(leftWeapon) in their left hand and \(rightWeapon) in their right hand ")
} else {
    print("The user didnt had enough weapons")
}

// 3
var playerExp : [String: Int] = ["Attack": 89, "Defense": 34, "Strategy": 56, "Potion": 13, "Magic": 23]

// 4
for (quality, experience) in playerExp {
    print("This \(quality) quality has \(experience) experience")
}

// 5
var playerProfile : [String: Int] = ["Kautilya": 2, "Sensehack": 3, "Zeus": 1, "KS": 2, "Kay": 0, "Swift": 244]
for (player, playerLevel) in playerProfile {
    guard playerLevel >= 1 else {
        print("The player \(player) is not qualified")
        continue
    }
    print("The player \(player) is qualified")
    
    // 6
    var experience = 270
    experience = playerLevel
    switch experience {
    case 32:
        print("The experience is perfect 32")
    case (200..<500):
        print("The experience is in range of 200 till 500")
    case let experience where experience > 500:
        print("The experience is greater than 500")
    default:
        print("Couldnt find the condition")
    }

}

