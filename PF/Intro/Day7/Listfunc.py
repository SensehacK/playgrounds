'''
Created on Jan 27, 2017

@author: kautilya.save
'''
import time
import datetime

num_list  = [1,2,3]
num_list.reverse()

print(num_list)


print(time.gmtime())

dict1 = {}
list1 =  ['1:A' , '2:B'  ,' 3:C' ]
print(list1)

for i in list1 :
    
    list2 = i.split(':')
    print(list2)
    dict1.update({list2[0]:list2[1]})

print(dict1)
