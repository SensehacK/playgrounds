import UIKit

/*
 Given the string, check if it is a palindrome.

 Example

     For inputString = "aabaa", the output should be
     checkPalindrome(inputString) = true;
     For inputString = "abac", the output should be
     checkPalindrome(inputString) = false;
     For inputString = "a", the output should be
     checkPalindrome(inputString) = true.

 Input/Output

     [execution time limit] 20 seconds (swift)

     [input] string inputString

     A non-empty string consisting of lowercase characters.

     Guaranteed constraints:
     1 ≤ inputString.length ≤ 105.

     [output] boolean

     true if inputString is a palindrome, false otherwise.

*/


func checkPalindrome(inputString: String) -> Bool {
    
    var isEqual: Bool = false
    var reverseStr = String(inputString.reversed())
    print("Reverse Stringify: \(reverseStr)" )
    
    
    let inputCount = inputString.count - 1
    var string2 = String()
    
    let arrString = Array(inputString)
    
    for i in 0..<inputString.count {
        print("index value \(i)")
        print("Computed value : \(inputCount - i)")

        let char = arrString[inputCount - i]
        print("Character reversed: \(char)")
        string2.append(char)
    }
    
    print("The reversed String:  \(string2)")
    
    print("isEqual \(isEqual)")
    if (string2 == inputString) {
        print("Equal Strings")
        isEqual = true
    }
    return isEqual
}


print(checkPalindrome(inputString: "aabaa"))

print(checkPalindrome(inputString: "Kautilya"))
