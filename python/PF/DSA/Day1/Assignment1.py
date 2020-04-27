#DSA-Assgn-1

def merge_list(list1, list2):
    merged_data= []
    resultant_data = ""
#     list3 = list2
#     list2.reverse()
#     #print(list2)
#     print(list3)
#     print(list2)
#     print(id(list2))
#     print(id(list3))
    i = -1
    for values in list1 :
        data1 = values
        data2 = list2[i]
        if data2 == None :
            data2 = ""
        if data1 == None :
            data1 = ""       
        data =  data1 + data2   
        i -= 1
    
        merged_data.append(data)
        
        
    
    for val in merged_data :
        val = val + " "
        resultant_data = resultant_data + val
    
    lent = len(resultant_data) - 1
    #print(resultant_data[:lent])
    return resultant_data[:lent]

#Provide different values for the variables and test your program
list1=['A', 'app','a', 'd', 'ke', 'th', 'doc', 'awa']
list2=['y','tor','e','eps','ay',None,'le','n']
merged_data=merge_list(list1,list2)
print(merged_data)












