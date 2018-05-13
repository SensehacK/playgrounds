#OOP-Assgn-10
#Start writing your code here



class Flower :
    
    def __init__(self):
        self.__flower_name = None
        self.__price_per_kg = None
        self.__stock_available = None
        self.__required_stock_available = None
        
    def get_flower_name(self):
        return self.__flower_name


    def get_price_per_kg(self):
        return self.__price_per_kg

    def get_required_stock_available(self):
        return self.__required_stock_available 
     
    def get_stock_available(self):
        return self.__stock_available


    def set_flower_name(self, value):
        self.__flower_name = value.lower()


    def set_price_per_kg(self, value):
        self.__price_per_kg = value

    def set_required_stock_available(self,value):
        self.__required_stock_available = value
        
    def set_stock_available(self, value):
        self.__stock_available = value


    def validate_flower(self):
        if self.get_flower_name() == "orchid"  or self.get_flower_name() == "rose" or  self.get_flower_name() == "jasmine" :
            return True
        else :
            return False
        
    def validate_stock(self,required_quantity):
        if self.check_level():
            return True
        else :
            return False
    
    def sell_flower(self,required_quantity):
        self.set_required_stock_available(required_quantity)
        if self.validate_flower() and self.validate_stock(required_quantity) :
            self.set_stock_available( self.get_stock_available() - required_quantity )
        else : 
            return False
#             print("Didnt execute")            

    
    def check_level(self):
        
        if self.get_flower_name() == "orchid" :
            if self.get_stock_available() >  self.get_required_stock_available() :
                return True
                
            
        elif self.get_flower_name() == "rose" :
            if self.get_stock_available() >  self.get_required_stock_available() :
                return True
                        
            
        elif  self.get_flower_name() == "jasmine" :
            if self.get_stock_available() >  self.get_required_stock_available() :
                return  True
            
f1 = Flower()
f1.set_flower_name("Orchid")
f1.set_price_per_kg(35)
f1.set_stock_available(50)
f1.sell_flower(60)


f2 = Flower()
f2.set_flower_name("Rosee")
f2.set_price_per_kg(20)
f2.set_stock_available(40)
f2.sell_flower(23)


f3 = Flower()
f3.set_flower_name("Jasmine")
f3.set_price_per_kg(39)
f3.set_stock_available(40)
f3.sell_flower(32)
