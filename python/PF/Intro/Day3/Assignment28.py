#PF-Assgn-28

def find_max(num1, num2):
    max_num=-1
    my_list = []
    
    
    
    if num1 < num2 :
        
        
        while (num1 <= num2) :
            
            num1_temp = num1 % 10
            print("num1_temp")
            print(num1_temp)
            
            num1_temp2 = num1 // 10
            print("num1_temp2")
            print(num1_temp2)
            
            
            sum_num1 = num1_temp + num1_temp2
            
            print("sum_num1")
            print(sum_num1)
            
            sum_nums = num1 + num2 
            
            print("sum_nums")
            print(sum_nums)
            
            
            if sum_num1 % 3 == 0 and num1 % 5 == 0 and sum_nums <=198 and sum_nums >=18 :
                
                print("sum_num1")
                print(sum_num1)
                
                print("number1")
                print(num1)
                my_list.append(num1)
                
                
                max_num = num1
                
            num1 += 1
            
            print("my_list")
            print(my_list)  
                
    
    # Write your logic here
    return max_num



#Provide different values for num1 and num2 and test your program.
max_num=find_max(10,87)
print(max_num)