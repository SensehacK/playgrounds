import UIKit


let dict = [String: Int]()

let dict2: [String: Int] = [
        "Kautilya": 0,
        "Zeus": 1,
        "Sensehack": 2,
]

let dict3: [String: Int]?

var initProtocol = [String : Int]()
initProtocol["one"] = 1
initProtocol["two"] = 2

let someProtocol = [
    "one" : 4,
    "two" : 3
]

initProtocol["one"]
someProtocol.count
//
//for (key, val) in someProtocol {
//    print("Keys: \(key)")
//    print("Values: \(val)")
//}


//for keyVal in dict2.enumerated() {
//    //print(keyVal.offset)
//    //print(keyVal.element)
//    // 0
//    // (key: "Zeus", value: 1)
//}

//for (key, Val) in dict2.enumerated() {
//    print(key)
//    print(Val.key)
//    print(Val.value)
//}


let names: Set = ["Sofia", "Camilla", "Martina", "Mateo", "Nicolás"]
var shorterIndices: [Set<String>.Index] = []
for (i, name) in zip(names.indices, names) {
    if name.count <= 5 {
        print(name)
        shorterIndices.append(i)
    }
}



// Hash Map
func hashTable()  {
        let numbers = [1,4,5,3,3,12,3,5,3,3,6,7,1,2]
        var hashMap = [Int: Int]()
        
        for number in numbers {
            if (hashMap[number] != nil) {
                hashMap[number]! += 1
            } else {
                hashMap[number] = 1
            }
        }
        
//        hashMap
        
        
        for (keys, values) in hashMap {
            print("\(keys): \(values)")
        }
    }
