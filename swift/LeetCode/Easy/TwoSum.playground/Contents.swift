import UIKit

var numbers = [2, 7, 11, 15, 14, 5]


func twoSum(_ nums: [Int], _ target: Int) -> [Int] {
//    var diffArr: [Int] = []
//    for num in nums {
//        let diff = target - num
//        diffArr.append(diff)
//    }
    
    for (index,var value) in nums.enumerated() {
        value = target - value
        for (index2, var value2) in nums.enumerated() {
            value2 = target - value2
            if (target == (value2+value)) {
                return [index,index2]
            }
        }
    }
    return []
}

print(twoSum(numbers, 9))
