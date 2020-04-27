'''
Created on Jan 30, 2017

@author: kautilya.save
'''


my_dict = {"100" : "Ramesh" , "101" : "Naresh" ,"102" : "Suresh" ,"103" : "Jayesh" ,"104" : "Durgesh"}


#print(my_dict)

list1 = ["a" , "b" , "c" , "d" , "e"] 
my_dict2 = {}

for l in list1 :
    for i in range(5) :
        my_dict2[l] = i+2

    
    
print(list1)


print(my_dict2)
    
#     
# for keys , values in my_dict.items() :
#     print(keys)
#     print(values)
#     
    