/*
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

 

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
Example 4:

Input: nums = [1,3,5,6], target = 0
Output: 0
Example 5:

Input: nums = [1], target = 0
Output: 0
 

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums contains distinct values sorted in ascending order.
-104 <= target <= 104

*/

class Solution {
    func searchInsert(_ nums: [Int], _ target: Int) -> Int {
        
        
        if (target < nums[0]) {
            return 0
        }
        
        for i in 0..<nums.count {
            print("Array number: \(nums[i])" )
            
            if (nums[i] == target) {
                return i
            } else if (nums[i] > target) {
                return i
            }
        }

        return nums.count
    }
}

//let nums = [1,3,5,6], target = 5
//let nums = [1,3,5,6], target = 0
//let nums = [1], target = 0
//let nums = [1,3,5,6], target = 2
let nums = [1,3,5,6], target = 7


Solution().searchInsert(nums, target)
