import UIKit

func mutateTheArray(n: Int, a: [Int]) -> [Int] {
    var arrayB = [Int]()
    
    for(index, item) in a.enumerated() {
        //print("The value \(item) and index \(index) ")
        
        let elementIndexDecrement = index - 1
        let elementIndexIncrement = index + 1
        //print(" Values elementIndexDecrement  \(elementIndexDecrement)  elementIndexIncrement \(elementIndexIncrement) " )
        var sum: Int
        
        let elementDec = elementIndexDecrement >= 0 ? a[elementIndexDecrement] : 0
        let elementInc = elementIndexIncrement < n ? a[elementIndexIncrement] : 0
        //print("###  elementDec  \(elementDec)  elementInc \(elementInc) ")
        sum = elementDec + item + elementInc
        //print("Index \(index)  === Sum \(sum)")
        arrayB.append(sum)
        
    }
    
    return arrayB
}

print(mutateTheArray(n: 5, a: [4, 0, 1, -2, 3]))
