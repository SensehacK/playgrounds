#DSA-Exer-1

def update_mark_list(mark_list, new_element, pos):
    mark_list.insert(pos, new_element)
    return mark_list

def find_mark(mark_list,pos1,pos2):
    print("Marks at ", pos1 , "are " , mark_list[pos1])
    
    print("Marks at ", pos2 , "are " , mark_list[pos2])
    list2 = []
    list2.append(mark_list[pos1])
    list2.append(mark_list[pos2])
    return list2

# mark_list=[98,87,65,33,49]
# pos1=2
# pos2=4

mark_list=[89,78,99,76,77,72,88,99]
new_element=69
pos=2
pos1=5
pos2=8
print(update_mark_list(mark_list, new_element, pos))
print(find_mark(mark_list, pos1, pos2))



