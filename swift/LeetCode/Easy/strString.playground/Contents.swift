/*
 Easy
 
 2152

 2243

 Add to List

 Share
 Implement strStr().

 Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 Clarification:

 What should we return when needle is an empty string? This is a great question to ask during an interview.

 For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

  

 Example 1:

 Input: haystack = "hello", needle = "ll"
 Output: 2
 Example 2:

 Input: haystack = "aaaaa", needle = "bba"
 Output: -1
 Example 3:

 Input: haystack = "", needle = ""
 Output: 0
  

 Constraints:

 0 <= haystack.length, needle.length <= 5 * 104
 haystack and needle consist of only lower-case English characters.
 */


class Solution {
    // First solution trial didn't go well while implementing.
    func strStr(_ haystack: String, _ needle: String) -> Int {
        let count = needle.count
//        for char in haystack {
//            print(char)
//        }
//        print(haystack.contains(needle))
        if (haystack.isEmpty && needle.isEmpty) {
            return 0
        }
        
        if (needle.isEmpty) {
            return 0
        }
        
        if (count > haystack.count) {
                  return -1
              }
        
        let hayArr = Array(haystack)
        let needleArr = Array(needle)
//        print(String(hayArr[2...4]))
        
        var trueCount = 0
        
        for i in 0..<hayArr.count {
            print("Ranges: " + String(hayArr[i]))
            print("TrueCount: \(trueCount)")
            for j in 0..<count {
                if (hayArr[i+j] == needleArr[trueCount]){
                    trueCount += 1
                    print("TrueCount++: \(trueCount)")
                } else {
                    trueCount = 0
                    print("TrueCount Reset: \(trueCount)")
                    break
                }
                if (trueCount == count) {
                    print("i th value: \(i) & trueCount Value: \(trueCount)" )
//                    return i - (trueCount - 1)
                    return i
                }
            }
//            if (hayArr[i] == needleArr[trueCount]){
//                trueCount += 1
//                print("TrueCount++: \(trueCount)")
//            } else {
//                trueCount = 0
//                print("TrueCount Reset: \(trueCount)")
//            }
//
//            if (trueCount == count) {
//                print("i th value: \(i) & trueCount Value: \(trueCount)" )
//                return i - (trueCount - 1)
//            }
        }
        
//        for i in 0..<hayArr.count {
//
//        }

//        for arr in hayArr {
//            print(arr)
//        }

        
        return -1

    }
    
    func strStr2(_ haystack: String, _ needle: String) -> Int {
            let count = needle.count
            if (haystack.isEmpty && needle.isEmpty) {
                return 0
            }
            if (needle.isEmpty) {
                return 0
            }
            if (count > haystack.count) {
                return -1
            }
            
            let hayArr = Array(haystack)
            let needleArr = Array(needle)
            
            var trueCount = 0
            
            for i in 0..<hayArr.count {
                if (i+count <= hayArr.count) {
                    print("I + Count \(i+count)")
                    for j in 0..<count {
                        let current = i+j
                        if (current > hayArr.count) {
                            print("Greater than current")
                        }
                        if (hayArr[i+j] == needleArr[trueCount]){
                            trueCount += 1
                        } else {
                            trueCount = 0
                            break
                        }
                        if (trueCount == count) {
                            print("i th value: \(i) & trueCount Value: \(trueCount)")
                            return i
                        }
                    }
                }
                
            }
            return -1
        }
        
    
}

//var haystack = "heelllo", needle = "lll"
//var haystack = "a", needle = ""
//var haystack = "", needle = "a"
//var haystack = "mississippi", needle = "issip"
//var haystack = "mississippi", needle = "issipi"
//var haystack = "aaa", needle = "aaaa"
var haystack = "a", needle = "a"
//Solution().strStr(haystack, needle)
Solution().strStr2(haystack, needle)
