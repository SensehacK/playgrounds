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
        print(index , "  " ,value)
        
    
    print()
    
    print("Please Select from the below menu ")
    print()
    
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
        print(index , "  " ,value)
        
    #insert into checkoutcart(username ,foodname , quantity) values ('Kautilya','Masala', 200);
    #Call Module 4 Billing
    
    pass
    
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        username = FoodModule.Food.registered_user
        print(username)
        print(type(username))
        for index , value in FoodModule.Food.cart_dict.items() :
            cur.execute("insert into checkoutcart(username ,foodname , quantity) values (:user_n, :food_n , :qty_ord)", {"user_n" : username, "food_n" : index , "qty_ord" : value})
        
        
        #cur.execute("select unique category_name from fooditem where restaurant_name=:rest_name",{"rest_name":restaurant_name})
        
        '''
        print("In function /get_restaurant_categories")
        print("executing the query for categories")
        print("Printing the tuples from query cursor directly")
        '''
    
    finally :
        print("Closing the cursor & connections in def checkout_Yes(username):")
        cur.close()
        con.commit()
        con.close()

def checkout_Cancel(username):
    print("checkout_Cancel")
    
    food_name=input(print("Please select item for cancellation"))
    username = FoodModule.Food.registered_user
    #Dictionary
    print("FoodName  \t Quantity")
    for index , value in FoodModule.Food.cart_dict.items() : 
        print(index , "  " ,value)
    
#     delete from checkoutcart where username = 'Kautilya' and foodname = 'Masala' ;    
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        
        for index , value in FoodModule.Food.cart_dict.items() :
                                                #where restaurant_name =:restaurant_n and category_name =:category_n",{"restaurant_n":restaurant_name, "category_n":category_name })
            cur.execute("delete from checkoutcart where username =:user_n and foodname =:food_n", {"user_n" : username, "food_n" : food_name})

    finally :
        print("Closing the cursor & connections in def checkout_Yes(username):")
        cur.close()
        con.commit()
        con.close()
    
    
def checkout_Save(username):
    print("checkout_Save")
    print("Saving to Database Checkout Cart")
    
    #Dictionary
    print("FoodName  \t Quantity")
    for index , value in FoodModule.Food.cart_dict.items() : 
        print(index , "  " ,value)
        
    
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        username = FoodModule.Food.registered_user
        print(username)
        print(type(username))
        for index , value in FoodModule.Food.cart_dict.items() :
            cur.execute("insert into checkoutcart(username ,foodname , quantity) values (:user_n, :food_n , :qty_ord)", {"user_n" : username, "food_n" : index , "qty_ord" : value})

    finally :
        print("Closing the cursor & connections in def checkout_Yes(username):")
        cur.close()
        con.commit()
        con.close()


print("Item Saved Successfully!!!")
    
