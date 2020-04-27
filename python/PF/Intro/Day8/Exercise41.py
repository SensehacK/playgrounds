
#PF-Exer-41
#This verification is based on string match.

def sum_all(function, data):
    total_sum = 0 
    normal_sum = 0
    for d in data :
        if function(d) :
            normal_sum = normal_sum + d
        #total_sum = total_sum + normal_sum
    return normal_sum


#list_of_nos=[1,3,4,5,6,7,8,9,10,15,20,30,110]
list_of_nos = [100,200,300,500,1040]
#list_of_nos = [25,26,27,28,29,30,147,187]

greater = lambda x : x > 10

divide = lambda x : (x % 10 == 0) and (x <= 100)

range_of_values = lambda x : (x >= 25) and (x <= 50)


#Use the below given print statements to display the output
# Also, do not modify them for verification to work
print(sum_all(greater,list_of_nos))
print(sum_all(divide,list_of_nos))
print(sum_all(range_of_values,list_of_nos))