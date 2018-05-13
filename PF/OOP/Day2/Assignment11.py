#OOP-Assgn-11
#Start writing your code here



class Customer :
    
    def __init__ (self,customer_id,customer_name,address):
        self.__customer_id = customer_id
        self.__customer_name = customer_name
        self.__address = address
    
    def validate_customer_id(self):
#         print("Hello")
#         print(self.__customer_id[0])
        if ( (self.__customer_id[0] == "1") and (len(self.__customer_id) == 6) ) :
            return True
        else :
            print("Please Enter Customer ID starting from 1 digit & length of 6 Digits")
            return False

    def get_customer_id(self):
            return self.__customer_id
        
    
    def get_customer_name(self):
        return self.__customer_name
        
    def get_address(self):
        return  self.__address
        
        
    
class Freight :
    __Freight_counter = 198

    def __init__ (self,from_customer,recipient_name,weight,distance):
        self.__freight_id = None
        self.__recipient_customer = recipient_name
        self.__from_customer = from_customer
        self.__weight = weight
        self.__distance = distance
        self.__freight_charge = None
        
        
    def validate_weight(self):
        if self.get_weight() % 5 == 0 :
            return True
        else :
            return False

    def validate_distance(self):
        if ((self.get_distance() >= 500) and (self.get_distance() <= 5000)) :
            return True
        else : 
            return  False
  
    def forward_cargo(self):
        
#         print("Debug Prints")
#         print("Forward cargo")
#         print(self.get_from_customer().validate_customer_id())
#         print(self.validate_distance())
#         print(self.get_recipient_name().validate_customer_id())
#         print(self.validate_weight())
#         print(Freight.__counter)

        if ( (self.get_from_customer().validate_customer_id()) and (self.get_recipient_name().validate_customer_id()) and (self.validate_distance()) and (self.validate_weight()) ) :
            Freight.__Freight_counter += 2
            self.__freight_id = Freight.__Freight_counter
            self.__freight_charge = (self.get_weight() * 150) + (self.get_distance() * 60)
#             return self.__freight_id
        else : 
            print("Validations didn't meet the specifications")
#             print("Else Forward Cargo")
            self.__freight_charge = 0
        
    def get_freight_id(self):
        return  self.__freight_id
    
    def get_freight_charge(self):
        return  self.__freight_charge
    
    def get_recipient_customer(self):
        return  self.__recipient_customer
    
    def get_from_customer(self):
        return  self.__from_customer
    
    def get_distance(self):
        return  self.__distance
    
    def get_weight(self):
        return  self.__weight

cust = Customer("100091","Kautilya Save", "Mumbai")
cust1 = Customer("107231","Kautilya saef", "Mumbai")

#def __init__ (self,from_customer,recipient_name,weight,distance)
frei = Freight(cust,cust1,10,1000)
frei.forward_cargo()
print("Freight ID : " , frei.get_freight_id(), "Freight Charge : ", frei.get_freight_charge())

# cust.set_customer_id(100091)
# cust.set_customer_name("Kautilya Save")
# cust.set_address("Mumbai")
    
    
        