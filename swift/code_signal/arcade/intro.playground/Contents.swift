import UIKit

var str = "Hello, playground"
/*
 Write a function that returns the sum of two numbers.

 Example

 For param1 = 1 and param2 = 2, the output should be
 add(param1, param2) = 3.

 Input/Output

     [execution time limit] 20 seconds (swift)

     [input] integer param1

     Guaranteed constraints:
     -1000 ≤ param1 ≤ 1000.

     [input] integer param2

     Guaranteed constraints:
     -1000 ≤ param2 ≤ 1000.

     [output] integer

     The sum of the two inputs.
*/


func add(param1: Int, param2: Int) -> Int {
    return param1 + param2
}

//print(add(param1: 3, param2: 7))


/*
 

 
 */

func centuryFromYear(year: Int) -> Int {
    print(year / 100)
    
    print(year / 100 + 1)
    // VS
    print((year + 99) / 100)


    return (year + 99) / 100
}
//print(centuryFromYear(year: 1992))
//
//print(centuryFromYear(year: 92))
//print(centuryFromYear(year: 792))
//
//print(centuryFromYear(year: 700))




