#PF-Assgn-29
def calculate(distance,no_of_passengers):
    
    #Remove pass and write your logic here
    Price_per_litre= 70
    Mileage = 10
    Price_ticket = 80
    
    profit = (no_of_passengers*Price_ticket) - ((distance / 10 ) * 70 )
    
    if profit > 0 :
        return profit
    else : 
        return -1


#Provide different values for distance, no_of_passenger and test your program   
distance=20
no_of_passengers=50
print(calculate(distance,no_of_passengers))