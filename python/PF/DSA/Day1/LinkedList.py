'''
Created on Feb 8, 2017

@author: kautilya.save
'''

class Node:
    def __init__(self,data):
        self.__data = data
        self.__next = None

    def get_data(self):
        return self.__data

    def get_next(self):
        return self.__next

    def set_data(self, value):
        self.__data = value

    def set_next(self, value):
        self.__next = value

class LinkedList():
    def __init__(self):
        self.__head = None 
        self.__tail = None

    def get_head(self):
        return self.__head
    def get_tail(self):
        return self.__tail
    def set_head(self, value):
        self.__head = value
    def set_tail(self, value):
        self.__tail = value

    def add(self,data):
        new_node = Node(data)
        if self.__head == None:
            self.__head = new_node
            self.__tail = new_node
        else:
            self.__tail.set_next(new_node)
            self.__tail = new_node
    
    def display(self):
        temp = self.__head
        while(temp is not None) :
            print(temp.get_data())
            temp = temp.get_next()
            
            
    def search(self,data):
        temp = self.__head
        while temp is not None :
            if temp.get_data() == data :
                return temp
            else :
                temp = temp.get_next()
                
        return None
        
        
    def insert(self,data_before,data):
        new_node = Node(data)
        if data_before == None :
            new_node.set_next(self.__head)
            self.__head = new_node
            
        else :
            node_before = self.find(data_before)
            if node_before is not None :
                new_node.set_next(node_before.get_next())
                node_before.set_next(new_node)
                if node_before == self.__tail :
                    self.__tail 
            else :
                print(data_before , "is not present")
        
        
l1 = LinkedList()
# print(l1.get_head(),l1.get_tail())
l1.add("a")
l1.add("b")
l1.add("c")
l1.add("d")
l1.add("e")

l1.display()




