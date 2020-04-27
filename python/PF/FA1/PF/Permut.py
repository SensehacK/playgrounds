'''
Created on Feb 19, 2017

@author: kautilya.save
'''

import itertools


print (list(itertools.permutations([1,2,3])))

print (list(itertools.permutations([1,2,3,4], 2)))


list1 = (itertools.permutations([4,22,43,14], 2))

for va in list1 :
    print(va)
    
