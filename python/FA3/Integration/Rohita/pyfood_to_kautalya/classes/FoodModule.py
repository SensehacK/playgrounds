'''
Created on Mar 15, 2017

@author: kautilya.save
'''
'''
This class represents a product
'''

class Food:
    #Example for accessing & storing the global variables ( Package Name >> Class Name >> Variable Name
    # FoodModule.Food.registered_user
    #Gaurav
    restaurant_name = None
    restaurant_city = None
    restaurant_area = None
    
    #Rohita
    registered_user = 'Kautilya'
    is_registered_user = False
    
    #Kautilya
    category = None
    product_id = None
    cart_dict = {}
    is_cart_saved = False
    
    #Komal 
    total_price = None
    
    def __init__(self):
        self.__product_id=None
        self.__restaurant_name=None
        self.__registered_user=None
        self.__category=None
