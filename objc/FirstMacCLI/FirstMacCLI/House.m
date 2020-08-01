//
//  House.m
//  FirstMacCLI
//
//  Created by Kautilya on 23/05/18.
//  Copyright © 2018 Sensehack. All rights reserved.
//

#import "House.h"



@interface House()

@property  (nonatomic, readwrite) int numberOfBedrooms;

@end


@implementation House

-(instancetype)initWithFakeAddress:(NSString *)address {
    
    self = [super init];
    
    if (self) {
        _address = [address copy];
        _numberOfBedrooms = 5;
        _hasHotTub = false;

    }
    
    return self;
}


@end
