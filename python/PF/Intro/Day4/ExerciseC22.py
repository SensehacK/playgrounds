#PF-Exer-22

def generate_ticket(airline,source,destination,no_of_passengers):
    ticket_number_list=[]
    
    greater_no_passenger = 0
    begg_num = 0
    begg_num2 = 101
    no_high = 4
    high_number = 101 + (no_of_passengers-1)
    print("high_number")
    print(high_number)
    #Write your logic here
    if no_of_passengers > 5 :
        begg_num_passenger = no_of_passengers - 5
        print("begg_num_passenger")
        print(begg_num_passenger)
        greater_no_passenger = 1
        print("greater_no_passenger = 1")
        
    else : 
        begg_num_passenger = 0
        greater_no_passenger = 0
        print("greater_no_passenger = 0")
    

    while no_of_passengers > begg_num_passenger :
        
        if greater_no_passenger == 1 : 
            
            print("high_number")
            print(high_number)
            
            print("no_high_number")
            print(no_high)
            
            begg_num = high_number - (no_high)
            print(begg_num)
            str_num  = str(begg_num)
            #str_num  = str(begg_num2)
        
            ticket_number_list.append(airline + ":" + source[0:3] + ":"+ destination[0:3] + ":" + str_num)
            no_high -= 1
            #begg_num2 += 1
        #begg_num += 1
        
            no_of_passengers -= 1
            
        if greater_no_passenger == 0 :
            print("if greater_no_passenger == 0 :")
            print("else Block")
        
            print("high_number")
            print(high_number)
        
            begg_num2 = 101
            print("begg_num2")
            print(begg_num2)

            while no_of_passengers > 0 :
                str_num  = str(begg_num2)
                print(str_num)
                print("while no_of_passengers > 0 ")
                ticket_number_list.append(airline + ":" + source[0:3] + ":"+ destination[0:3] + ":" + str_num)
           
                begg_num2 += 1
                print("begg_num2")
                print(begg_num2)
            
                print(" no_of_passengers ")
                print(no_of_passengers)
            
                no_of_passengers -= 1


    #Use the below return statement wherever applicable
    return ticket_number_list

#Provide different values for airline,source,destination,no_of_passengers and test your program
print("////////////////////////////////////////////")
print(generate_ticket("AI","Bangalore","London",7))

print("////////////////////////////////////////////")
print(generate_ticket("AI","Mumbai","NewYork",3))

print("////////////////////////////////////////////")
print(generate_ticket("AI","Bangalore","Sydney",5))


print("////////////////////////////////////////////")
print(generate_ticket("AI","Bangalore","Sydney",8))

