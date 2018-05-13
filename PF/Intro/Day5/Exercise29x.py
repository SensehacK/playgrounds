#PF-Exer-29

def merge_lists(list1,list2):
    #Write your logic here
    new_merge_list = list1 + list2
    return new_merge_list

def sort_list(merged_list):
    i = 0
    j = i + 1
    #merged_list2 = []
    for i in range (0, len(merged_list)) :
        
        for j in range (i , len(merged_list)) :
            
            if (merged_list[i] > merged_list[j]) :
                
                temp = merged_list[j]
                merged_list[j] = merged_list[i]
                merged_list[i] = temp
    
                 
    return merged_list

#Provide different values for list1 and list2 and test your program
merged_list=merge_lists(list1=[1,2,3,4,1] ,list2=[2,3,4,5,4,6])
print(merged_list)
sorted_merged_list=sort_list(merged_list)  
print(sorted_merged_list)