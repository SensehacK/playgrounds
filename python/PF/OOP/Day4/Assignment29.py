#OOP-Assgn-29
#Start writing your code here
from abc import ABCMeta,abstractmethod


class Customer(metaclass = ABCMeta) :
    
    def __init__(self,customer_name):
        self.__customer_name = customer_name
        self.bill_amount = None
        self.bill_id = None
        
    @abstractmethod    
    def calculate_bill_amount(self):
        pass
    
    def get_customer_name(self):
        return self.__customer_name
    
class OccasionalCustomer(Customer) :
    __counter = 1000
    
    def __init__(self,customer_name,distance_in_kms):
        super().__init__(customer_name)
        self.__distance_in_kms = distance_in_kms
        OccasionalCustomer.__counter += 1
        self.bill_id = "O" + str(OccasionalCustomer.__counter)
        
    def validate_distance_in_kms(self):
        if self.get_distance_in_kms() >= 1 and self.get_distance_in_kms() <= 5 :
            return True
        return False   
    
    def calculate_bill_amount(self):
        if self.validate_distance_in_kms():
            pass
            distance = self.get_distance_in_kms()
            bill_amount = 0
            delivery_charge = 0
            cost_tiffin  = 50
            if distance >= 1 and distance <= 2 :
                delivery_charge = 5 * distance
            elif distance >= 2 and distance <=5 :
                delivery_charge = 7.5 * distance
            
            
            bill_amount = cost_tiffin + delivery_charge
            self.bill_amount = bill_amount
            return self.bill_amount
        else :
            self.bill_amount = -1
            return self.bill_amount
    
    def get_distance_in_kms(self):
        return self.__distance_in_kms
    
    
class RegularCustomer(Customer) :
    __counter = 100
    
    def __init__(self,customer_name,no_of_tiffin):
        super().__init__(customer_name)
        self.__no_of_tiffin = no_of_tiffin
        RegularCustomer.__counter += 1
        self.bill_id = "R" + str(RegularCustomer.__counter)
    
    def validate_no_of_tiffin(self):
        if self.get_no_of_tiffin() >= 1 and self.get_no_of_tiffin() <= 7 :
            return True
        return False   
    
    def calculate_bill_amount(self):
        if self.validate_no_of_tiffin() :
            tiffins = self.__no_of_tiffin
            bill_amount = 0
            delivery_charge = 0
            cost_tiffin  = 50
            
            delivery_charge = cost_tiffin * tiffins 
            
            bill_amount = 7 * delivery_charge
            self.bill_amount = bill_amount
            return self.bill_amount
        
        else:
            self.bill_amount = -1
            return self.bill_amount
    
    def get_no_of_tiffin(self):
        return self.__no_of_tiffin
    



oc  = OccasionalCustomer("Kautilya" , 4)
rc = RegularCustomer("NAresh", 5)


oc.calculate_bill_amount()
rc.calculate_bill_amount()


