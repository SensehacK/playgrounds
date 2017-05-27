'''
Created on Mar 15, 2017

@author: kautilya.save
'''

from validations import Validate
from exceptions.CustomException2 import InvalidCategoryException, InvalidCatItemsException , Validate_item_present , Validate_item_available
from functionality import Checkout
from classes import FoodModule
from database import ViewDB

#Global Variables
#Creating list for taking multiple input from user for both Food items & Quantity required
category_items = []
category_items_quantity = []
category_item_name = ""


def view_category():
    try:
        global category_item_name
        restaurant=input("Enter a Restaurant Name: ")
        print()
        list_numbers = []
        #list_of_category_str = []
        FoodModule.Food.restaurant_name = restaurant
        
        '''
        Validate the user input
        '''
        
        list_of_category=Validate.validate_view_category(restaurant)
        
        length_categories = len(list_of_category)
        
        for i in range(1,length_categories+1) :
            
            list_numbers.append(i)
        
        #Using Zip Functionality for zipping two lists
        print("Index ","Category")
        for index , category in zip(list_numbers,list_of_category) :
            print(index,"   " ,category)
           
        print()   
        
        choice=input("Please Select The Category with its Corresponding Number ")
        
        if(choice=="1"):
            #Converting to int for easy manipulation
            category_item = int(choice)
            #Storing the name from displayed items for specific category
            category_item_name = list_of_category[category_item-1]
            print("Choice Selected :" , choice , category_item_name)
            FoodModule.Food.category = category_item_name

            
        elif(choice=="2"):
            #Converting to int for easy manipulation
            category_item = int(choice)
            #Storing the name from displayed items for specific category
            category_item_name = list_of_category[category_item-1]
            print("Choice Selected :" , choice , category_item_name)
            FoodModule.Food.category = category_item_name
            
        elif(choice=="3"):
            #Converting to int for easy manipulation
            category_item = int(choice)
            #Storing the name from displayed items for specific category
            category_item_name = list_of_category[category_item-1]
            print("Choice Selected :" , choice , category_item_name)
            FoodModule.Food.category = category_item_name

        
        elif(choice=="4"):
            #Converting to int for easy manipulation
            category_item = int(choice)
            #Storing the name from displayed items for specific category
            category_item_name = list_of_category[category_item-1]
            print("Choice Selected :" , choice , category_item_name)
            FoodModule.Food.category = category_item_name


        elif(choice=="5"):
            #Converting to int for easy manipulation
            category_item = int(choice)
            #Storing the name from displayed items for specific category
            category_item_name = list_of_category[category_item-1]
            print("Choice Selected :" , choice , category_item_name)
            FoodModule.Food.category = category_item_name
            
            
        elif(choice=="6"):
            #Converting to int for easy manipulation
            category_item = int(choice)
            #Storing the name from displayed items for specific category
            category_item_name = list_of_category[category_item-1]
            print("Choice Selected :" , choice ,":", category_item_name)
            FoodModule.Food.category = category_item_name
            
        
        print()
        #Calling def view_category_items(category): with parameter
        view_category_items(category_item_name)    
        
        '''
        Handle all the exceptions that can occur
        '''
        
    except InvalidCategoryException as e:
        print(e)
    except Exception as e:
        print("Sorry. Some system error occurred")
        print(e)
    print()
    
    
def view_category_items(category):
    global category_items
    global category_items_quantity
    
    try:   
        
        restaurant_name = FoodModule.Food.restaurant_name
        print("Printing restaurant name accessed from FoodModule.Food.restaurant_name ")
        print(restaurant_name)
        
        '''
        Validate the user input
        '''
        list_of_category_items=Validate.validate_view_category_items(category,restaurant_name)
        
        print("After List_of_category_items=Validate.val")
        
        '''
        Print the details
        '''
        
        print("FoodName \t Price \t Availability")
        for item in list_of_category_items:
            print(item.get_food_name(),"\t",item.get_price(),"\t",item.get_availability())
        print()  
        
        #Calling the function defined below
        enter_food_items()
        
        #Calling the function defined below
        availability_view(category_items)
        
        #Calling the function defined below
        enter_food_quantity()
    
        print("Printing Dictionary")
        print("FoodName  \t Quantity")
        for index , value in FoodModule.Food.cart_dict.items() :
            
            print(index , "  " ,value)
        ''' WIll call them later after debugging next function '''
        
        username = FoodModule.Food.registered_user
        Checkout.checkout(username)
        
        #Temporary hardcoding for easy debugging
#         username = "Kautilya"
#         
#         Checkout.checkout(username)   
        '''
        Handle all the exceptions that can occur
        '''   
        print()
        
    except InvalidCategoryException as e:
        print(e)
        
    except InvalidCatItemsException as e:
        print(e)
        
    except Exception as e:
        print("Sorry. Some system error occurred in View functions")
        print(e)
        
    
    finally :
        print("def view_category_items FINALLY ENDS")
    
    

def enter_food_items():
    global category_items
    global category_items_quantity
    
    #Getting valid item from the displayed items for the selected category
    item_selected=input("Enter a Items for order: ")
    print()
    
    print("item_selected")
    print(item_selected)
    
    #Splitting the item_selected with respect to multiple items selected
    category_items = item_selected.split(',')
    
    #printing the list of multi selects or single selects using split
    print(category_items)
    print()
    
    
    '''
        Validate the Food Items enter_food_items input
    '''
    print("In function def enter_food_items(category_items): ")
    
    try :
        item_selected = Validate.validate_item_present(category_items)
    
    except  Validate_item_present  as e:
        print(e)
        print(" The selected item is Not Available , Re-Enter Again")
        enter_food_items()
    
    finally :
        print("Finally")
    
    
def availability_view(category_items): 
    
    '''
        Validate the Food Items Availability input
    '''
    
    print("In function def availability_view(category_items): ")
    food_available = False
    try :
        food_available = Validate.validate_item_available(category_items)
    
    except  Validate_item_available  as e:
        print(e)
        print(" after e Selected item not Available!!! Please Select a different item")
        view_category_items(category_item_name)
    
    finally :
        print("Finally")
        
    #food_available = ViewDB.get_food_items_availability(category_items)
    print("food_available")
    print(food_available)
    
        
def enter_food_quantity():
    global category_items
    global category_items_quantity
    
    quantity_req = input("Enter a  quantity required : ")
        #Splitting the category with respect to multiple items selected
    category_items_quantity = quantity_req.split(',')
    
    print("category_index , quantity_item")
    for category_index , quantity_item in zip(category_items , category_items_quantity) :
        
        print(category_index ," ", quantity_item)
        FoodModule.Food.cart_dict[category_index] = quantity_item
    
    print("def enter_food_quantity() ENDS")
    


