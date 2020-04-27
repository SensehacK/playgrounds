#PF-Assgn-16
def make_amount(rupees_to_make,no_of_five,no_of_one):
    #five_needed=0
    one_needed=0
     

    #Start writing your code here
    #Populate the variables: five_needed and one_needed
    print(no_of_five)
    print(no_of_one)
    five_needed = rupees_to_make // 5
    print(five_needed)
    print(one_needed)
    one_needed = rupees_to_make % 5
    
    if no_of_five < five_needed :
        print("if no_of_five < five_needed :")
        print(five_needed)
        print(one_needed)
        
        five_required = five_needed - no_of_five
        print("five Required")
        print(five_required)
        five_converted_one = no_of_one // 5
        print("five_converted_one")
        print(five_converted_one)
        if five_converted_one >= five_required :
            no_of_one = five_required * 5
            print(no_of_one)
            print(" No. of Five needed :", no_of_five,"No. of One needed :" , no_of_one)


    elif no_of_five >= five_needed and no_of_one >= one_needed : 
        print("1st Statement")
        print(" No. of Five needed :", five_needed,"No. of One needed :" , one_needed)
        
    elif five_needed == 0 and no_of_one >= one_needed :
       
        print(" No. of Five needed :", five_needed,"No. of One needed :" , one_needed)
        
    elif five_needed < no_of_five and no_of_one >= one_needed :
        print(" No. of Five needed :", five_needed, "No. of One needed :" , one_needed)
        
    else :
        print(-1)
        
#Provide different values for rupees_to_make,no_of_five,no_of_one and test your progra

make_amount(138,81,51)
print("Second input")
make_amount(118,24,4)
print("Third input")
make_amount(4,3,23)
print("Fourth input")
make_amount(110,21,8)

print("///////////////////////////////////////////")

print("Fifth input")
make_amount(100,21,5)


print("///////////////////////////////////////////")

print("sixth input")
make_amount(16,1,15)

