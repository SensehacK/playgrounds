'''
Created on Jan 31, 2017

@author: kautilya.save
'''

my_list = [220,10,1,2,3,4,5,6,10]
indexes = [4,5,6]

j = 0
sum1 = 0

for i in range(0,len(my_list)) :
    if i == indexes[j]:
        if j < (len(indexes)-1):
            j+=1
    else :
        sum1 += my_list[i]
        
print("sum1",sum1) 
        

    