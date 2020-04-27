'''
Created on Mar 17, 2017

@author: gaurav.sainger
'''

from validations import Validate
from exceptions.CustomException2 import InvalidCategoryException, InvalidCatItemsException
from functionality import filtersearch
def search_as_login(city,area):
    try:
       
        list_of_restaurants=Validate.validate_search_category(city,area)
        
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
        print("resturantname     type of food    likes     dislikes     rating")
        for select in list_of_restaurants:
            print(select.get_restaurantname(),"     ",select.get_type_of_food()," " ,  select.get_likes(),"     ",select.get_dislikes(),"     ",select.get_rating())
        print()   
        
        
        choice=input("Do you want to filter or select restaurant?(F/S)")
        if (choice=="F"):
            
            filtersearch.Filter_search()
            
            
        if (choice=="S"):
            resturant_name=input("Enter the resturant name:")  
            print("")  
    
    except InvalidCategoryException as e:
        print(e)
    except Exception as e:
        print("here is")
        print("Sorry. Some system error occurred")
        print(e)
    print()    
    