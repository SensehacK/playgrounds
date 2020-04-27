'''
Created on Feb 16, 2017

@author: kautilya.save
'''

# 2 Logics created by me , 2nd one is more resource efficient



num1 = 9999999999
num1 = 6666666666
num1 = 1111191111
num1 = 2222222222
num1 = 7777777777
num_str = str(num1)
list1 = [1,2,3,4,5,6,7,8,9]
count = 0

for nu in list1 :
    flag_same = 0
    for char in num_str :
        if str(nu) == char :
            flag_same += 1
        else :
            flag_same -= 1
    
    if flag_same == 10 :
        print("Same numbers")
        print(num_str) 
    
# 
# num1 = 9199
# num_str = str(num1)
# num1_len = len(num_str)
# count = 0
# first_num = num_str[0]
# for value in num_str :
#     if first_num == value :
#         count += 1
# 
# 
# if count == num1_len :
#     print("Same digits")
# else :
#     print("false ")