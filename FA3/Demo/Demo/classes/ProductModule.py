'''
Created on Aug 5, 2015

@author: Deepak_M05
'''
'''
This class represents a product
'''
class Product:
    def __init__(self):
        self.__product_id=None
        self.__product_name=None
        self.__price=None
        self.__category=None

    def get_product_id(self):
        return self.__product_id


    def get_product_name(self):
        return self.__product_name


    def get_price(self):
        return self.__price


    def set_product_id(self, value):
        self.__product_id = value


    def set_product_name(self, value):
        self.__product_name = value


    def set_price(self, value):
        self.__price = value

