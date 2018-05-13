'''
Created on Feb 9, 2017

@author: kautilya.save
'''
class Node:
    def __init__(self,data):
        self.__data=data
        self.__next=None

    def get_data(self):
        return self.__data
    
    def set_data(self,data):
        self.__data=data
    
    def get_next(self):
        return self.__next
    
    def set_next(self,next_node):
        self.__next=next_node
    
class LinkedList:
    def __init__(self):
        self.__head=None
        self.__tail=None
    
    def get_head(self):
        return self.__head
    
    def get_tail(self):
        return self.__tail
    
    def add(self,data):
        new_node = Node(data)
        
        if self.__head == None :
            self.__head = new_node
            self.__tail = new_node
        
        else :
            self.__tail.set_next(new_node)
            self.__tail = new_node

    def display(self):
        temp = self.__head
        
        while(temp is not None) :
            print(temp.get_data())
            temp = temp.get_next()
        
        
    def find_node(self,data):
        temp = self.__head
        
        while temp is not None :
            if temp.get_data() == data :
                return temp
            else :
                temp = temp.get_next()
        
        return None
    
    
    def delete(self,data):
        node = self.find_node(data)
        if node != None :
            if node == self.__head :
                self.__head = node.get_next() 
                node.set_next(None)
                
            else :
                temp = self.__head
                while(temp is not None) :
                    if temp.get_next() == node:
                        temp.set_next(node.get_next())
                        node.set_next(None)
                        
                        if temp.get_next() == None : 
                            self.__tail = temp
                    
                    else :
                        
                        temp = temp.get_next()
                        
        else :
            
            print(data, "not present")
            
l1=LinkedList()
l1.add("Milk")
l1.add("Salt")
l1.add("Biscuit")
l1.add("Apple Juice")
l1.add("Pomegranate")
l1.add("Watermelon")

print("Before")
l1.display()

l1.delete("Salt")
print("////////////////////////////////////////")
print("After")
l1.display()

node=l1.find_node("Biscuit")
if(node!=None):
    print("Node found" , node.get_data())
else:
    print("Node not found") 