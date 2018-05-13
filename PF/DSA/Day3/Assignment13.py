#DSA-Assgn-13

#This assignment needs DataStructures.py file in your package, you can get it    from resources page

from DataStructures import Stack

def change_smallest_value(number_stack):
    list1 = []
    while not number_stack.is_empty() :
        list1.append(number_stack.pop())
    min_list = min(list1)
    
    for values in list1:
        if values == min_list :
            number_stack.push(values)
    for st in list1[::-1] :
        if st != min_list :
            number_stack.push(st)
    return number_stack   

number_stack=Stack(10)
number_stack.push(90)
number_stack.push(3)
number_stack.push(3)
number_stack.push(7)
number_stack.push(4)

print("Initial Stack:")
number_stack.display()
change_smallest_value(number_stack)
print("After the change:")
number_stack.display()