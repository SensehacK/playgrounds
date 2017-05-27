'''
Created on Mar 15, 2017

@author: kautilya.save
'''

from classes import FoodModule
from utility import DBConnectivity

def checkout(username):
    print("****************CheckOut************************")
    print("Items added Successfully to the Cart !!!")
    print("Checkout in progress")
    print()
    
    print("Items Ordered")
    print("FoodName  \t Quantity")
    for index , value in FoodModule.Food.cart_dict.items() : 
        print(index , " \t " ,value)
        
    
    print()
    
    print("Please Select from the below menu ")
    print()
    
    
    checkout_final(username)


def checkout_final(username):
    checkout_choice = input("Do you wish to proceed for billing or cancelling any item or Save for later ? (Y/C/S) " )
    
    print("Your Selected Choice is ")
    print(checkout_choice)
    print()
    
    if checkout_choice == 'Y': 
        
        print("Hello checkout_choice == 'Y'")
        checkout_Yes(username)

    elif checkout_choice == 'C' :
        print("Hello checkout_choice == 'C'")
        checkout_Cancel(username)
        pass
    
    elif checkout_choice == 'S' :
        print("Hello checkout_choice == 'S'")
        checkout_Save(username)
        pass


def checkout_Yes(username):
    print("Checkout Yes")
    print("FoodName  \t Quantity")
    for index , value in FoodModule.Food.cart_dict.items() : 
        print(index , " \t " ,value)
        
    
    #Call Module 4 Billing
    
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        username = FoodModule.Food.registered_user
        #insert into checkoutcart(username ,foodname , quantity) values ('Kautilya','Masala', 200);
        for index , value in FoodModule.Food.cart_dict.items() :
            cur.execute("insert into checkoutcart(username ,foodname , quantity) values (:user_n, :food_n , :qty_ord)", {"user_n" : username, "food_n" : index , "qty_ord" : value})

    finally :
        print("Closing the cursor & connections in def checkout_Yes(username):")
        cur.close()
        con.commit()
        con.close()

def checkout_Cancel(username):
    print("checkout_Cancel")
    
    #Dictionary
    print("FoodName  \t Quantity")
    for index , value in FoodModule.Food.cart_dict.items() : 
        print(index , "  \t" ,value)
    
    food_name=input("Please select item for cancellation :")
    username = FoodModule.Food.registered_user

    itempop = FoodModule.Food.cart_dict.pop(food_name)
    print("Item popped " , itempop)
    
    #Dictionary
    print("FoodName  \t Quantity")
    for index , value in FoodModule.Food.cart_dict.items() : 
        print(index , "  \t" ,value)
    
    #Calling Functions
    checkout_final(username)

def checkout_Save(username):
    print("checkout_Save")
    print("Saving to Database Checkout Cart")
    
    #Dictionary
    print("FoodName  \t Quantity")
    for index , value in FoodModule.Food.cart_dict.items() : 
        print(index , " \t " ,value)
        
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        username = FoodModule.Food.registered_user
        #insert into checkoutcart(username ,foodname , quantity) values ('Kautilya','Masala', 200);
        for index , value in FoodModule.Food.cart_dict.items() :
            cur.execute("insert into checkoutcart(username ,foodname , quantity) values (:user_n, :food_n , :qty_ord)", {"user_n" : username, "food_n" : index , "qty_ord" : value})
        
        #Saving the flag for Direct Module 4 execution that The cart is been saved once for this registered user
        FoodModule.Food.is_cart_saved = True
    finally :
        print("Closing the cursor & connections in def checkout_Yes(username):")
        print("Item Saved Successfully!!!")
        cur.close()
        con.commit()
        con.close()
        

#print("Item Saved Successfully!!!")
    
