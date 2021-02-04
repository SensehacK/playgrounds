import UIKit
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public var val: Int
 *     public var next: ListNode?
 *     public init() { self.val = 0; self.next = nil; }
 *     public init(_ val: Int) { self.val = val; self.next = nil; }
 *     public init(_ val: Int, _ next: ListNode?) { self.val = val; self.next = next; }
 * }
 */
public class ListNode {
     public var val: Int
     public var next: ListNode?
     public init() { self.val = 0; self.next = nil; }
     public init(_ val: Int) { self.val = val; self.next = nil; }
     public init(_ val: Int, _ next: ListNode?) { self.val = val; self.next = next; }
}

class Solution {
    func mergeTwoLists(_ l1: ListNode?, _ l2: ListNode?) -> ListNode? {
        var mergedList: ListNode? = ListNode()
        
        if (l1 == nil && l2 == nil) {
            print("Hello")
            return l1 ?? l2
        }
        
        var tempNode = ListNode()
        var mergedArray: [Int] = []
        mergedList?.val = (1)
        
        mergedList?.next = tempNode
        var currentNodeL1 = l1
        var currentNodeL2 = l2
        
        while(currentNodeL1?.val != nil || currentNodeL2?.val != nil) {
            guard let l1Value = currentNodeL1?.val else {
                
                let remainingArray = emptyList(currentNodeL2)
                print("remainingArray  Array1: \(remainingArray)")
                mergedArray.append(contentsOf: remainingArray)
                print("Full Merged Array1: \(mergedArray)")
                return arrayToNode(mergedArray)}
            
            guard let l2Value = currentNodeL2?.val else {
                let remainingArray = emptyList(currentNodeL1)
                mergedArray.append(contentsOf: remainingArray)
                print("Full Merged Array2: \(mergedArray)")
                return arrayToNode(mergedArray)}
            
//            print("Value of currentNodeL1: " + String(currentNodeL1?.val ?? -111))
//            print("Value of currentNodeL2: " + String(currentNodeL2?.val ?? -111))
            
//            print("Value1 guard  \(l1Value)")
//            print("Value2 guard  \(l2Value)")
            
            /*
            if (l1Value < l2Value) {
                if(mergedList?.val == nil) {
                    mergedList?.val = l1Value
                } else {
                    tempNode.val = l1Value
                    mergedList?.next = tempNode
                }
                
            } else if (l1Value == l2Value) {
                tempNode.val = l1Value
                
                mergedList?.val = l1Value
                
            }
            */
            
            
            // Different logic
            if (l1Value < l2Value) {
                mergedArray.append(l1Value)
                currentNodeL1 = currentNodeL1?.next
            } else if (l1Value == l2Value) {
                mergedArray.append(l1Value)
                mergedArray.append(l2Value)
                currentNodeL1 = currentNodeL1?.next
                currentNodeL2 = currentNodeL2?.next
            } else {
                mergedArray.append(l2Value)
                currentNodeL2 = currentNodeL2?.next
            }
                  
            
            // Normal traversing
//            currentNodeL1 = currentNodeL1?.next
//            currentNodeL2 = currentNodeL2?.next
            
            
        }
        
        
        
        
        return arrayToNode(mergedArray)
    }
    
    
    func emptyList(_ currentList: ListNode?) -> [Int] {
        print("Current List " )
        var currentNode = currentList
        var currentListArr: [Int] = []
        while(currentNode?.val != nil) {
            print("Value of empty List \(String(describing: currentNode!.val))")
            let value = currentNode!.val
            if value != 0 {
                currentListArr.append(value)
            }
            currentNode = currentNode?.next
        }
        return currentListArr
    }
    
    func arrayToNode(_ list: [Int]) -> ListNode {
        var lastNode: ListNode
        var mergedArray = list
//        guard let lastItem = mergedArray.popLast() else { return lastNode }
        
        if let lastItem = mergedArray.popLast() {
            lastNode = ListNode(lastItem)
            while(mergedArray.count > 0) {
                let item = mergedArray.popLast()!
                print("Item popped \(item)")
                let temp = ListNode(item, lastNode)
                lastNode = temp
            }
            
            return lastNode
        }
//        lastNode = ListNode(lastItem)
        print("total MergedArray \(mergedArray)")
//        var temp: ListNode?
        
        return ListNode()
    }
    
}


var firstNode = ListNode(5)
var secondNode = ListNode(2, firstNode)
var thirdNode = ListNode(1, secondNode)



var firstNode2 = ListNode(6)
var secondNode2 = ListNode(5, firstNode2)
var thirdNode2 = ListNode(4, secondNode2)



// Class declaration

//Solution().mergeTwoLists(thirdNode, thirdNode2)
//Solution().mergeTwoLists(ListNode(), ListNode())
//Solution().mergeTwoLists(nil, nil)



var firstN = ListNode(3)
var secondN = ListNode(-9, firstN)


var firstN2 = ListNode(7)
var secondN2 = ListNode(5, firstN2)
Solution().mergeTwoLists(secondN, secondN2)
