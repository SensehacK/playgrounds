import UIKit

struct Calculator {
    static func calculateGamesPlayed() -> Int {
        var games: [Int] = []
        for i in 1...4_000 { games.append(i) }
        return games.last!
    }
}

struct Player {
    
    var name: String
    var team: String
    var position: String
    
    // Property but ran only once.
    lazy var gamesPlayed = {
        return Calculator.calculateGamesPlayed()
    }()
    
    // Computed property
    var gamesPlayed2:Int {
        return Calculator.calculateGamesPlayed()
    }
    
    lazy var introduction = {
        return "Now entering the game: \(name), \(position) for the \(team)"
    }()
    
    
}

// Having lazy property won't initialize on every object creation.
var jordan = Player(name: "Michael Jordan", team: "Bulls", position: "Shooting Guard")
var jordan2 = Player(name: "Michael Jordan", team: "Bulls", position: "Shooting Guard")
var jordan3 = Player(name: "Michael Jordan", team: "Bulls", position: "Shooting Guard")
var jordan4 = Player(name: "Michael Jordan", team: "Bulls", position: "Shooting Guard")
var jordan5 = Player(name: "Michael Jordan", team: "Bulls", position: "Shooting Guard")

// Will only initialize when the object references the property.
print(jordan.gamesPlayed)
print(jordan.gamesPlayed)
print(jordan.gamesPlayed)


// If computed property it won't store the computation, it will again compute the property everytime it gets called. Could get really expensive if we are referencing something more than once and if no data has changed leads to wasted computing cycles.
print(jordan.gamesPlayed2)
print(jordan.gamesPlayed2)
print(jordan.gamesPlayed2)


print(jordan2.gamesPlayed)
print(jordan3.gamesPlayed)
print(jordan4.gamesPlayed)
