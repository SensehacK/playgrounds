#PF-Assgn-36
def create_largest_number(number_list):
    
    print("number_list bEfore")
    print(number_list)
    i = 0
    j = i + 1
    
    for i in range (0 , len(number_list)) :
        for j in range(i, len(number_list)) :
            if number_list[i] < number_list[j] :
                temp = number_list[i]
                number_list[i] = number_list[j]
                number_list[j] = temp
    
    print("number_list after")        
    print(number_list)

    sum = ""
    for k in range(0, len(number_list)) :
        
        str_len = str(number_list[k])
        print(str_len)
        sum = sum + str_len
        print(sum)
        largest_number = int(sum)
    return largest_number


#         print(number_list[k])
#         sum = "sum" + number_list[k]
#         print(number_list[k+1])
#         gest_number = number_list[k] + number_list[k+1]
#         print(gest_number)
#         largest_number = largest_number + gest_number
#         print(largest_number)

number_list=[23,45,67]
largest_number=create_largest_number(number_list)
print(largest_number)