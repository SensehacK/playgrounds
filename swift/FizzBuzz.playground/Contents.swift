import UIKit

var str = "Hello, playground"

var threeFives = [0,0,0];

for i in 1...100 {
    
    
    
    if (i%3==0 && i%5==0) {
        print("FizzBuzz");
        threeFives[2] = threeFives[2] + 1;
        continue;
    }
    
    if (i%3==0) {
        print("Fizz");
        threeFives[0] = threeFives[0] + 1;
        continue;
    }
    
    if (i%5==0) {
        print("Buzz");
        threeFives[1] += 1;
        continue;
    }
    
    print("Value", +i);
    
}

print("Overall Numbers divided by 3 are " , +threeFives[0]);

print("Overall Numbers divided by 5 are " , +threeFives[1]);

print("Overall Numbers divided by 5 & 3 are " , +threeFives[2]);
