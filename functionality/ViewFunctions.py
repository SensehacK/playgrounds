'''
Created on Mar 15, 2017

@author: kautilya.save
'''

from validations import Validate
from exceptions.CustomException2 import InvalidCategoryException, InvalidCatItemsException
from functionality import Checkout

def view_category():
    try:
        restaurant=input("Enter a Restaurant Name: ")
        print()
        list_numbers = []
       
        '''
        Validate the user input
        '''
        list_of_category=Validate.validate_view_category(restaurant)
        
        '''
        Print the details
        '''
        
        
        print()
        length_categories = len(list_of_category)
        print("Length of Categories " , length_categories)
        print()
        print("Printing list _ numbers auto generated for easy linking of numbers")
        for i in range(1,length_categories+1) :
            list_numbers.append(i)
    
        # Printing index numbers
#         print(list_numbers)
        
        print("After Validation now printing in for loop")
        print()
        print("Using Zip Functionality for zipping two lists")
        #Using Zip Functionality for zipping two lists
        for index , category in zip(list_numbers,list_of_category) :
            print("Index ","Category")
            print()
            print(index,category)
            print()
        
        
        # Duplicate printing of categories again
#         for category in list_of_category :
#             print(category)
           
        print()   
        
        
        
        choice=input("Please Select The Category, Enter Corresponding Number ")
        
        if(choice=="1"):
            print("Choice Selected = 1")
            
            category_item=input("Enter the Category ID")
            
            
            '''
            Here we are invoking a dummy function and passing the data to it.
            This dummy function has to be completed by another programmer.
            '''
        elif(choice=="2"):
            print("Choice Selected = 2")
            category_item=input("Enter the Category ID")
            
            '''
            Here we are invoking a dummy function and passing the data to it.
            This dummy function has to be completed by another programmer.
            '''
        elif(choice=="3"):
            print("Choice Selected = 3")
            category_item=input("Enter the Category ID")
            
            '''
            Here we are invoking a dummy function and passing the data to it.
            This dummy function has to be completed by another programmer.
            '''
        
        elif(choice=="4"):
            print("Choice Selected = 4")
            category_item=input("Enter the Category ID")
            
            '''
            Here we are invoking a dummy function and passing the data to it.
            This dummy function has to be completed by another programmer.
            '''
        
        elif(choice=="5"):
            print("Choice Selected = 5")
            category_item=input("Enter the Category ID")
            
            '''
            Here we are invoking a dummy function and passing the data to it.
            This dummy function has to be completed by another programmer.
            '''
        
        elif(choice=="6"):
            print("Choice Selected = 6")
            category_item=input("Enter the Category ID")
            
            '''
            Here we are invoking a dummy function and passing the data to it.
            This dummy function has to be completed by another programmer.
            '''
            
        view_category_items(category_item)    
        
        #Temporary hardcoding for easy debugging
        username = "Kautilya"
        
        Checkout.checkout(username)
            
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
    try:
        
        
        '''
        Validate the user input
        '''
        list_of_category_items=Validate.validate_view_category_items(category)
        
        '''
        Print the details
        '''
        
        for product in list_of_category_items:
            print(product.get_product_id()," ",product.get_product_name()," ",product.get_price())
        print()  
        
        
        # Creating list for taking multiple input from user for both Food items & Quantity required
        category_items = []
        category_items_quantity = []
        
        
        #Getting valid item from the displayed items for the selected category
        item_selected=input("Enter a Items for order: ")
        print()
        
        #Splitting the item_selected with respect to multiple items selected
        category_items = item_selected.split(',')
        
        #printing the list of multi selects or single selects using split
        print(category_items)
        print()
        
        quantity_req = input("Enter a  quantity required : ")
        #Splitting the category with respect to multiple items selected
        category_items_quantity = quantity_req.split(',')
        
        cart_dict = {}
        
        for category_index , quantity_item in zip(category_items , category_items_quantity) :
            print("category_index , quantity_item")
            print(category_index ," ", quantity_item)
            cart_dict[category_index] = quantity_item
            
        print()   
       
        category_id = 
        Checkout.checkout(category_id)
            
        '''
        Handle all the exceptions that can occur
        '''   
    except InvalidCategoryException as e:
        print(e)
    except Exception as e:
        print("Sorry. Some system error occurred")
        print(e)
    print()