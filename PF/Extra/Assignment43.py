#PF-Assgn-43

def find_smallest_number(num):
    #start writing your code here
    if num == 0:
        return 0
    number = 1
    while True:
        count =  0
        for divisor in range(1,number+1):
            if number % divisor == 0:
                count = count + 1
        if count == num:
            return number
        number = number + 1
        
num=10
print("The number of divisors :",num)
result=find_smallest_number(num)
print("The smallest number having",num," divisors:",result)