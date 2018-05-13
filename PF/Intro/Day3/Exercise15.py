#PF-Exer-15

def find_sum_of_digits(number):
    sum_of_digits=0
    loop1 = 0
    #Write your logic here

    
    #print(i)
    while(number > 0) :
        
        print("Loop", loop1)
        
        '''
        print(number)
        last_number = number % 10
        print(last_number)

        second_last_number = number % 100
        print(second_last_number)
        second_last_number = second_last_number//10
        print(second_last_number)

        third_last_number = number//100
        print(third_last_number)
        '''
        
        print(number)
        remainder = number % 10
        print(remainder)
        number = number // 10
        print(number)
        print("Sum before " ,sum_of_digits)
        sum_of_digits = sum_of_digits + remainder
        print("Sum after " , sum_of_digits)
        
        
        loop1 += 1
    
    
    #sum_of_digits = last_number + second_last_number + third_last_number
    return sum_of_digits

#Provide different values for number and test your program
sum_of_digits = find_sum_of_digits(245343253)
print("Sum of digits:",sum_of_digits)