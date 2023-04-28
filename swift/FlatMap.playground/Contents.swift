import UIKit

let stringNumber: String? = "5"
let intNumber = stringNumber.map { Int($0) }
print(intNumber)


let flatMapNumber = stringNumber.flatMap { Int($0) }
print(flatMapNumber)

if let flatMapNumber {
    print(flatMapNumber)
}

