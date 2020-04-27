'''
Created on Aug 6, 2015

@author: Deepak_M05
'''
from validations.ViewValidations import validate_view
from exceptions.CustomExceptions import InvalidCategoryException

'''
positive test cases
'''
list_of_products=validate_view('soap')
list_of_products=validate_view('shampoo')

'''
negative test cases
'''
try:
    list_of_products=validate_view('x')
except InvalidCategoryException as e:
    print(e)

