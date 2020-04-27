#DSA-Exer-8
                                        
class Queue:
    def __init__(self,max_size):
        self.__max_size=max_size
        self.__elements=[None]*self.__max_size
        self.__rear=-1
        self.__front=0
    
    def get_front(self):
        return self.__front
    
    def get_rear(self):
        return self.__rear
    
    def get_max_size(self):
        return self.__max_size
    
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
    
def split_queue(num_queue):
    #Populate queue_list with odd_queue and even_queue
    queue_list=[]
    even_queue = Queue(num_queue.get_max_size())
    odd_queue = Queue(num_queue.get_max_size())
    
    while not num_queue.is_empty() :
        num = num_queue.dequeue()
        if num % 2 == 0 :
            even_queue.enqueue(num)
        
        else :
            odd_queue.enqueue(num)
    
    queue_list.append(odd_queue)
    queue_list.append(even_queue)
    

    return queue_list

# Enqueue different values to the queue and test your program

num_queue=Queue(7)
num_queue.enqueue(2)
num_queue.enqueue(7)
num_queue.enqueue(9)
num_queue.enqueue(4)
num_queue.enqueue(6)
num_queue.enqueue(5)
num_queue.enqueue(10)

q_list=split_queue(num_queue)
q_list[0].display()
q_list[1].display()