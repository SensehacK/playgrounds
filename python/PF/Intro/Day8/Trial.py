'''
Created on Jan 30, 2017

wrong program , just trial of deadlock loops
@author: kautilya.save
'''
from threading import Thread


def tryit1():
    #name = input("Enter your name")
    for i in range(len(z)) :
        z-=1
        print("i:", i)
#         tryit2()
    print("Done") 
    #print(name)
    
def tryit2():
    x= 1 
    for i in range(len(y)) :
        y-=1
        x = x*i
        print("x:" , x)
        tryit1()
    print("Done") 
    
    
z = 100
y = 100
t1 = Thread(target=tryit1)
t2 = Thread(target=tryit2)
t1.start()
print("Sensehack Threads")
t2.start()

# tryit1()
# 
# print("Hello")
# tryit2()
