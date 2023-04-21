import UIKit


func fibonacciSequence(n: Int) -> [Int] {
    var result: [Int] = [0,1]
    guard n > 1 else { return result }

    for _ in 0...n-2 {
        let index = result.count
        let sum = result[index - 2] + result.last!
        result.append(sum)
    }
    return result
}



print(fibonacciSequence(n: 5))
// [0,1,1,2,3]
//print(fibonacciSequence(n: 7))
// [0, 1, 1, 2, 3, 5, 8]

//print(fibonacciSequence(n: 0))
//print(fibonacciSequence(n: 1))
//print(fibonacciSequence(n: 2))
//print(fibonacciSequence(n: 0))
//print(fibonacciSequence(n: 9))
//print(fibonacciSequence(n: 5))

func fibonacciNumber(n: Int) -> Int {
    var result: [Int] = [0,1]
    guard n > 1 else { return result[n] }
    
    for _ in 0...n-2 {
        let sum = result[result.count - 2] + result[result.count - 1]
        result.append(sum)
    }
    return result[n]
}

fibonacciNumber(n: 0)
fibonacciNumber(n: 1)
fibonacciNumber(n: 2)
fibonacciNumber(n: 3)
fibonacciNumber(n: 4)
fibonacciNumber(n: 5)
fibonacciNumber(n: 6)
fibonacciNumber(n: 7)
//fibonacciNumber(n: 8)
//fibonacciNumber(n: 9)
