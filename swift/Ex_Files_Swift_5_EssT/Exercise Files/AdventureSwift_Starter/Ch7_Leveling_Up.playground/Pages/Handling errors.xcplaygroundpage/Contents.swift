/*:
 # Handling Errors
 ---
 
 ## Topic Essentials
 Errors that are thrown from functions need to be handled with a combination of the **try** keyword and a **do-catch** statement. The idea behind this is delegation - where do we want to send out an error and how does it need to be addressed.
 
 ### Objectives
 + Understand error propagation
 + Use the **do-catch** statement to handle errors effectively
 
 [Previous Topic](@previous)
 
 */
// Test code
enum DataError: Error {
    case EmptyPath
    case InvalidPath
}

let playerDataPath = "example/data.txt"
let playerInvalidDataPath = "exampledata.txt"
let playerEmptyDataPath = ""


func loadData(path: String) throws -> Bool {
    guard path.contains("/") else {
        throw DataError.InvalidPath
    }
    
    print(path.isEmpty)
    guard !path.isEmpty else {
        throw DataError.EmptyPath
    }
    
    return true
}

// Do-Catch statements

//try loadData(path: playerDataPath)
//do {
//    try loadData(path: playerDataPath)
//    print("Data Fetch successful")
//} catch is DataError {
//    print("Invalid or empty path")
//} catch {
//    print("Unknown error detected..")
//}


// Trying with if let
if let dataLoaded = try? loadData(path: playerInvalidDataPath) {
    print("The data is loaded properly")
}

// Propagating errors
func propagateDataError() throws {
    try loadData(path: playerEmptyDataPath)
}

do {
    try propagateDataError()
    print("Propagated function fetch success")
} catch DataError.EmptyPath {
    print("empty path")
} catch DataError.InvalidPath {
    print("Invalid path")
} catch {
    print("Unknown error")
}
