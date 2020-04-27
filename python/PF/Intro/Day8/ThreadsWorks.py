'''
Created on Jan 30, 2017

@author: kautilya.save
'''
from threading import Thread
list1=[]
list2=[]
myarray=[25,11,12,95,12,56,43,87,12,34,55,95,15,26,48,66,74,28,54,73]
def array_operation(start_index,end_index,out_list,thread_name):
    sum=0
    for i in range(start_index,end_index):
        sum=sum+myarray[i]
        print(thread_name)
    out_list.append(sum)
t1 = Thread(target=array_operation, args=(0,9,list1,"Thread One"))
t2 = Thread(target=array_operation, args=(10,19,list2,"Thread Two"))
t2.start()
t1.start()
# t2.join()
# t1.join()
func_value1 = list1
print("Sum of elements of first half list:",func_value1)
                       
func_value2 = list2
print("Sum of elements of second half list:",func_value2)
total=func_value1[0]+func_value2[0]
print("Total sum:",total)