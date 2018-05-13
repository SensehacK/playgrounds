#OOP-Assgn-23

class Apparel:
    __counter = 100
    def __init__(self,price,item_type):
        self.__item_id=None
        if item_type == "Silk" :
            Apparel.__counter += 1
            self.__item_id="S" + str(Apparel.__counter)
        elif item_type == "Cotton" :
            Apparel.__counter += 1
            self.__item_id="C" + str(Apparel.__counter) 
        
        self.__item_type=item_type
        self.__price=price

    def get_item_id(self):
        return self.__item_id

    def get_item_type(self):
        return self.__item_type

    def get_price(self):
        return self.__price

    def set_price(self, value):
        self.__price = value

    def calculate_price(self):
        price = self.get_price() + (self.get_price()  * 5 / 100 )
        self.set_price(price)
    
class Cotton(Apparel):
    def __init__(self,price,discount):
        self.__discount=discount
        super().__init__(price,"Cotton")
           
    def calculate_price(self):
        super().calculate_price()
        price_super = super().get_price()
        #Calculate Discounted Price
        price_super = price_super - (price_super * self.get_discount() / 100)
        # Add 5% VAT
        total_price_vat = price_super + (price_super * 5 / 100)
        
        super().set_price(total_price_vat)
        
    def get_discount(self):
        return self.__discount
        
        
class Silk(Apparel):
    def __init__(self,price):
        self.__points = None
        super().__init__(price,"Silk")
             
    def calculate_price(self):
        super().calculate_price()
        price_super = super().get_price()
        #Calculate Points
        if price_super > 10000 :
            self.__points = 10
        elif price_super <= 10000 :
            self.__points = 3
        # Add 10% VAT
        total_price_vat = price_super + (price_super * 10 / 100)
        
        super().set_price(total_price_vat)
    
    def get_points(self):
        return self.__points


cot = Cotton(1000,10)
cot.calculate_price()
print("Cotton Total Price : " , cot.get_price())
sil = Silk(9000)
sil.calculate_price()
print("Silk Total Price : " , sil.get_price())
