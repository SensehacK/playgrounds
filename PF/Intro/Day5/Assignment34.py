#PF-Assgn-34
def find_pairs_of_numbers(num_list,n):
    count_sum = 0
    for i in range(0 , len(num_list)) :
        for j in range(i, len(num_list)-1) : 
            sum2 = num_list[i] + num_list[j+1]
            
            if sum2 == n :
                count_sum +=1
    return count_sum

num_list=[1, 2, 4, 5, 6]
n=6
print(find_pairs_of_numbers(num_list,n))