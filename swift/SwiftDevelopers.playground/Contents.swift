//: Playground - noun: a place where people can play

import UIKit

var str = "Hello, playground"



// Remember how we declared the string variable, name?
var name = "Kautilya Save"
var language = "Swift"

// In the next line, declare a variable called language and set it equal to "Swift"

var epiphany = " Then, one day, I discovered \(language)."

print(epiphany)




// Your story 
//On the line below, declare the variable, language, again

//Declare the variable, nobleGoal, again as well

var language1 = "Swift"
var nobleGoal = "To make programming great again"

// Using string interpolation insert the variables, name and nobleGoal into the
// string, end.
var condition = "Then I knew that, programming in \(language1) "
var result = "I could make my dream of \(nobleGoal) a reality."

// Concatenate the variables, condition and result, to create the end of your
// story
var end = condition + result

// Now, on the line below print out the end to your story
print(end)




// String Interpolation


// Plain string
var doggyDiet = "Mia eats 10lbs of dog food per month"

// Define variables
var dogName = "Sia"
var lbsPerMonth: Double = 10

// Same string, this time with the variable inserted
doggyDiet = "\(dogName) eats \(lbsPerMonth)lbs of dog food per month"
print(doggyDiet)

// String interpolation works with expressions too.
let kilosInALb = 0.45
lbsPerMonth = 20
var metricDoggyDiet = "\(dogName) eats \(kilosInALb * lbsPerMonth)kilos of dog food per month"

print(metricDoggyDiet)

dogName = "mafiamf"
lbsPerMonth = 10
metricDoggyDiet = "\(dogName) eats \(kilosInALb * lbsPerMonth)kilos of dog food per month"

print(metricDoggyDiet)










///////




// Create an array of haphazardly chosen words.
var nounArray = ["puppy", "laptop", "ocean", "app", "cow", "skateboard", "developer", "coffee", "moon"]

// Generate random indices to choose words from the array
var index1 = Int(arc4random() % 9)
var index2 = Int(arc4random() % 9)
print("index1  : \(index1)")
print("index2  : \(index2)")

// Insert words into a sensible sentence
var sentence = "The \(nounArray[6]) spilled her \(nounArray[7])."

// Randomly choose words to create a silly sentence
var  sillySentence = "The \(nounArray[index1]) jumped over the \(nounArray[index2])."

// Print out the results!
print(sentence)
print(sillySentence)

var yourSentence = "TODO: Incorporate objects from the noun array here."
yourSentence = "The \(nounArray[0]) was enjoying the \(nounArray[5])"
var yourSillySentence = "TODO: Incorporate randomly chosen objects from the noun array here."

var index3 = Int(arc4random() % 9)
var index4 = Int(arc4random() % 9)
print("index3  : \(index3)")
print("index4  : \(index4)")
var exSillySentence = " The \(nounArray[index3]) stared at the \(nounArray[index4]) "


print(yourSentence)
print(exSillySentence)




//Characters Property 


// The characters property enables us to loop through the characters in a string.
var eString = "Meet me in St. Louis"
for character in eString.characters {
    if character == "e" {
        print("found an e!")
    } else {
    }
}

// The characters property also give us access to properties like count.
var theTruth = "Money can’t buy me love."
var characterCount = theTruth.characters.count
print("characterCount : \(characterCount)")
// It also provides access to functions like reversed()
var forwardString = "spoons"
var charactersReversed = forwardString.characters.reversed()
var backwardsString = String(charactersReversed)

print(backwardsString)



// Create the string, <shoutString> by using the didYouKnowString as a starting point.
// The shoutString should be equivalent to didYouKnowString, but be in ALL CAPS.

// Use a strategy similar to the way we made the whisperString.
var didYouKnowString = "Did you know that the Swift String class comes with lots of useful methods?"
var whisperString = "psst" + ", " + "\(didYouKnowString.lowercased())"
var shoutString = "\(didYouKnowString.uppercased())" + " !!!"

print(whisperString)
print(shoutString)




// Exercise 1

//Reverse the string below and create a new string, called <backwardsString> from the result.

var forwardString1 = "stressed"

var backwardsString1 = String(forwardString1.characters.reversed())

print(backwardsString1)
// Exercise 2
// Write a program that deletes all occurrences of the word "like" in the following string.
// Create a new string, called <noLikes>
var lottaLikes = "If like, you wanna learn Swift like, you should build lots of small apps, cuz it's like, a good way to practice."


print(backwardsString1)

lottaLikes = lottaLikes.replacingOccurrences(of: "like", with: "")
lottaLikes = lottaLikes.replacingOccurrences(of: "  ", with: " ")
var noLikes = lottaLikes.replacingOccurrences(of: " , ", with: " ")

print(noLikes)





var encouragement = "You can do it!"
encouragement = encouragement.replacingOccurrences(of: "can", with: "will")

print(encouragement)

// Use var when assigning a value that is expected to change.
var personalizedEncouragement = "You can do it, Stephanie!"
personalizedEncouragement = personalizedEncouragement.replacingOccurrences(of: "Stephanie", with: "Ryder")

print(personalizedEncouragement)