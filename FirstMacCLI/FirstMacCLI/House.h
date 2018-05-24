//
//  House.h
//  FirstMacCLI
//
//  Created by Kautilya on 23/05/18.
//  Copyright © 2018 Sensehack. All rights reserved.
//

#import <Foundation/Foundation.h>

@interface House : NSObject

@property (nonatomic) NSString *address;
@property (nonatomic, readonly) int numberOfBedrooms;
@property (nonatomic) bool hasHotTub;


-(instancetype)initWithFakeAddress : (NSString*)address;

@end
