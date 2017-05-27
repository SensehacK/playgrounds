'''
Created on Mar 17, 2017

@author: gaurav.sainger
'''
class Customer():
    def __init__(self):
        self.__username=None
        self.__password=None
        self.__emailid=None
        self.__mobilenumber=None
        self.__answer=None
        self.__city=None
        self.__area=None
        self.__state=None
        self.__question=None

    def get_question(self):
        return self.__question


    def set_question(self, value):
        self.__question = value



    def get_username(self):
        return self.__username


    def get_password(self):
        return self.__password


    def get_emailid(self):
        return self.__emailid


    def get_mobilenumber(self):
        return self.__mobilenumber


    def get_answer(self):
        return self.__answer


    def get_city(self):
        return self.__city


    def get_area(self):
        return self.__area


    def get_state(self):
        return self.__state


    def set_username(self, value):
        self.__username = value


    def set_password(self, value):
        self.__password = value


    def set_emailid(self, value):
        self.__emailid = value


    def set_mobilenumber(self, value):
        self.__mobilenumber = value


    def set_answer(self, value):
        self.__answer = value


    def set_city(self, value):
        self.__city = value


    def set_area(self, value):
        self.__area = value


    def set_state(self, value):
        self.__state = value
