'''
Created on Jan 30, 2017

@author: kautilya.save
'''


def addTwo(a,b):
    print("hi")
    return a+b
        
    
    
def display(func1,m,n):
    print("In display func")
    return  func1(m,n)
   

print(display(addTwo,20,32))