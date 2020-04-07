'''
Created on Mar 16, 2017

@author: gaurav.sainger
'''
class Select:
    def __init__(self):
        self.__restaurantname=None
        self.__type_of_food=None
        self.__likes=None
        self.__dislikes=None
        self.__area=None
        self.__city=None
        self.__rating=None

    def get_type_of_food(self):
        return self.__type_of_food


    def set_type_of_food(self, value):
        self.__type_of_food = value


    def get_restaurantname(self):
        return self.__restaurantname


    def get_likes(self):
        return self.__likes


    def get_dislikes(self):
        return self.__dislikes


    def get_rating(self):
        return self.__rating


    def set_restaurantname(self, value):
        self.__restaurantname = value


    def set_likes(self, value):
        self.__likes = value


    def set_dislikes(self, value):
        self.__dislikes = value


    def set_rating(self, value):
        self.__rating = value



    def get_area(self):
        return self.__area


    def get_city(self):
        return self.__city


    def set_area(self, value):
        self.__area = value


    def set_city(self, value):
        self.__city = value
    
   
        
        
        