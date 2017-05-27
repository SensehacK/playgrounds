'''
Created on Mar 15, 2017

@author: kautilya.save
'''

from validations import Validate
from exceptions.CustomException2 import InvalidCategoryException, InvalidCatItemsException
from functionality import Checkout

def view_category():
    try:
        restaurant=input("Enter a category: ")
        print()
        
        '''
        Validate the user input
        '''
        list_of_category=Validate.validate_view_category(restaurant)
        
        '''
        Print the details
        '''
        for index , category in list_of_category:
            print(index ," ", category)
            
        print()   
        
        
        
        choice=input("Please Select The Category. Enter Corresponding Number ")
        
        if(choice=="1"):
            category_id=input("Enter the Category ID")
            print("Choice Selected = 1")
            '''
            Here we are invoking a dummy function and passing the data to it.
            This dummy function has to be completed by another programmer.
            '''
        elif(choice=="2"):
            category_id=input("Enter the Category ID")
            print("Choice Selected = 2")
            '''
            Here we are invoking a dummy function and passing the data to it.
            This dummy function has to be completed by another programmer.
            '''
        elif(choice=="3"):
            category_id=input("Enter the Category ID")
            print("Choice Selected = 3")
            '''
            Here we are invoking a dummy function and passing the data to it.
            This dummy function has to be completed by another programmer.
            '''
        
        elif(choice=="4"):
            category_id=input("Enter the Category ID")
            print("Choice Selected = 4")
            '''
            Here we are invoking a dummy function and passing the data to it.
            This dummy function has to be completed by another programmer.
            '''
        
        elif(choice=="5"):
            category_id=input("Enter the Category ID")
            print("Choice Selected = 5")
            '''
            Here we are invoking a dummy function and passing the data to it.
            This dummy function has to be completed by another programmer.
            '''
        
        elif(choice=="6"):
            category_id=input("Enter the Category ID")
            print("Choice Selected = 6")
            '''
            Here we are invoking a dummy function and passing the data to it.
            This dummy function has to be completed by another programmer.
            '''
            
            
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
        
        #Getting valid item from the displayed items for the selected category
        item_selected=input("Enter a Items for order: ")
        print()
        
        category_items = []
        category_items_quantity = []
        
        #Splitting the category with respect to multiple items selected
        category_items = category.split(',')
        
        
        quantity_req =input("Enter a  quantity required : ")
        #Splitting the category with respect to multiple items selected
        category_items_quantity = quantity_req.split(',')
        
        
        for index , category in zip(category_items , list_of_category_items) :
            print(index ," ", category)
            
        print()   
        
        
        
        choice=input("Please Select The Category. Enter Corresponding Number ")
        if(choice=="1"):
            category_id=input("Enter the Category ID")
            '''
            Here we are invoking a dummy function and passing the data to it.
            This dummy function has to be completed by another programmer.
            '''
        elif(choice=="2"):
            category_id=input("Enter the Category ID")
            '''
            Here we are invoking a dummy function and passing the data to it.
            This dummy function has to be completed by another programmer.
            '''
        elif(choice=="3"):
            category_id=input("Enter the Category ID")
            '''
            Here we are invoking a dummy function and passing the data to it.
            This dummy function has to be completed by another programmer.
            '''
        
        elif(choice=="4"):
            category_id=input("Enter the Category ID")
            '''
            Here we are invoking a dummy function and passing the data to it.
            This dummy function has to be completed by another programmer.
            '''
        
        elif(choice=="5"):
            category_id=input("Enter the Category ID")
            '''
            Here we are invoking a dummy function and passing the data to it.
            This dummy function has to be completed by another programmer.
            '''
        
        elif(choice=="6"):
            category_id=input("Enter the Category ID")
            '''
            Here we are invoking a dummy function and passing the data to it.
            This dummy function has to be completed by another programmer.
            '''
            
            
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