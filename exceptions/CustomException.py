'''
Created on Mar 15, 2017

@author: kautilya.save
'''

'''
This file has all the custom exceptions needed for the project
'''

class InvalidCategoryException(Exception):
    def __init__(self):
        super().__init__("The category is invalid")