'''
Created on Jan 23, 2017

@author: kautilya.save
'''
#goal of this tryout is to create a function from scratch and invoke it for the given problem

def fahrenheit(celsius) :
    
    return temp* (9/5)) + 32
    


def celsius(fahrenheit) :
    
    return (fahrenheit - 32) * (5/9)
    

def conversion(temp,type) :
    
    if type == "F" :
        return (temp - 32) * (5/9)
    elif type == "C":
        return temp* (9/5)) + 32
    

print("Celsius of :" , celsius(87))
#print("Celsius of :" , celsius(78))

print("fahrenheit of :" , fahrenheit(30))


print("Temperature of : " , conversion(78, "F"))