'''
Created on Feb 6, 2017

@author: kautilya.save
'''

# class A():
#      def __init__(self, s="Welcome"):
#          self.s = s
#  
#      def print_1(self):
#          print(self.s)


# 
# a = A()
# a.print_1()
# x = 'My name is XYZ'
# y=x.lower()
# print(y)
# 
# list1 = [5,4,7,6,8,2,9]
# list2 = list1[:]
# list2.sort(reverse = True)
# print(list2)


from abc import ABCMeta, abstractmethod
class A(metaclass=ABCMeta):
    @abstractmethod
    def do_something(self):
        pass

class B(A):
    def __init__(self,name):
        self.__name = name 
    
    def get_name(self):
        return self.__name
    def do_something(self):
        pass 


class Product:
    prod_id = 6
    def __init__(self, prod_name, price):
        self.prod_id = self.prod_id + 1
        self.__prod_name = prod_name
        self.__price = price

class Broadband(Product):
    def __init__(self, speed, data_per_month):
        self.prod_id = self.prod_id + 1
        self.__speed = speed
        self.__data_per_month = data_per_month

product1 = Broadband (500, 10)
product2 = Broadband (400, 20)