import UIKit

var someString: String?


extension Optional where Wrapped == String {
    
    var orEmpty: String {
        switch self {
        case .some(let value):
            return value
        case .none:
            return ""
        }
    }
}

print(someString.orEmpty)

