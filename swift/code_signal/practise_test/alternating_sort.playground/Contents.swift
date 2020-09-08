import UIKit

import UIKit

func alternatingSort(a: [Int]) -> Bool{
    var arrayB = [Int]()
    var frontIndex = 0
    var backIndex = a.count - 1
    var isFront = true
    var isAscending = true
    print("Length of an arrayA \(backIndex)")
    print("Length of an arrayB \(arrayB.count)")
    
    for(index, item) in a.enumerated() {
        print("The value \(item) and index \(index) ")
        if (arrayB.count != a.count) {
            if (isFront) {
                arrayB.append(a[frontIndex])
                frontIndex += 1
                isFront = false
                print("The isFront:  \(isFront) and frontIndex \(frontIndex) ")
            } else {
                arrayB.append(a[backIndex])
                backIndex -= 1
                isFront = true
                print("The isFront:  \(isFront) and backIndex \(backIndex) ")
            }
        }
        
    }
    
    print("Array B is \(arrayB)")
    
    for i in 1..<arrayB.count {
        print("The front:  \(arrayB[i-1]) and front+1 \(arrayB[i]) ")
        if arrayB[i-1] >= arrayB[i] {
            print("Not ascending ")
            isAscending = false }
    }
    return isAscending
}

//print(alternatingSort(a: [1, 3, 5, 6, 4, 2]))
//print(alternatingSort(a: [1, 4, 5, 6, 3]))

print(alternatingSort(a: [-92, -23, 0, 45, 89, 96, 99, 95, 89, 41, -17, -48]))
