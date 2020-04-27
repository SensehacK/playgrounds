'''
Created on Aug 5, 2015

@author: Deepak_M05
'''

'''
This file has all the custom exceptions needed for the project
'''
class InvalidCategoryException(Exception):
    def __init__(self):
        super().__init__("The category is invalid")
        

