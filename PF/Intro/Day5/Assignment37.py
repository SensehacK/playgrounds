#PF-Assgn-37

#Global variables
#Tuples 
#child_id=(10,20,30,40,50)
#child_id =(11,12,13,14,15)
#child_id =(101,201,301,401,501)
child_id = (11,12,13,14,15)
#chocolates_received=[10,5,3,2,4]
chocolates_received=[22,33,44,55,66]

def calculate_total_chocolates():
    sum = 0
    for chocolate in chocolates_received :
        sum = sum + chocolate
    return sum

def reward_child(child_id_rewarded,extra_chocolates):
    flag = False
    flag_extraC = False
    if extra_chocolates < 1 :
            flag_extraC = True
            print("Extra chocolates is less than 1")
            
    if flag_extraC == False : 
        for i in range(0 , len(child_id)) :
                if child_id_rewarded == child_id[i] :
                    flag = True
                    chocolates_received[i] = chocolates_received[i] + extra_chocolates
        if flag == False :
            print("Child id is invalid")          
        else :
            print(chocolates_received)
        
print(calculate_total_chocolates())
#reward_child(11,-2)
#reward_child(201,2)
reward_child(20,5)