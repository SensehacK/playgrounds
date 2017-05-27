'''
Created on Mar 15, 2017

@author: kautilya.save
'''
from database import ViewDB
from exceptions.CustomException2 import InvalidCategoryException, InvalidCatItemsException


def validate_view_category(restaurant_type): 
    list_of_restaurant_categories=ViewDB.get_restaurant_categories(restaurant_type)
    if(len(list_of_restaurant_categories)==0):
        print("Raising Exception")
        raise InvalidCategoryException()
    print("In validate function class  /validate_view_category")
    return list_of_restaurant_categories


def validate_view_category_items(category): 
    list_of_restaurant_categories_items=ViewDB.get_categories_fooditems(category)
    if(len(list_of_restaurant_categories_items)==0):
        raise InvalidCatItemsException
    
    return list_of_restaurant_categories_items