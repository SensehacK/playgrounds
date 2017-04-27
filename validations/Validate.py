'''
Created on Mar 15, 2017

@author: kautilya.save
'''
from database import ViewDB

def validate_view_category(category): 
    list_of_restaurant_categories=ViewDB.get_restaurant_categories(category)
    pass