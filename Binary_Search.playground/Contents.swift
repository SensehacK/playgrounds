import UIKit

var str = "Hello Sensehack!"

/* Algorithm
function binary_search(A, n, T):
L := 0
R := n − 1
while L <= R:
m := floor((L + R) / 2)
if A[m] < T:
L := m + 1
else if A[m] > T:
R := m - 1
else:
return m
return unsuccessful
*/

// Defining the Array Data which is presumed to be sorted.
var ArrayData: [Int] =  [1,2,4,5,8,9,24];

// Function accepting 3 parameters
func binary_search(ArrayD: [Int], key: Int, length: Int) -> Int{
    var LowerBound = 0;
    var HigherBound = length - 1;
    print(LowerBound, HigherBound)
    while LowerBound <= HigherBound {
        let medium = (LowerBound + HigherBound) / 2;
        print("Medium ",medium)
        print("Key", key)
        print("Variable checking at Array" , ArrayD[medium])
        if (ArrayD[medium]) < key {
            LowerBound = medium + 1;
        }
        else if (ArrayD[medium]) > key {
            HigherBound = medium - 1;
        }
        if ((ArrayD[medium]) == key) {
            return medium;
        }
    }
    // Return unsuccessful
    return 0;
}

// Calling of Function Binary search
print("Binary search for the given array",binary_search(ArrayD: ArrayData, key: 9, length: ArrayData.count));
