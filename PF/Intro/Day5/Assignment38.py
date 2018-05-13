#PF-Assgn-38

def check_double(number):
   
    print(number)
    double_number = number + number 
    print(double_number)
    str_num = str(number)
    str_double = str(double_number)
    count_one = 0
    my_list  = []
    flag_once = False
    for i in str_num :
        #print(i)
        count_one = 0 
        #count2 = 0
        for j in range ( 0 , len(str_double)) :
            
            print("str_double[j]")
            print(str_double[j])
            print(i)
            if i == str_double[j] :
                print("ze")
                count_one += 1
                my_list.append(count_one)
                

    print(my_list)
    
    for i in range(0,len(my_list)) :
        print(i)
        print(my_list[i])
        if my_list[i] == 1 :
            print("Hello")
            if  len(my_list) == len(str_num) :
                flag_once = True
            else :
                flag_once = False
        else :
            flag_once = False
            
    
    if flag_once :
        print(double_number)
        return flag_once
    else :
        print("Not Equal")
        return flag_once


#Provide different values for number and test your program
print(check_double(125874))
print(check_double(245))
