class Solution {
    func removeElement(_ nums: inout [Int], _ val: Int) -> Int {
        var index = 0
        for i in 0..<nums.count {
            print("Numbers: \(nums[i - index]) index: \(i-index)")
//            if (i == 0) {nums.remove(at: 2)
//                index += 1
//            }
//            nums.remove(at: 2)
//            print(nums[2])
//            print(nums[1])
            if val == nums[i - index] {
                nums.remove(at: i - index)
                index += 1
            }
        }
        for num in nums {
            print("Current number: \(num)")
            if val == num {
//                nums.remove(at: index)
                
            }
        }
        return nums.count
    }
}

var nums = [3,2,2,3], val = 3

Solution().removeElement(&nums, val)
