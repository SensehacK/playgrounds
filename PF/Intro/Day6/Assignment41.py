#PF-Assgn-41
def find_ten_substring(num_str):
    ten_list = []
    count = 0
    
    for i,num1 in enumerate(num_str[:-1]):
        sum_now= int(num1)
        for j,num2 in enumerate(num_str[i+1:]):
            sum_now+=int(num2)
            if sum_now==10:
                ten_list.append(num_str[i: i + j+2])
                
#     for i in range(0,len(num_str)-2) :
#         sum = int(num_str[i])
#         for j in range(i+1, len (num_str)-1) : 
#             sum = sum + int(num_str[j])
#             count+=1
#             if sum == 10 :
#                 ten_list.append(num_str[i: i+ j+2])
    return ten_list            


num_str="2825302"
print("The number is:",num_str)
result_list=find_ten_substring(num_str)
print(result_list)