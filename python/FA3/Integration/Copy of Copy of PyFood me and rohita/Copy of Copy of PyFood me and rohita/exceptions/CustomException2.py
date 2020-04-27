'''
Created on Mar 15, 2017

@author: kautilya.save
'''

'''
This file has all the custom exceptions needed for the project

'''
class Invalidcityareaname(Exception):
    def __init__(self):
        super().__init__("NO Hotel matched with your city and area")
        
class Invalidfilter(Exception):
    def __init__(self):
        super().__init__("opps!!! no match ")  

class Invalidselectname(Exception):
    def __init__(self):
        super().__init__("Name not match with the hotel list")         
              
        
class InvalidCategoryException(Exception):
    def __init__(self):
        super().__init__("The category is invalid")
        
class InvalidCatItemsException(Exception):
    def __init__(self):
        super().__init__("The category items is invalid")
