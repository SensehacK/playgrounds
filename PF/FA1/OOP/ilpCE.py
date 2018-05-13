'''
Created on Feb 15, 2017

@author: kautilya.save
'''


'''
from abc import ABCMeta, abstractmethod

class Shape(metaclass = ABCMeta) :
    def __init__(self):
        print("I Am in init")
        
        
    @abstractmethod
    def draw_shape(self):
        pass
    
    
    @abstractmethod
    def set_color(self):
        pass
    
    
class Circle(Shape):
    
    def draw_shape(self):
        print("Draw Circle")
        
    
    def set_color(self):
        print("Draw Circle")
        
        
clas  = Circle()
clas.draw_shape()




'''

'''
class SomeException(Exception) :
    pass
class Calculator :
    def div (self , a ,b):
        c = a//b
        raise SomeException
    

try :
    cal = Calculator()
    cal.div(10,0)
    
except SomeException:
    print("Some Exception")
except :
    print("error")
    
finally: 
    print("Finally")
        
        
'''
# This was the error  , it is important to initialize the constructors of parent class init method constructor.

class ClassA :
    def __init__(self):
        self.__var_one = 100
    
    def method_one(self):
        return self.__var_one

class ClassB(ClassA):
    
    def __init__(self,var_two):
        super().__init__()
        self.__var_two = var_two
        
    
    def method_two(self):
        
        final_val = self.__var_two + self.method_one()
        
        return final_val

bob = ClassB(50)

print(bob.method_two())







