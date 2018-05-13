#PF-Assgn-44

def find_duplicates(list_of_numbers):
    #start writing your code here
    list_of_duplicates = []
    for number in list_of_numbers[:]:
        if list_of_numbers.count(number) > 1:
            list_of_duplicates.append(number)
            while number in list_of_numbers:
                list_of_numbers.remove(number)
    return list_of_duplicates

list_of_numbers=[1,2,3,3,2,1,4,4,4,1]  #[1,2,2,3,3,3,4,4,4,4]
list_of_duplicates=find_duplicates(list_of_numbers)
print(list_of_duplicates)