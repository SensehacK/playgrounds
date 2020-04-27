#PF-Exer-26

def factorial(number):
    fact = 1
    while number > 0 :
        fact = fact * number
        number -= 1
    return fact

def find_strong_numbers(num_list):

    strong_list = []
    
    for number_sel in num_list :
        sum = 0
        print(number_sel)
        temp = number_sel
        str_number = str(number_sel)
        length = len(str_number)
       
        while length > 0 :
            remainder = number_sel % 10
            print(remainder)
            number_sel = number_sel // 10
            
            print(factorial(remainder))
            fact = factorial(remainder)
            sum = sum + fact
            print(number_sel)
            print(sum)
            length -= 1
 
        if temp == sum :
            print("Strong Number", temp)
            strong_list.append(temp)
        else : 
            print("Not Strong Number", temp)

    print("Strong Number")
    return strong_list

num_list=[145,375,100,2,10]

strong_num_list=find_strong_numbers(num_list)
print(strong_num_list)
print("factorial(5)")
print(factorial(5))


num_list2=[0,2423,34232,5,10]
strong_num_list2=find_strong_numbers(num_list2)
print(strong_num_list2)