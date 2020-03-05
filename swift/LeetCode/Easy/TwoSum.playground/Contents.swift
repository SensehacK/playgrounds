import UIKit

var numbers = [3,2,4]

func twoSum(_ nums: [Int], _ target: Int) -> [Int] {

    for (index,var value) in nums.enumerated() {
        value = target - value
        for i in index+1...nums.count-1 {
            let value2 = target - nums[i]
            if (target == (value + value2)) {
                return [index,i]
            }
        }
    }
    return []
}

print(twoSum(numbers, 6))


/*
 
 Question :
 
 Given an array of integers, return indices of the two numbers such that they add up to a specific target.

 You may assume that each input would have exactly one solution, and you may not use the same element twice.

 Example:

 Given nums = [2, 7, 11, 15], target = 9,

 Because nums[0] + nums[1] = 2 + 7 = 9,
 return [0, 1].


 Link: https://leetcode.com/problems/two-sum/
 
 Stats
Runtime: 468 ms, faster than 26.55% of Swift online submissions for Two Sum.
Memory Usage: 21 MB, less than 5.88% of Swift online submissions for Two Sum.

 */
