#PF-Assgn-52

def sum_of_numbers(list_of_num,filter_func=None):
    total_sum = 0
    for i in list_of_num :
        if filter_func == None :
            total_sum += i
        else :
            if filter_func(i) :
                total_sum += i
    return total_sum
def even(data):
    if data % 2 == 0 :
        return data
def odd(data):
    if data % 2 != 0 :
        return data
sample_data = range(1,11)
print(sum_of_numbers(sample_data,even))
