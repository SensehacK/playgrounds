#OOP-Assgn-14
#Start writing your code here

class Parrot :
    
    __counter = 0

    def __init__ (self,name,color):
        self.__unique_number = 7000
        self.__name = name
        self.__color = color
        self.set_unique_number()
        
    def get_name(self):
        return self.__name

    def get_color(self):
        return self.__color

    def set_name(self, value):
        self.__name = value

    def set_color(self, value):
        self.__color = value
        
    def set_unique_number(self):
        Parrot.__counter += 1
        self.__unique_number = self.__unique_number + (Parrot.__counter)
        self.print()
        
    def get_unique_number(self):
        return self.__unique_number
    
    def print(self):
        print("Parrot Name : ", self.get_name())
        print("Parrot color : ", self.get_color())
        print("Parrot Unique ID : ", self.get_unique_number())
        
p = Parrot("sense","green")
p1 = Parrot("sense","green")
p2 = Parrot("sense","green")
p3 = Parrot("sense","green")        
        

    