#OOP-Assgn-30

class Customer:
    def __init__(self,customer_name,quantity):
        self.__customer_name=customer_name
        self.__quantity=quantity

    def get_customer_name(self):
        return self.__customer_name


    def get_quantity(self):
        return self.__quantity
    
    def validate_quantity(self):
        if self.get_quantity()>=1 and self.get_quantity()<=5:
            return True
        else:
            return False
    
    
    
class Pizzaservice:
    counter=100
    def __init__(self,customer,pizza_type,additional_topping):
        self.__customer=customer
        self.__pizza_type=pizza_type
        self.__additional_topping=additional_topping
        self.__service_id=None
        self.pizza_cost=None

    def get_pizza_type(self):
        return self.__pizza_type


    def get_additional_topping(self):
        return self.__additional_topping
            
        


    def get_service_id(self):
        return self.__service_id
    
    def get_customer(self):
        return self.__customer
    def validate_pizza_type(self):
        if self.get_pizza_type().lower()=="small" or self.get_pizza_type().lower()=="medium":
            return True
        else:
            return False
        
       
    def calculate_pizza_cost(self):
     
        pizza_cost=0
        x= self.__customer.get_quantity()
        if self.validate_pizza_type()==True and self.__customer.validate_quantity()==True:
            if self.get_pizza_type().lower()=="small":
                if self.get_additional_topping()==True:
                    pizza_cost=(150+35)*x
                    
                else:
                    pizza_cost=150*x
            elif self.get_pizza_type().lower()=="medium": 
                if self.get_additional_topping()==True:
                    pizza_cost=(200+50)*x
                else:
                    pizza_cost=200*x
            Pizzaservice.counter+=1
           
            self.__service_id=self.get_pizza_type()[0]+str(Pizzaservice.counter) 
            self.pizza_cost=pizza_cost 
            return (self.pizza_cost)
        else:
            pizza_cost=-1
            self.pizza_cost=pizza_cost
            return (self.pizza_cost)
    
    
class Doordelivery(Pizzaservice):
    def __init__(self,customer,pizza_type,additional_topping,distance_in_kms):
        super().__init__(customer, pizza_type, additional_topping)
        self.__distance_in_kms=distance_in_kms
        self.__delivery_charge=None

    def get_distance_in_kms(self):
        return self.__distance_in_kms


    def get_delivery_charge(self):
        return self.__delivery_charge

    
        
    def validate_distance_in_kms(self):
        if self.get_distance_in_kms()>=1 and self.get_distance_in_kms()<=10:
            return True
        else:
            return False
           
    
    def calculate_pizza_cost(self):
        if self.validate_distance_in_kms()==True:
            super().calculate_pizza_cost()
            if self.pizza_cost!=-1:
                if self.get_distance_in_kms()<=5:
                    self.pizza_cost=self.pizza_cost+5*self.get_distance_in_kms()
                    
                else:
                    self.pizza_cost=self.pizza_cost+25+(self.get_distance_in_kms()-5)*7
                    
            else:
                self.pizza_cost=-1
                return self.pizza_cost
         
        else:
            self.pizza_cost=-1
            return self.pizza_cost       
     
   


cust=Customer("Asha",5)
cust.validate_quantity()
p1=Pizzaservice(cust,"SMALL",True)
p1.calculate_pizza_cost()
d1=Doordelivery(cust,"SMALL",True,6)
d1.calculate_pizza_cost()
    
