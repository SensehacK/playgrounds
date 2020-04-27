'''
Created on Feb 17, 2017

@author: kautilya.save
'''
class Queue:
    def __init__(self,max_size):
        
        self.__max_size=max_size
        self.__elements=[None]*self.__max_size
        self.__rear=-1
        self.__front=0
    
    def is_full(self):
        if(self.__rear==self.__max_size-1):
                return True
        return False
    
    def is_empty(self):
        if(self.__front>self.__rear):
            return True
        return False
    
    def enqueue(self,data):
        if(self.is_full()):
            print("Queue is full!!!")
        else:
            self.__rear+=1
            self.__elements[self.__rear]=data
    
    def dequeue(self):
        if(self.is_empty()):
            print("Queue is empty!!!")
        else:
            data=self.__elements[self.__front]
            self.__front+=1
            return data
    
    def display(self):
        for index in range(self.__front, self.__rear+1):
            print(self.__elements[index])
    
    def get_front(self):
        return self.__front
    
    def get_rear(self):
        return self.__rear
    
    def get_max_size(self):
        return self.__max_size
    
"""*********************Stack*****************************"""
class Stack:
    def __init__(self,max_size):
        self.__max_size=max_size
        self.__elements=[None]*self.__max_size
        self.__top=-1
            
    def is_full(self):
        if(self.__top==self.__max_size-1):
            return True
        return False
    
    def is_empty(self):
        if(self.__top==-1):
            return True
        return False
    
    def push(self,data):
        if(self.is_full()):
            print("The stack is full!!")
        else:
            self.__top+=1
            self.__elements[self.__top]=data
            
    def pop(self):
        if(self.is_empty()):
            print("The stack is empty!!")
        else:
            data= self.__elements[self.__top]
            self.__top-=1
            return data
    
    def display(self):
        if(self.is_empty()):
            print("The stack is empty")
        else:
            index=self.__top
            while(index>=0):
                print(self.__elements[index])
                index-=1
    
    def get_top(self):
        return self.__top
    
    def get_max_size(self):
        return self.__max_size
    
    


class Extra :
    
    
    
    def retur(self, input_stack , input_queue):
        
        output_queue = Queue((input_queue.get_max_size()))
        
        list1  = []
        list2 = []
        stack_list = []
        
        
        while not input_queue.is_empty() :
            temp = input_queue.dequeue()
            list1.append(temp)
            
            
        list2 = list1[:]
        
        
        
        
        while not input_stack.is_empty() :
            stpop = input_stack.pop()
            stack_list.append(stpop)
            print(stpop)
            
            if stpop == 1:
                print("Before operation 1")
                print(list1)
                print("1")
                temp = list1[0]
                list1 = list1[1:]
                list1.append(temp)
                
                
                
            elif stpop == 2 :
                print("Before operation 2")
                print(list1)
                print("2")
                list2 = []
                temp = list1[:-1]
                str2 = list1[-1]
                list1 = []
                list1.append(str2)
                
                for v in temp :
                    list1.append(v)
                    
                
        pop_stack_list = stack_list[0]
        
        
        if pop_stack_list == 1:
                print("Before operation 1")
                print(list1)
                print("1")
                temp = list1[0]
                list1 = list1[1:]
                list1.append(temp)
                
                
                
        elif pop_stack_list == 2 :
                print("Before operation 2")
                print(list1)
                print("2")
                list2 = []
                temp = list1[:-1]
                str2 = list1[-1]
                list1 = []
                list1.append(str2)
                
                for v in temp :
                    list1.append(v)
        
    
        
        for values in list1 :
            output_queue.enqueue(values)
        
        print("output_queue.display()")
        output_queue.display()
        return list1
    
    
    
st = Stack(2)
st.push(2)
st.push(1)


que = Queue(3)

que.enqueue("A")
que.enqueue("B")
que.enqueue("C")


ex = Extra()
ex.retur(st, que)