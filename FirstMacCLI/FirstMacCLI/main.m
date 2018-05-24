//
//  main.m
//  FirstMacCLI
//
//  Created by Kautilya on 23/05/18.
//  Copyright © 2018 Sensehack. All rights reserved.
//

#import <Foundation/Foundation.h>
#import "House.h"


int main(int argc, const char * argv[]) {
    @autoreleasepool {
        // insert code here...
        NSLog(@"Hello, Sensehack World!");
//        /*
        House *myHouse = [[House alloc]init];
        int number = myHouse.numberOfBedrooms;
//        myHouse.numberOfBedrooms = 5 + 7;
        
        NSLog(@"%d", number);
        NSLog(@"%d", myHouse.numberOfBedrooms);
        
//        */
        
        // Mutating the string on to a pointer & then try to edit it.
        
        NSMutableString *addressString = [[NSMutableString alloc] initWithString: @"C/501 Park Avenue West."];
        //Printing address string before assigning address
//        NSLog(@"%@", addressString);
        
        // Allocating a new object with this string.
        House *myAddr = [[House alloc] initWithFakeAddress: addressString];
        
        NSLog(@"%@", myAddr.address);
        
        NSLog(@"myHouse.numberOfBedrooms %d", myHouse.numberOfBedrooms);
        NSLog(@"myAddr.numberOfBedrooms %d", myAddr.numberOfBedrooms);
    }
    return 0;
}
