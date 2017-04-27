'''
Created on Mar 15, 2017

@author: kautilya.save
'''

from validations import Validate

def view_category():
    try:
        category=input("Enter a category: ")
        print()
        
        '''
        Validate the user input
        '''
        list_of_products=Validate.validate_view_category(category)
        
        '''
        Print the details
        '''
        for product in list_of_products:
            print(product.get_product_id()," ",product.get_product_name()," ",product.get_price())
        print()   
        
        
        
        choice=input("Do you want to purchase a product? Enter 'Y' or 'N' ")
        if(choice=="Y"):
            product_id=input("Enter the product Id")
            '''
            Here we are invoking a dummy function and passing the data to it.
            This dummy function has to be completed by another programmer.
            '''
            
            PurchaseFunctions.purchase_product(product_id)
            
        '''
        Handle all the exceptions that can occur
        '''   
    except InvalidCategoryException as e:
        print(e)
    except Exception as e:
        print("Sorry. Some system error occurred")
        print(e)
    print()