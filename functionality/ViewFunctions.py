'''
Created on Mar 15, 2017

@author: kautilya.save
'''

from validations import Validate
from exceptions.CustomException2 import InvalidCategoryException, InvalidCatItemsException , Validate_item_present , Validate_item_available
from functionality import Checkout
from classes import FoodModule
from database import ViewDB

#Class Global Variables
#Creating list for taking multiple input from user for both Food items & Quantity required
category_items = []
category_items_quantity = []
category_item_name = ""
list_of_category = []
list_numbers = []

def view_category():
    try:
        global category_item_name
        global list_of_category
        global list_numbers
#         category_item_name = ""
        restaurant=input("Enter a Restaurant Name: ")
        print()
        
        #list_of_category_str = []
        FoodModule.Food.restaurant_name = restaurant
        
        #Calling Validate Function
        validate_restaurant_name(restaurant)
        
#         '''
#         Validate the user input
#         '''
#         
#         list_of_category=Validate.validate_view_category(restaurant)
#       
#         for i in range(1,len(list_of_category)+1) :
#             
#             list_numbers.append(i)
#         
#         #Using Zip Functionality for zipping two lists
#         print("Index ","Category")
#         for index , category in zip(list_numbers,list_of_category) :
#             print(index,"   " ,category)
#            
#         print()   

        #Asking for user for Category of his choice , will run till the given input is valid & return that valid input
        category_item_name = select_category_choice()

        print()
        print(category_item_name)
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

def validate_restaurant_name(restaurant):
    global list_of_category
    global list_numbers
    '''
    Validate the user input
    '''
    #Empty the list_numbers
    del list_numbers[:]

    list_of_category=Validate.validate_view_category(restaurant)
    for i in range(1,len(list_of_category)+1) :
        list_numbers.append(i)
    
    #Using Zip Functionality for zipping two lists
    print("Index ","Category")
    for index , category in zip(list_numbers,list_of_category) :
        print(index,"   " ,category)
       
    print()   

def select_category_choice():
    global list_of_category
    global list_numbers
    
    choice=input("Please Select The Category with its Corresponding Number ")
    v_choice = Validate.validate_input_is_decimal(choice)
    print(v_choice)
    print("len(list_of_category)")
    print(len(list_of_category))
    if v_choice == False:
        print("Please select from the given choices only")
        select_category_choice()
    else :
        if int(choice) <= len(list_of_category) and int(choice) >= 1 :
            for index in zip(list_numbers,list_of_category) :
                    if int(choice) == index[0] :
                        print("Choice Selected : ", index[0],"-", index[1])
                        return index[1]
        else : 
            print("Please select from the given choices only2")
            select_category_choice()

def view_category_items(category):
    global category_items
    global category_items_quantity
    
    try:   
        '''
        Validate the user input & get Restaurant name from Class Global Variables
        '''
        
        restaurant_name = FoodModule.Food.restaurant_name
        list_of_category_items=Validate.validate_view_category_items(category,restaurant_name)
        
#         print("Printing restaurant name accessed from FoodModule.Food.restaurant_name ")
#         print(restaurant_name)
#         print("After List_of_category_items=Validate.val")
        
        
        '''
        Print the food items details
        '''
        
        print("FoodName \t Price \t Availability")
        for item in list_of_category_items:
            print(item.get_food_name(),"\t",item.get_price(),"\t",item.get_availability())
        print()  
        
        '''
        Calling the function defined below
        '''
        
        enter_food_items()
        
        availability_view(category_items)
        
        enter_food_quantity()
    
        '''
        Printing Dictionary
        #print("Printing Dictionary")
        '''
        
        print("FoodName  \t Quantity")
        for index , value in FoodModule.Food.cart_dict.items() :
            print(index , "  \t" ,value)
        
        
        '''
         WIll call them later after debugging next function
        #Temporary hardcoding for easy debugging
#        username = "Kautilya"
#        Checkout.checkout(username)  
        '''
  
        '''
        Calling Class Checkout for further processing
         
        '''
        
        username = FoodModule.Food.registered_user
        Checkout.checkout(username)
        
        print()
        '''
        Handle all the exceptions that can occur
        '''   
       
        
    except InvalidCategoryException as e:
        print(e)
        
    except InvalidCatItemsException as e:
        print(e)
        
    except Exception as e:
        #Will edit the Error messages in View functions
        print("Sorry. Some system error occurred.")
        print(e)
        
    finally :
        pass
        #print("def view_category_items FINALLY ENDS")
    
    

def enter_food_items():
    global category_items
    
    #Getting valid item from the displayed items for the selected category
    item_selected=input("Enter a Items for order: ")
    print()
    
    print("Item Selected from the Menu : ")
    print(item_selected)
    
    #Splitting the item_selected with respect to multiple items selected
    category_items = item_selected.split(',')
    
    '''
        #print("In function def enter_food_items(category_items): ")
        #printing the list of multi selects or single selects using split
        print(category_items)
        print()
        
        Validate the Food Items enter_food_items input
           
    '''

    try :
        restaurant_name = FoodModule.Food.restaurant_name
        item_selected = Validate.validate_item_present(category_items,restaurant_name)
    
    except  Validate_item_present  as e:
        print(e)
        #Extra print
        #print(" The selected item is Not Available , Please Re-Enter Again")
        enter_food_items()
    
    finally :
        pass
        #print("Finally")
    
    
def availability_view(category_items): 
    
    '''
        Validate the Food Items Availability input
    '''
    global category_item_name
    #print("In function def availability_view(category_items): ")
    food_available = False
    restaurant_name = FoodModule.Food.restaurant_name
    try :
        
        food_available = Validate.validate_item_available(category_items,restaurant_name)
    
    except  Validate_item_available  as e:
        print(e)
        #print(" after e Selected item not Available!!! Please Select a different item")
        view_category_items(category_item_name)
    
    finally :
        pass
        #print("Finally")
        
#     print("food_available status")
#     print(food_available)
    
        
def enter_food_quantity():
    global category_items
    global category_items_quantity
    
    '''
    #Taking input for quantity of Food Items
    #Splitting the category with respect to multiple items selected or single item
    '''
    
    quantity_req = input("Enter a  quantity required : ")
    category_items_quantity = quantity_req.split(',')
    
    #Checking values returned are digits
    for number in category_items_quantity :
        if Validate.validate_input_is_decimal(number) == False  :
            enter_food_quantity()
        
        elif int(number) > 25 or int(number) < 1 :
                print("Please enter a Decimal Number in Range (1.. 25)!")
                enter_food_quantity()
            

    #print("Category name , Quantity")
    for category_index , quantity_item in zip(category_items , category_items_quantity) :
        
        #print(category_index ," ", quantity_item)
        FoodModule.Food.cart_dict[category_index] = quantity_item
    
    
    #print("def enter_food_quantity() ENDS")
    


