import UIKit
class Solution {
    
    
    func longestCommonPrefix(_ strs: [String]) -> String {
        print("Hello \(strs)")
        var commonStr = ""
        var lowestLength = -1
        var lowestString = ""
//        print("Length of string array \(strs.count)")
        for string in strs {
//            print("String is: " + string)
            let currentCount = string.count
            if lowestLength == -1 {
                lowestLength = currentCount
                lowestString = string
            }
            if lowestLength > currentCount {
                lowestLength = currentCount
                lowestString = string
            }
        }
        
//        print("Lowest String length is \(lowestLength)")
        let lowestStringArr = Array(lowestString)
        
        
        
//        print("Specific character of flower ", strs[0].prefix(2))
        
        
        for i in 0..<lowestLength {
//            print("Printing word by word " + String(lowestStringArr[i]))
            
//            let index = strs.index(strs.startIndex, offsetBy: i)
            
            
//            let mySubstring = currentStr[..<index]
//            print("mysubstring ####### \(mySubstring)")
            
            let lowestBasedChar = String(lowestStringArr[i])
            var isSameChar:Bool = false
            
            
            
            for word in 0..<strs.count {
                let currentStr = strs[word]
                print("Current Word: " + currentStr + " Count " + String(currentStr.count))
                let start = currentStr.index(currentStr.startIndex, offsetBy: i)
                let end = currentStr.index(start, offsetBy: 1)
                let range = start..<end
                let mySubstring = String(currentStr[range])
                print("#### Range:  \(mySubstring)")
                
                
                if (mySubstring == lowestBasedChar) {
                    isSameChar = true
                } else {
                    isSameChar = false
                }
            }
            
            
            if (isSameChar) {
                print("Common Strs: " + commonStr)
                commonStr.append(lowestBasedChar)
            } else {
                break
            }
            
            
//            print("String indexes" strs[1].index(index(i), offsetBy:)
//
//            let startIndex = strs[0].index(strs[0].startIndex, offsetBy: strs.startIndex.advanced(by: 1))
            
            
//            let endIndex = strs[0].strs[0].index(startIndex, offsetBy: <#T##String.IndexDistance#>)
//            let range = strs[0].startIndex ..< strs[0].index(<#T##i: String.Index##String.Index#>, offsetBy: <#T##String.IndexDistance#>)
            
//            print("Specific character of flower ", strs[0].prefix(2))
            
            
            
        }

        
        return commonStr
    }
}

let strArray = ["flower","flow","flight"]
let strArray2 = ["dog","racecar","car"]
let empty = ["", "safa"]
//Solution().longestCommonPrefix(strArray)
Solution().longestCommonPrefix(empty)

