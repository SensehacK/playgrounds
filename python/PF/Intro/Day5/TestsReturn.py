'''
Created on Jan 24, 2017

@author: kautilya.save
'''


#product Sum increase.

def sum ( num ) :
    sum = 0
    for i in range(1, num+1) :
        
        sum = sum + i
    
    
    
    return sum

print(sum(6))