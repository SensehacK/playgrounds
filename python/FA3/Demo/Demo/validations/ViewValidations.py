'''
Created on Aug 5, 2015

@author: Deepak_M05
'''
from database import ViewDB
from exceptions.CustomExceptions import InvalidCategoryException

'''
This function is used for validating the category.
'''
def validate_view(category):
    list_of_products=ViewDB.get_products(category)
    if(len(list_of_products)==0):
        raise InvalidCategoryException()
    
    return list_of_products
    
    