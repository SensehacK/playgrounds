#OOP-Assgn-7
#Start writing your code here

class Vehicle :
    
    def __init__(self) :
        self.__premium_amount = None
        self.__vehicle_id = None
        self.__vehicle_cost = None
        self.__vehicle_type = None
        
#     def set_premium_amount(self,premium_amount):
#         self.__premium_amount = premium_amount
        
    def get_premium_amount(self):
        return self.__premium_amount
        
    def set_vehicle_id (self,vehicle_id):
        self.__vehicle_id = vehicle_id 
    
    def get_vehicle_id (self):
        return self.__vehicle_id
        
    def get_vehicle_cost(self):
        return self.__vehicle_cost
    
    def set_vehicle_cost(self,vehicle_cost):
        self.__vehicle_cost = vehicle_cost
    
    def set_vehicle_type(self,vehicle_type):
        if (vehicle_type == "TwoWheeler") or (vehicle_type == "FourWheeler") :
            self.__vehicle_type = vehicle_type
        else :
            print("Please enter proper Vehicle type \"TwoWheeler\" \"FourWheeler\"   ")
    
    def get_vehicle_type(self):
        return self.__vehicle_type

    def display_vehicle_details(self):
        print("Vehicle ID : ", self.get_vehicle_id())
        print("Vehicle type : ", self.get_vehicle_type())
        print("Vehicle vehicle cost : ", self.get_vehicle_cost())
        print("Vehicle Premium amount : ", self.get_premium_amount())         
                 
    def calculate_premium(self):
        if self.get_vehicle_type() == "TwoWheeler" :
            self.__premium_amount = (self.get_vehicle_cost() * 2 // 100)
           
        elif self.get_vehicle_type() == "FourWheeler" :
            self.__premium_amount = (self.get_vehicle_cost() * 6 // 100)
                

#Initialize Object & set variables
veh = Vehicle()
veh.set_vehicle_id(1001)
veh.set_vehicle_type("FourWheeler")
veh.set_vehicle_cost(105000)
veh.calculate_premium()
veh.display_vehicle_details()
        
        



















