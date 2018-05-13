#PF-Assgn-35

#Global variable
list_of_marks=(12,18,25,24,2,5,18,20,20,21)

def find_more_than_average():
    sum=0
    count=0
    x=len(list_of_marks)
    for i in list_of_marks:
        sum=sum+i
    avg=sum/x
    for i in list_of_marks:
        if (i>avg):
            count+=1
        
    percentage_of_students=(count/x)*100
    return(percentage_of_students) 
        
    
    #Remove pass and write your logic here

def sort_marks():
    list_of_marks.sort()
    return (list_of_marks)
    
    #Remove pass and write your logic here

def generate_frequency():
    count=0
    generate_frequency_list=[]
    for t in range(0,25):
        for j in list_of_marks:
        
            if t==j:
                count+=1
        
        generate_frequency_list.append(count)
        count=0
    print(generate_frequency_list)
    return(generate_frequency_list)
            
                
        
    
            
        
        
    
    
    
    #Remove pass and write your logic here

print(find_more_than_average())
print(generate_frequency())
print(sort_marks())
