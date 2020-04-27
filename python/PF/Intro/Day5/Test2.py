'''
Created on Jan 24, 2017

@author: kautilya.save
'''



# pass by reference & Value

def change (list1):
    list1.append(4)
    
    print(list1, "Inside Function")
    return


my_list = [1,2,3]
print(my_list, "Outside , before")
change(my_list)
print(my_list, "Outside , after")




# Tuple Pass by value 


def change2 (list_t):
    list_t = my_list_tuple + list_t
    
    
    print(list_t, "Inside Function")
    return


my_list_tuple = (1,2,3)
print(my_list_tuple, "Outside , before")
change2(my_list_tuple)
print(my_list_tuple, "Outside , after")





    