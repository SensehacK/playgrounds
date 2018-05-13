#PF-Assgn-54
def check_anagram(data1,data2):
    count = 0
    lenth = len(data1)
    data1 = data1.lower()
    data2 = data2.lower()
    if len(data1) != len( data2) :
        return False
    if sorted(data1) != sorted(data2) :
        return False   
    for i1 , j1 in zip (data1, data2) :
        if i1 == j1 :
            return False

    return True
    
#     for i in range(0,len(data1)) :
#         for j in range(0,len(data2)) :
#             if data1[i] == data2[j] :
#                 count += 1



#print(check_anagram("backward","drawback")) 
print(check_anagram("EAT","tea"))
#print(check_anagram("listen", "silent"))
#print(check_anagram("About", "table"))  
#print(check_anagram("eat","tea"))