#PF-Assgn-19

def calculate_bill_amount(food_type,quantity_ordered,distance_in_kms):
    bill_amount=0
    food_plate = 0
    overall_charge = 0
    delivery_charge = 0
    #write your logic here
    
    print("hello3")
    if food_type != "N" and food_type != "V" or quantity_ordered < 1 or distance_in_kms <= 0 :
        print("hello2")
        bill_amount = -1
        return bill_amount
        
    else :
        print("hello")
        if distance_in_kms <= 3 :
            print("hello")
            delivery_charge = 0
            overall_charge = delivery_charge
        
        elif distance_in_kms > 3 and distance_in_kms <= 6 :
            
            delivery_charge = 3
            distance_in_kms = distance_in_kms - 3
            overall_charge = distance_in_kms * 3
    
        else :
            print("hello5")
            distance_in_kms = distance_in_kms - 3
            remaining_lastDistance = 0
            first_delivery_charge = 0
            remaining_delivery_charge = 0
            
            #extra_distance = distance_in_kms
        
            if distance_in_kms > 3 :
                print("hello6")
                #first_distance_cut = distance_in_kms
                first_delivery_charge = 3 * 3
                remaining_lastDistance = distance_in_kms - 3
                remaining_delivery_charge = remaining_lastDistance * 6
                
        
            else :
                    
                    remaining_delivery_charge = distance_in_kms * 3
                    #first_delivery_charge = 6 * 3
                    #remaining_distance = distance_in_kms - 6
            
            print("Overall Charge")
            overall_charge = first_delivery_charge + remaining_delivery_charge
            print(overall_charge)
        
        
        
        if food_type == "N" :
            food_plate = 150
            bill_amount = food_plate * quantity_ordered + overall_charge
        
        else :           
            food_plate = 120
            bill_amount = food_plate * quantity_ordered + overall_charge

                        
                        
                        
    return bill_amount

#Provide different values for food_type,quantity_ordered,distance_in_kms and test your program
bill_amount=calculate_bill_amount("N",2,7)
print(bill_amount)