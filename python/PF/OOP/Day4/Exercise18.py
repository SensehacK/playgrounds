#OOP-Exer-18
#Start writing your code here


from abc import ABCMeta , abstractmethod

class DirectToHomeService(metaclass = ABCMeta) :
    __counter = 101
    
    def __init__(self,consumer_name):
        self.__consumer_name = consumer_name
        self.__consumer_number = DirectToHomeService.__counter
        DirectToHomeService.__counter += 1

    def get_consumer_name(self):
        return self.__consumer_name

    def get_consumer_number(self):
        return self.__consumer_number
        
    @abstractmethod
    def calculate_monthly_rent(self):
        pass
    
    
    
    
class BasePackage(DirectToHomeService):
    
    def __init__(self,consumer_name,base_pack_name,subscription_period):
        self.__base_pack_name = base_pack_name
        self.__subscription_period = subscription_period
        super().__init__(consumer_name)

    def get_base_pack_name(self):
        return self.__base_pack_name


    def get_subscription_period(self):
        return self.__subscription_period
    
    def validate_base_pack_name(self):
        if self.get_base_pack_name() == "Silver" or self.get_base_pack_name() == "Gold" or self.get_base_pack_name() == "Platinum" :
            return True
        else :
            self.__base_pack_name = "Silver"
            print("Base package name is incorrect, set to Silver")
            return True
        
    
    def calculate_monthly_rent(self):
        
        if self.get_subscription_period() >= 1 and self.get_subscription_period() <= 24 :
            if self.validate_base_pack_name() :
                base_pack = self.get_base_pack_name()
                #print(base_pack)
                base_price = 0
                final_monthly_rent = None
                discount_price = 0
                if base_pack == "Silver" :
                    base_price = 350.00
                    if self.get_subscription_period() > 12 :
                        discount_price = 350.00
                        
                elif base_pack == "Gold" :
                    base_price = 440.00
                    if self.get_subscription_period() > 12 :
                        discount_price = 440.00
                        
                elif base_pack == "Platinum" :
                    base_price = 560.00
                    if self.get_subscription_period() > 12 :
                        discount_price = 560.00
                        
                        
                final_monthly_rent = ( (base_price * self.get_subscription_period() ) - discount_price ) / self.get_subscription_period()
                print(final_monthly_rent)
                
                return final_monthly_rent
            
            else :
                print("validate else false")
                return -1
        else :
            return -1
            
             
 
basep = BasePackage("Kautilya","Gold",13)
basep.calculate_monthly_rent()
                             
basep2 = BasePackage("Sita","Silver",12)
basep2.calculate_monthly_rent()
               
basep3 = BasePackage("Sita","Gold",25)
basep3.calculate_monthly_rent()

basep4 = BasePackage("Sita","silver",15)
basep4.calculate_monthly_rent()

            
                
        
    
    
    
    