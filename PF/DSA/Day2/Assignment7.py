#DSA-Assgn-7

#This assignment needs DataStructures.py file in your package, you can get it    from resources page

from DataStructures import LinkedList

def remove_duplicates(duplicate_list):
    #write your logic here
    
    present_node = duplicate_list.get_head()
    next_node = present_node.get_next()
    
    while ( present_node.get_next() != None) :
        
        data1 = present_node.get_data()
        data2 = next_node.get_data()
        
        if data1 == data2 : 
            print(data1)
            duplicate_list.delete(data1)
            present_node = next_node
            next_node = next_node.get_next()
        
        if data1 != data2 :
            present_node = next_node
            next_node = next_node.get_next()
        
    
    duplicate_list.display()
    return duplicate_list



#Add different values to the linked list and test your program 
duplicate_list=LinkedList()
duplicate_list.add(30)
duplicate_list.add(40)
duplicate_list.add(40)
duplicate_list.add(40)
duplicate_list.add(40)

print(remove_duplicates(duplicate_list))
