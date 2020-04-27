#DSA-Assgn-13

#This assignment needs DataStructures.py file in your package, you can get it    from resources page
# Done with Stacks & not lists
from DataStructures import Stack

def change_smallest_value(number_stack):
    
    
    length1 = number_stack.get_max_size()
    copy_stack = Stack(length1)
    extra_stack = Stack(length1)
    extra_stack2 = Stack(length1)
    
    temp = number_stack.pop()
    min_stack = temp
    copy_stack.push(min_stack)
    
    while not number_stack.is_empty() :
        temp_min = number_stack.pop()
        if temp_min < min_stack :
            min_stack = temp_min
            copy_stack.push(temp_min)
        else :
            copy_stack.push(temp_min)

    while not copy_stack.is_empty() :
        temp_min = copy_stack.pop()
        
        if temp_min ==  min_stack :
            extra_stack.push(temp_min)
        elif temp_min !=  min_stack :
            extra_stack2.push(temp_min)
    
    while not extra_stack2.is_empty() :
        temp_min = extra_stack2.pop()
        copy_stack.push(temp_min)
       
    while not copy_stack.is_empty() :
        temp_min = copy_stack.pop() 
        extra_stack.push(temp_min) 
        
    return extra_stack   


#Add different values to the stack and test your program
number_stack=Stack(11)
number_stack.push(7)
number_stack.push(8)
number_stack.push(5)
number_stack.push(1)
number_stack.push(66)
number_stack.push(5)
number_stack.push(1)
number_stack.push(3)
number_stack.push(8)
number_stack.push(5)

print("Initial Stack:")
number_stack.display()
number_stack = change_smallest_value(number_stack)
print("After the change:")
number_stack.display()