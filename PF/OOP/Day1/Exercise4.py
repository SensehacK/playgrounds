#OOP-Exer-5
#Start writing your code here


class Vehicle : 
    
    def __init__ (self):
        self.fuel_left = None
        self.mileage = None
        
    def identify_distance_that_can_be_travelled(self):

        if int(self.fuel_left) <= 5 :
            return 0
        else :
            return (int(self.fuel_left) - 5)* self.mileage
            
    def identify_distance_travelled(self,initial_fuel): 
        fuel_consumed = int(initial_fuel) - self.fuel_left

        return fuel_consumed * self.mileage
    
    

# my_car = Vehicle()
# my_car.fuel_left = 5
# my_car.mileage = 15
# print(my_car.identify_distance_that_can_be_travelled())
# my_car.identify_distance_travelled("100")




        
        
        