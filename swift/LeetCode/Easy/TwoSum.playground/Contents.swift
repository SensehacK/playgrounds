import UIKit

var str = "Hello, playground"
var numbers = [2, 7, 11, 15, 14, 5]
var numbers2 = [2, 11, 15, 14, 5, 9]


func twoSum(_ nums: [Int], _ target: Int) -> [Int] {
    
    var diffArr: [Int] = []
    for num in nums {
        let diff = target - num
        print("Printing diff",diff)
        if (diff>0)  {
            diffArr.append(diff)
        }
        
    }
    
    for value in diffArr {
        
        print("Values of value in diffArr", value)
    }
    let firstNumber = diffArr[0]
    for (index,value) in diffArr.enumerated() {
        print("Values of diffArr", value)
        for (index2, value2) in diffArr.enumerated() {
            print("Adding two values", value2, value, target )
            print("Addition two values", (value2+value), target )
            if (target == (value2+value)) {
                return [index,index2]
            }
        }
    }
    
    return []
}

//print(twoSum(numbers, 9))
print(twoSum(numbers2, 11))
