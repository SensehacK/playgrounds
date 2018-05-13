#PF-Exer-35

def count_names(name_list):
    count1=0
    count2=0
    count3=0
    for i in name_list :
        if i[1:] == "at" :
            count1 += 1
        if i.count('at') :
            count3 +=1
        if "at" in i :
            #print(i)
            count2 += 1
    print("_at -> ",count1)
    print("%at% -> ",count2)
    #print(count3)

#Provide different names in the list and test your program
#name_list=["Hat","Cat","rabbit","matter"]
name_list =["GOAT","atter","at"]
count_names(name_list)