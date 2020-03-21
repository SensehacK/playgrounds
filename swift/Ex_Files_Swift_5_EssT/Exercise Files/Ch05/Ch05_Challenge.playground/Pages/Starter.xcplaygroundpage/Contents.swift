/*:
 # Chapter Challenge: Battle Grounds
 ---
 
 ### Tasks
 1. Create a type alias tuple called **Attack** with named values for name and damage
 2. Write a simple function called **attackEnemy** with an integer parameter that prints out an interpolated string
 3. Write an overloaded version of **attackEnemy** with a parameter of type Attack that returns an string
 4. Use both **attackEnemy** methods
 5. Create a type alias closure called **AttackClosure** that takes in an array of Attacks and returns void, then declare a test array of Attack values.
 6. Write a function called **fetchPlayerAttacks** that has a closure parameter of type AttackClosure and no return value
 7. Call **fetchPlayerAttacks** and loop through the array inside the closure body to print out its tuple values
 
 [Previous Topic](@previous)
 
 */
// 1
typealias Attack = (name: String, damage: Int)

// 2
func attackEnemy(damage: Int) {
    print("The damage is \(damage)")
}

// 3
func attackEnemy(attack: Attack) {
    print("The attacker name is \(attack.name) and damage is \(attack.damage)")
}

// 4
attackEnemy(damage: 24)
attackEnemy(attack: Attack("Red Haired Shanks", 10000))

// 5
var attacks = [
    Attack("Sasuke", 89),
    Attack("Naruto", 95)
]
typealias AttackClosure = ([Attack]) -> Void


// 6
func fetchPlayerAttacks(completion: AttackClosure) {
    completion(attacks)
}

// 7

fetchPlayerAttacks { (attacks) in
    for attack in attacks {
        print("The person attacking is \(attack.name) and his damage is \(attack.damage)")
    }
}

