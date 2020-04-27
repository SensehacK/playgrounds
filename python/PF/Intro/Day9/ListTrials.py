'''
Created on Jan 31, 2017

@author: kautilya.save
'''
a = [220,10,1,2,3,4,5,6,10]
#print("Before",a)
#b = a 
b = list(a)
b[1] = 50
#print("After",a)

#print(b)
print(id(a))
print(id(b))