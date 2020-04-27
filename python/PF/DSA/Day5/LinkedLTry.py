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
        new_node=Node(data)
        if(self.__head is None):
            self.__head=self.__tail=new_node
        else:
            self.__tail.set_next(new_node) 
            self.__tail=new_node
    
    def insert(self,data,data_before):
        new_node=Node(data)
        if(data_before==None):
            new_node.set_next(self.__head) 
            self.__head=new_node
            
        else:
            node_before=self.find_node(data_before)
            if(node_before is not None):
                new_node.set_next(node_before.get_next()) 
                node_before.set_next(new_node)   
                if(new_node.get_next() is None):       
                    self.__tail=new_node
            else:
                print(data_before,"is not present in the Linked list")
    
    def display(self):
        temp=self.__head
        while(temp is not None):
            print(temp.get_data())
            temp=temp.get_next()     
    
    
    def find_node(self,data):
        temp=self.__head
        while(temp is not None):
            if(temp.get_data()==data):
                return temp
            temp=temp.get_next()    
        return None
    
    def delete(self,data):
        node=self.find_node(data)
        if(node is not None):
            if(node==self.__head):
                self.__head=node.get_next() 
            else:
                temp=self .__head
                while(temp is not None):
                    if(temp.get_next()==node): 
                        temp.set_next(node.get_next())    
                        if(node==self.__tail):
                            self.__tail=temp
                        node.set_next(None)
                        break
                    temp=temp.get_next()    
        else:
            print(data,"is not present in Linked list")


    def fun(self,head):
        if head==None:
            return
        self.fun(head.get_next())
        print(head.get_data())
    
    
    def fun2(self,head):
        if head==None:
            return
        print(head.get_data())
        if head.get_next() is not None:
            self.fun2(head.get_next().get_next())
        print(head.get_data())
    
    def fun3(self,list1):
        if list1.get_head()==None and list1.get_head().get_next()==None:
            return
        point1=list1.get_head()
        point2=list1.get_head().get_next()
        while point2:
            temp=point1.get_data()
            point1.set_data(point2.get_data())
            point2.set_data(temp)
            point1=point2.get_next()
            if point2.get_next()==None:
                break
            point2=point1.get_next() 
        list1.display()  
l1=LinkedList()
l1.add(10)
l1.add(20)
l1.add(30)
l1.add(40)
l1.add(50)
l1.add(60)
# l1.fun(l1.get_head())
# l1.fun2(l1.get_head())
l1.fun3(l1)