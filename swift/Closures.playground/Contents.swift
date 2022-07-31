import UIKit


//func getData2(completion: ((Bool) -> Void)) {
//    completion(true)
//}

print("GH")
//
//
//func getData(completion: @escaping ((Bool) -> Void)) {
//
//    let task = URLSession.shared.dataTask(with: URL(string: "http://www.google.com")!) { data, response, error in
//        guard data != nil else {
//            completion(false)
//            return
//        }
//
//        completion(true)
//    }
//
//    task.resume()
//}
//
//
//getData { state in
//    if state {
//        print("Yay")
//    } else {
//        print("Nay")
//    }
//}
//


final class APICaller {
    
    var isReady = false
    
    var completionHandlers = [(() -> Void)]()
    
    func warmup(completion: @escaping (() -> Void)) {
        isReady = true
        print("In Warmup")
        if !completionHandlers.isEmpty {
            completionHandlers.forEach({ $0() })
            completionHandlers.removeAll()
            completion()
        }
        
        
    }
    
    func doSomething(completion: @escaping (() -> Void)) {
        guard isReady else {
            completionHandlers.append {
                completion()
            }
            return
        }
        
        completion()
    }
    
}


APICaller().doSomething {
    print("Doing something !") // This will add the closure
}

APICaller().warmup {
    print("CAll warmup")
}
APICaller().doSomething {
    print("After warmup!")
}


let apiA = APICaller()
apiA.doSomething {
    print("##1 First do something!") // This will append the message in the closure array
}

apiA.doSomething {
    print("##2 Second try!") // This will append the message in the closure array
}

apiA.doSomething {
    print("##3 Third try!") // This will append the message in the closure array
}

apiA.warmup {
    print("### Hello warmup!") // This will unwrap all the closure array elements and execute their completions which were the print statements.
    // I'm assuming swift is just storing the reference types of the API closure address!
}

//APICaller().
