'''
Created on Jan 24, 2017

@author: kautilya.save
'''

# Direct assigned parameters 
def find_sum (num1 , num2):
    print(num2)
    return num1 + num2

print(find_sum(num2=10, num1 = 15))


def find_sum2 (num1 , *num2):
    print(num2)
    sum = 0
    for i in num2 :
        sum = sum + i
        print(sum , "iteration" , i)
    print(sum)  
    print("/////////////////////////////////////////")  
    sum2 = 0 
    for i2 in range(0,len(num2)) :
        sum2 = sum2 + num2[i2]
        print(sum2 , "iteration" , i2)
    
    print(sum2 + num1)
    print(sum2 + sum)
    return sum + num1

print(find_sum2(100 , 20,40,45,65,6,45,34))













