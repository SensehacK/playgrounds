'''
Created on Mar 15, 2017

@author: kautilya.save
'''
from classes import FoodModule


def checkout(username):
    
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
    
    #Call Module 4 Billing
    
    pass
    

def checkout_Cancel(username):
    print("checkout_Cancel")
    
    print("Please select item for cancellation")
    
    pass
    
    
def checkout_Save(username):
    print("checkout_Save")
    print("Saving to Database Checkout Cart")
    
    #Dictionary
    print("FoodName  \t Quantity")
    for index , value in FoodModule.Food.cart_dict.items() : 
        print(index , "  " ,value)
    pass


print("Item Saved Successfully!!!")
    
