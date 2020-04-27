'''
Created on Jan 30, 2017

@author: kautilya.save
'''


g = lambda a ,b : a+b
g1 = lambda a , b : a*b

print(g(4343424242453424242424224232324354465574753634634643643634645334,5335252525524563446332525352435534))

print("Multiply 42 * 40 : " ,g1(42,40))

print("Adding + Product : " , g(24,534) * g1(23,46))


#PF-Exer-38
#This verification is based on string match.
import math
num1=36
num2=10
num3=4
num4 = 36

calc = lambda x , y :(x-y) + (x%y)
print(calc(num1,num2))

square_root = lambda x : math.sqrt(x)
print(square_root(num3))

square_root2=lambda x : x ** 0.5
print(square_root2(num4))