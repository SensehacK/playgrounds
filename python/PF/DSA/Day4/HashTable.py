'''
Created on Feb 13, 2017

@author: kautilya.save
'''

from DataStructures import *
def fun(input_stack):
    output_queue=Queue(input_stack.get_max_size())
    temp_queue=Queue(input_stack.get_max_size())
    while(not input_stack.is_empty()):
        data=input_stack.pop()
        if(data%2==0):
            print("Even")
            output_queue.enqueue(data)
        else:
            print("Odd")
            temp_queue.enqueue(data)
    temp_data=0
    while(not temp_queue.is_empty()):
        temp_data+=temp_queue.dequeue()        
        output_queue.enqueue(temp_data)    
    output_queue.display()

input_stack = Stack(5)
input_stack.push(7)
input_stack.push(6)
input_stack.push(9)
input_stack.push(1)
input_stack.push(2)

fun(input_stack)
    