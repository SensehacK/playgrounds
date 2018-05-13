#DSA-Exer-16

def find_decreasing_start(list1,start,end):
    #Remove pass and write your logic here
    j = 1
    for index in range(len(list1)) :
        if list1[j] < list1[index] :
            return j 
        j += 1
    
#Use different values for list1 and test your program
list1=[1,4,7,8,9,5,4]
start=0
end=len(list1)-1
result=find_decreasing_start(list1,start,end)
print("The index position at which the increasing array starts decreasing is:",result)
