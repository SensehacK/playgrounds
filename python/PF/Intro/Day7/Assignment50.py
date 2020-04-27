#PF-Assgn-50

def sms_encoding(data):
    
    #print("Hello Sensehack")        
    data_return = []
    vowels = ['a' , 'e' ,'i' ,'o' ,'u' ]
    
    #if data.lower 
#     data2 = data
#     print(data2)
    upper = False
    data_lower = data
    #print(data_lower)
    #print(data)
#     if data.isupper() :
#         data_lower = data.lower()
#         upper = True
        
    data_return = data_lower.split()
    str_main = ""
    for i in data_return :
        j = 0
        st = ""
        for j in range(len(i)) :
            if (i[j] == "a" or i[j] == "e" or i[j] == "o"  or i[j] == "u" or  i[j] == "i"  or i[j] == "A" or  i[j] == "E" or  i[j] == "O" or  i[j] == "U"   ) :
                continue
            else :
                st = st + i[j]
        str_main = str_main + " "  + st        
    str_main = str_main.replace(" ", "",1)
    #str_main = str_main.replace("  ", " ")
    
    # Revert back to Upper case by checking the flag
    if upper :
        return str_main.upper()
    else :
        return str_main
    

# /////////////////////////// Old method program ////////////////

#     for i in data :
#         temp = data.replace("a", "")
#         temp2 = temp.replace("e", "")
#         temp3 = temp2.replace("i", "")
#         temp4 = temp3.replace("u", "")
#         temp5 = temp4.replace("o", "")
#     data_return.append(temp5)  
#     return temp5
# import itertools
# list1 = (itertools.permutations([4,22,43,14], 2))
# 
# for va in list1 :
#     print(va)
#     


           
        
#data="I love Python"
#data="Life is beautiful"
data="Have a nice day"
#data="MSD says I love cricket and tennis too"

 
#data="GOOD DAYS AND BAD DAYS"
 
print(sms_encoding(data)) 