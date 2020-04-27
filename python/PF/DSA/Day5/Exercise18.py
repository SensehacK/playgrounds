#DSA-Exer-18

def find_next_min(num_list,start_index):
    #Remove pass and write the logic to find the minimum element in a sub-list and return the index of the identified element in the num_list.
    min_index = start_index
    
    for i in range(start_index+1,len(num_list)) :
        print(num_list[i])
        print(num_list[min_index])
        if num_list[i]<num_list[min_index] :
            min_index = i
            
    return min_index
        
    

#Pass different values to the function and test your program
num_list=[1,10,2,3,100,67]
start_index=4
print("Index of the next minimum element is", find_next_min(num_list,start_index))