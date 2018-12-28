//: A UIKit based Playground for presenting user interface
  
import UIKit
import PlaygroundSupport

class MyViewController : UIViewController {
    override func loadView() {
        let view = UIView()
        view.backgroundColor = .white

        let label = UILabel()
        label.frame = CGRect(x: 150, y: 200, width: 200, height: 20)
        label.text = "Hello World!"
        label.textColor = .black
        
        view.addSubview(label)
        self.view = view
            
//        let IS_IPHONEX = ( ([[UIScreen mainScreen] bounds].size.height-812)? NO:YES)
        print(UIScreen.main.bounds.size.height)
        let boolIpX = UIScreen.main.bounds.size.height
        print(boolIpX)
    }
}
// Present the view controller in the Live View window
PlaygroundPage.current.liveView = MyViewController()
