#OOP-Exer-10
#Start writing your code here


class Clown :
    __count_of_clowns = None
    
    def __init__(self,name):
        self.__name = name
        
    def make_people_laugh(self):
        print(self.__name, "has a funny nose")
        print("No of Clowns are " , self.get_count_of_clowns())
        print(self.__name, "left his fly open , oopsies :P ")
    
    def set_name(self,name):
        self._Clown__name = name
        
    def get_name(self):
        return self.__name 
    
    @staticmethod    
    def set_clown_count(number):
        Clown.__count_of_clowns = number
        
    @staticmethod    
    def get_count_of_clowns():
        return Clown.__count_of_clowns

mkr = Clown("Ledger")

Clown._Clown__count_of_clowns = 5

mkr.make_people_laugh()
#Set clown Name :) via setter 
Clown.set_clown_count(10)
        
print("Mkr.get Clown Count",Clown.get_count_of_clowns())

#SEtting clown name directly via accessing classname + private static variable
Clown._Clown__count_of_clowns = 50
print("Mkr.get Clown Count2 after :", Clown._Clown__count_of_clowns)

print(Clown._Clown__count_of_clowns)
    
Clown.set_clown_count(100)    
mkr.set_name("Kautilya")

print("Clown Name is " , mkr.get_name()) 
        
mkr.make_people_laugh()
        

gau = Clown("Gaurav")  
gau.make_people_laugh()
    