import UIKit

// Array


struct SessionEntry {
    let Id: Int
    let User: String
}

let sessionFields = [
    SessionEntry(Id: 1, User: "Test 1"),
    SessionEntry(Id: 2, User: "Test 2"),
    SessionEntry(Id: 3, User: "Test 3"),
    SessionEntry(Id: 4, User: "Test 4"),
    SessionEntry(Id: 5, User: "Test 5"),
]

let currentID = 6
let result = sessionFields.contains { currentEntry in
    return currentEntry.Id == currentID
}

print(result)
