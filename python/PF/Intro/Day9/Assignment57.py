#PF-Assgn-57
from itertools import count

def check_prime(number):
    for i in range(2,number):
        if number % i == 0 :
            return False 
        return  True
    
def rotations(num):
    answer_list = []
    num_str = str(num)
    while int(num_str) not in answer_list:
        answer_list.append(int(num_str))
        num_str=num_str[1:] + num_str[0]
    return answer_list
    
    
def get_circular_prime_count(limit):
    count = 0
    for i in range(2,limit):
        list1 = rotations(i)
        for j in range(len(list1)):
            status = check_prime(list1[j])
            if status==False :
                break
        if status :
            count+=1
    return count

#Provide different values for limit and test your program
print(get_circular_prime_count(1000))

    
    
    

    