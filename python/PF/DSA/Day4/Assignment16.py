#DSA-Assgn-16

#This assignment needs DataStructures.py file in your package, you can get it    from resources page

from DataStructures import Stack,Queue

def separate_boxes(box_stack):
    length = box_stack.get_max_size()
    temp_stack = Stack(length)
    que = Queue(length)
    while not box_stack.is_empty() :
        temp_box = box_stack.pop()
        
        if temp_box == "Red" or temp_box == "Green" or temp_box == "Blue" :
            temp_stack.push(temp_box)
        else :
            que.enqueue(temp_box)

    while not temp_stack.is_empty() :
        temp_box = temp_stack.pop()
        box_stack.push(temp_box)
        
    
    return que
        
#Use different values for stack and test your program
box_stack=Stack(8)
box_stack.push("Red")
box_stack.push("Magenta")
box_stack.push("Yellow")
box_stack.push("Red")
box_stack.push("Orange")
box_stack.push("Green")
box_stack.push("White")
box_stack.push("Purple")
print("Boxes in the stack:")
box_stack.display()
result=separate_boxes(box_stack)
print()
print("Boxes in the stack after modification:")
box_stack.display()
print("Boxes in the queue:")
result.display()