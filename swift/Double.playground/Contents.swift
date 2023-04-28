import UIKit

var greeting = "Hello, playground"

let value2e2 = 2212.6

extension Double {
    func roundValue() -> String {
        return String(format: "%.0f", self)
    }
}


print(value2e2)
print(String(format: "%.0f", value2e2))
print(value2e2.rounded())
