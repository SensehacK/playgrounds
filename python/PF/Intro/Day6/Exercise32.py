#PF-Exer-32

def human_pyramid(no_of_people):
    pass #remove pass and place the recursive code the you had written earlier for this function

    if (no_of_people == 1) :
        return 1*50
    else :
        return no_of_people*(50)+human_pyramid(no_of_people-2)
    
    
def find_maximum_people(max_weight):
    no_of_people=1
    #write your logic here. You may invoke recursive function human_pyramid() wherever applicable 
    while (1) :
        no_of_people+= 2
        possible_weight = (human_pyramid(no_of_people))
        
        if possible_weight > max_weight :
            no_of_people -=2
            break
    return no_of_people

        
    
#     no_of_people = max_weight // 50
#     print(no_of_people)
#     print("human_pyramid(no_of_people)")
#     human_pyramid(no_of_people)
#     
#     return no_of_people


#Provide different values for max_weight and test your program
max_people=find_maximum_people(1000)
print(max_people)