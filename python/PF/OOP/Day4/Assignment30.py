#OOP-Assgn-30
#Start writing your code here

class Customer :
    
    def __init__(self,customer_name , quantity):
        self.__customer_name = customer_name
        self.__quantity = quantity
        
    def validate_quantity(self):
        if self.get_quantity() >= 1 and self.get_quantity() <= 5 :
            return True
        else :
            return False
    
    def get_customer_name(self):
        return self.__customer_name
    
    def get_quantity(self):
        return  self.__quantity
            


class Pizzaservice :
    counter = 100
    
    def __init__(self,customer,pizza_type,additional_topping):
        self.__customer = customer
        self.__service_id = None
        self.__pizza_type = pizza_type
        self.__additional_topping = additional_topping
        
        self.pizza_cost = None

    def get_customer(self):
        return self.__customer


    def get_service_id(self):
        return self.__service_id


    def get_pizza_type(self):
        return self.__pizza_type


    def get_additional_topping(self):
        return self.__additional_topping

        
    def validate_pizza_type(self):
        if self.get_pizza_type().lower() == "small" or self.get_pizza_type().lower() == "medium" :
            return True
        else :
            return False

    def calculate_pizza_cost(self):
        pizza_price = 0
        self.pizza_cost = 0
        pizza_topping = 0
        quantity  = self.get_customer().get_quantity()
        Pizzaservice.counter += 1
        
        if self.validate_pizza_type() and self.get_customer().validate_quantity() :
            if self.get_pizza_type().lower() == "small" :
                pizza_price = 150
                pizza_topping = 35
                
                if self.get_additional_topping() :
                    self.pizza_cost = (pizza_price + pizza_topping) * quantity 
                else :
                    self.pizza_cost = pizza_price * quantity
            
            elif self.get_pizza_type().lower() == "medium" :
                pizza_price = 200
                pizza_topping = 50
                if self.get_additional_topping() :
                    self.pizza_cost = (pizza_price + pizza_topping) * quantity 
                else :
                    self.pizza_cost = pizza_price * quantity
            
                
            self.get_service_id = self.get_pizza_type()[0] + str(Pizzaservice.counter)
#             return (self.pizza_cost)
        
        else :
            self.pizza_cost= -1
#             return (self.pizza_cost)
        
        
    
    
class Doordelivery(Pizzaservice) :
    
    def __init__(self,customer,pizza_type,additional_topping,distance_in_kms):
        super().__init__(customer, pizza_type, additional_topping)
        self.__delivery_charge = None
        self.__distance_in_kms = distance_in_kms

    def get_delivery_charge(self):
        return self.__delivery_charge


    def get_distance_in_kms(self):
        return self.__distance_in_kms

    
    def validate_distance_in_kms(self):
        if self.get_distance_in_kms() >= 1 and self.get_distance_in_kms() <= 10 :
            return True
        else :
            return False

    def calculate_pizza_cost(self):
        pizza_total = 0
        if self.validate_distance_in_kms() :
            super().calculate_pizza_cost()
            pizza_total = 0
            if self.pizza_cost != -1 :
                pizza_distance = self.get_distance_in_kms()
                if pizza_distance <= 5 :
                    pizza_total = self.pizza_cost + (pizza_distance * 5)
                    self.pizza_cost = pizza_total
                if pizza_distance > 5 and pizza_distance <= 10:
                    first_five_charge = pizza_distance * 5
                    remaining_kms = pizza_distance - 5 
                    remaining_price_charge = remaining_kms * 7
                    pizza_total = self.pizza_cost + (first_five_charge + remaining_price_charge)
                    self.pizza_cost = pizza_total
            
            
            else :
                self.pizza_cost = -1
                return self.pizza_cost
                  
        else :
            self.pizza_cost = -1
            return self.pizza_cost
        
        
           
   
    
    
    
    
cust = Customer("Kautilya" , 4)
pizza = Pizzaservice(cust,"medIUm",True)
pizza.calculate_pizza_cost()
# door_d = Doordelivery(cust,"medIUm",False,6)
# door_d.calculate_pizza_cost()
