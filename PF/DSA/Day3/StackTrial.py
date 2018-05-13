'''
Created on Feb 10, 2017

@author: kautilya.save
'''



class Stack :
    
    
    def __init__(self,max_size):
        self.__top = -1
        self.__max_size = max_size
        self.__element_list = [None] * self.__max_size
    
    def is_full(self):
        if self.__top == self.__max_size -1 :
            return True
        
        return False
    
    def push (self,data):
        if self.is_full():
            
            print("Stack is full re baba!!")
               
        else :
            
            self.__top += 1
            self.__element_list[self.top] = data
            
            
    def is_empty(self):
        if is_self.__top == -1 :

            return True
    
    def pop(self,value):
        
        if self.is_empty():
            print("Stack is empty")
            
        else :
            data = self.__element_list[self.top]
            self.__top += 1 
            return data
        
        
        
        
        
        
        
        
s1 = Stack(5)
s1.push("a")
s1.push("b")
s1.push("c")
s1.push("d")
s1.push("e")
            