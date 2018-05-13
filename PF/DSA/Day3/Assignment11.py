# DSA-Assgn-11

# This assignment needs DataStructures.py file in your package, you can get it    from resources page

from DataStructures import Queue

def merge_queue(queue1, queue2):
    lent = queue1.get_max_size() + queue2.get_max_size()
    
    
    merge_list2 = Queue(lent)
    
    while not merge_list2.is_full():
        
        if not queue1.is_empty() :
            merge_list2.enqueue(queue1.dequeue()) 
            
        if not queue2.is_empty():
            merge_list2.enqueue(queue2.dequeue()) 
    
           
        
    
    return merge_list2
    
    
    
    
    
#     
#     if lent1 < lent2 :
#         difference = lent2 - lent1 
#         queue1_flag = False
#     elif lent2 < lent1 :
#         difference = lent1 - lent2
#         queue1_flag = True
#     
#     else :
#         difference = 0
#         
#         
#     
#     while(1) :
#         if count > lent :
#             break
#         
#             
#         if count % 2 == 0 and not queue1.is_empty():
#             dataq1 = queue1.dequeue()
#             merged_queue2.enqueue(dataq1)
#             count += 1
#             print(merged_queue2.display()) 
#         elif (count % 2 != 0 and not queue2.is_empty()) :
#             dataq2 = queue2.dequeue()
#             merged_queue2.enqueue(dataq2)
#             count += 1
#         else :  
#             if queue1_flag :
#                 while(difference != 0) :  
#                     dataq1 = queue1.dequeue()
#                     merged_queue2.enqueue(dataq1)
#                     difference -= 1
#             else :
#                 while(difference != 0) :  
#                     dataq2 = queue2.dequeue()
#                     merged_queue2.enqueue(dataq2)
#                     difference -= 1
#                     
#                     
#     merged_queue2.display()
#     return merged_queue2

# Enqueue different values to both the queues and test your program

queue1 = Queue(3)
queue2 = Queue(6)
queue1.enqueue(3)
queue1.enqueue(6)
queue1.enqueue(8)
queue2.enqueue('b')
queue2.enqueue('y')
queue2.enqueue('u')
queue2.enqueue('t')
queue2.enqueue('r')
queue2.enqueue('o')

merged_queue = merge_queue(queue1, queue2)
print("The elements in the merged queue are:")
merged_queue.display()
