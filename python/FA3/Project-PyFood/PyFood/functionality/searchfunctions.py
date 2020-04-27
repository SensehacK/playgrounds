'''
Created on Mar 16, 2017

@author: gaurav.sainger
'''

# from database.ViewDB import search_restaurants
from validations import Validate
from exceptions import CustomException2
from functionality import filtersearch

def search_as_guest():
    try:
        city=input("Enter your city:")
        area=input("Enter your area:")
        
#         city=city1.upper()
#         area=area1.upper()
        list_of_restaurants=Validate.validate_search_category(city,area)
        
        '''
        Print the details
         '''
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
        print("resturantname     type of food    likes     dislikes     rating")
        for select in list_of_restaurants:
            print(select.get_restaurantname(),"     ",select.get_type_of_food()," " ,  select.get_likes(),"     ",select.get_dislikes(),"     ",select.get_rating())
        print()   
        
        
        choice=input("Do you want to filter or select restaurant?(F/S)")
        try:
            if (choice.upper()=="F"):
            
                filtersearch.Filter_search(city,area)
        except CustomException2.Invalidfilter as e:
            print(e) 
        except Exception as e:
            print("Choose F or S")
            print(e)       
            
        if (choice.upper()=="S"):
            resturant_name=input("Enter the resturant name:")  
            print("")  
    
    except CustomException2.InvalidCategoryException as e:
        print(e)
    except Exception as e:
        print(e)
    print()

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
        print("Sorry. Some system error occurred")
        print(e)
    print()    
    
    
    