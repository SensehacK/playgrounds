import UIKit


var image_: (String) -> String {
    { "image-\($0)" }
}

// Call

print(image_("3"))
