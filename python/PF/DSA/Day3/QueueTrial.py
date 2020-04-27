'''
Created on Feb 10, 2017

@author: kautilya.save
'''


class Queue() :
    def __init__(self,max_size):
        self.__max_size = max_size
        self.__element_list = [None] * max_size
        self.__front = 0 
        self.__rear = -1
        
    
    def is_full(self):
        if self.__rear == self.__max_size - 1 :
            return True
        
        
    def enque(self,data):
        if self.is_full() :
            print("Queue is already full")
            
        else :
            self.__rear+= 1
            self.__element_list[self.__rear] = data
    
    
    def is_empty(self):
        if self.__front > self.__rear :
            return True        
    def deque(self):
        
        if self.is_empty():
            
            print("Queue is empty")
            
        else :
            
            data = self.__element_list[self.__front]
            self.__front +=1
            return data
        
        
    def display(self):
        if self.is_empty() :
            pass
        else :  
            index = self.__front
            
            while index <= self.__rear :
                print(self.__element_list[index])
                index += 1
        
        
        
q1 = Queue(5)
q1.enque("A")
q1.enque("R")
q1.enque("T")
q1.enque("Y")
q1.enque("I")
print("Sixth Element")
q1.enque("Y")

q1.display()
