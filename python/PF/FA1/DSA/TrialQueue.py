'''
Created on Feb 18, 2017

@author: kautilya.save
'''
'''
queue1=[2,5,8,9,6,4]
queue2-->output
output-->[10,5,40,9,30,20]
if even then multiply with 5


'''

from DataStructures import Queue

class Cal :
        
    def calculate(self,queue1):
        queue2 = Queue(queue1.get_max_size())
        
        
        while ( queue1.get_rear() >= queue1.get_front()) :
            
            temp = queue1.dequeue()
            
            if temp % 2 == 0 :
                queue2.enqueue(temp*5)
                
            else :
                queue2.enqueue(temp)
        
        
        return queue2

que = Queue(6)
que.enqueue(2)
que.enqueue(5)
que.enqueue(8)
que.enqueue(9)
que.enqueue(6)
que.enqueue(4)

cla = Cal()

cla.calculate(que).display()
