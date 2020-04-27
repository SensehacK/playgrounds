#PF-Assgn-41
def find_ten_substring(num_str):
    #Remove pass and write your logic here
    result_list = []
    for index, num in enumerate(num_str[:-1]):
        sum_upto_now = int(num)
        for next_index, next_num in enumerate(num_str[index+1:]):
            sum_upto_now = sum_upto_now + int(next_num)
            if sum_upto_now == 10:
                result_list.append(num_str[index: index + next_index + 2])
    return result_list

num_str="2825302"
num_str = "3523014"
print("The number is:",num_str)
result_list=find_ten_substring(num_str)
print(result_list)