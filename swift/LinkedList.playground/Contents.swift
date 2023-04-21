// https://medium.com/geekculture/linked-lists-in-swift-5-69ba9748f4b6
// https://www.youtube.com/watch?v=oLXRe7JWJ5g

// Linked List in Swift



class Node<T> {

    var value: T
    var next: Node<T>?

    init(value: T, next: Node<T>? = nil) {
        self.value = value
        self.next = next
    }
}


struct LinkedList<T> {
 
  var head: Node<T>?
  var tail: Node<T>?
  
  var isEmpty: Bool { head == nil }
  
  init() {}
    
  mutating func push(_ value: T) {
          head = Node(value: value, next: head)

          if tail == nil {
              tail = head
          }
  }
    
  mutating func append(_ value: T) {
      let node = Node(value: value)

      tail?.next = node
      tail = node
  }

  func node(at index: Int) -> Node<T>? {
        var currentIndex = 0
        var currentNode = head

        while currentNode != nil && currentIndex < index {
            currentNode = currentNode?.next
            currentIndex += 1
        }

        return currentNode
  }
    
    func insert(_ value: T, after index: Int) {
      guard let node = node(at: index) else { return }
      
      node.next = Node(value: value, next: node.next)
    }
    
    
    mutating func pop() -> T? {
        defer {
          head = head?.next
          
          if isEmpty {
            tail = nil
          }
        }
        
        return head?.value
      }
    
    
    mutating func removeLast() -> T? {
        guard let head = head else { return nil }
        if head.next == nil { return pop() }
        
        var previousNode = head
        var currentNode = head
        
        while let next = currentNode.next {
          previousNode = currentNode
          currentNode = next
        }
        
        previousNode.next = nil
        tail = previousNode
        
        return currentNode.value
      }
    
    
    mutating func remove(after index: Int) -> T? {
        guard let node = node(at: index) else { return nil }
        
        defer {
          if node.next === tail {
            tail = node
          }
          
          node.next = node.next?.next
        }
        
        return node.next?.value
      }
    
}

func printLList<T>(list: LinkedList<T>) {
    
    var current = list.head
    while current != nil {
        print(current!.value as T)
        current = current?.next
    }
    
}



var list = LinkedList<Int>()

list.push(10)
list.push(22)
//printLList(list: list)
// 22 -> 10
list.append(5)
list.append(2)
//printLList(list: list)
// 22 -> 10 -> 5 -> 2



list.insert(15, after: 1)
//printLList(list: list)
// 22 -> 10 -> 15 -> 5 -> 2



list.pop()
printLList(list: list)
// 10 -> 15 -> 5 -> 2


list.removeLast()
//printLList(list: list)
// 10 -> 15 -> 5


list.remove(after: 0)
//printLList(list: list)
// 10 -> 5

