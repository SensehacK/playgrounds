#PF-Assgn-26

def solve(heads,legs):
    error_msg="No solution" 
    chicken_count=0
    rabbit_count=0

    #Start writing your code here
    print("heads")
    print(heads)

    print("legs")
    print(legs)
    
    #First remove rabbit 2 legs conclusion
    
    headsLegs_overall_noChicken = heads * 2
    print("headsLegs_overall_noChicken")
    print(headsLegs_overall_noChicken)
    
    heads_overall_chicken = legs - headsLegs_overall_noChicken
    if ( heads_overall_chicken == 0) :
        print("heads_overall_chicken == 0")
        heads_overall_rabbit = headsLegs_overall_noChicken // 2
        print("heads_overall_rabbit")
        print(heads_overall_rabbit)
        rabbit_count = heads_overall_rabbit
        print("rabbit_count")
        print(rabbit_count)
    
    
    
    
    print("heads_overall_chicken")
    print(heads_overall_chicken)
    #rabbit_count = heads_overall_chicken
    print("rabbit_count")
    print(rabbit_count)
    
    
    chicken_count_temp = heads_overall_chicken * 2
    print("chicken_count_temp")
    print(chicken_count_temp)
    
    chicken_count = chicken_count_temp // 4
    print("chicken_count")
    print(chicken_count)
    
    rabbit_count_legs_temp =  legs - chicken_count_temp
    print("rabbit_count_legs_temp")
    print(rabbit_count_legs_temp)
    
    rabbit_count = rabbit_count_legs_temp // 2
    print("rabbit_count")
    print(rabbit_count)
    
    if chicken_count_temp == legs  :
        print("if chicken_count == legs :")
        chicken_count = legs // 4
        print("chicken_count")
        print(chicken_count)
        print(rabbit_count)
        
     
       
     
    if heads_overall_chicken < 0 :
        print("heads_overall_chicken")
        print(heads_overall_chicken)
        rabbit_count_temp = heads_overall_chicken * 2
        print("rabbit_count_temp")
        print(rabbit_count_temp)
        
        
        if rabbit_count_temp == legs  :
            print("if rabbit_count_temp == legs  :")
            rabbit_count = legs // 2
            print("rabbit_count")
            print(rabbit_count)
    
    
    
   # if 
    
    
    
    print("rabbit_count")
    print(rabbit_count)
    print("chicken_count")
    print(chicken_count)
    
    
    #Populate the variables: chicken_count and rabbit_count



    # Use the below given print statements to display the output 
    # Also, do not modify them for verification to work

    #print(chicken_count,rabbit_count)
    #print(error_msg)

#Provide different values for heads and legs and test your program
solve(400,1020)

print("/////////////////////////////////")

solve(10,20)

print("/////////////////////////////////")

solve(20,10)

print("/////////////////////////////////")

solve(20,60)

print("/////////////////////////////////")

solve(35,94)
