#DSA-Assgn-2

class Car:
    def __init__(self,model,year,registration_number):
        self.__model=model
        self.__year=year
        self.__registration_number=registration_number
    
    def get_model(self): 
        return self.__model
    
    def get_year(self):
        return self.__year
    
    def get_registration_number(self):
        return self.__registration_number
    
    def __str__(self):
        return(self.__model+" "+self.__registration_number+" "+(str)(self.__year))
    
    
class Service: 
    
    def __init__(self,car_list): 
        self.__car_list = car_list
        
    def get_car_list(self):
        return self.__car_list
    
    
    def find_cars_by_year(self,year):
        car_list_year = []
        for cars_obj in self.get_car_list() :
            if cars_obj.get_year() == year :
                model_name = cars_obj.get_model()
                car_list_year.append(model_name)
    
                
        if len(car_list_year) > 0 :
            return car_list_year
        else :
            return None
            
    def add_cars(self,new_car_list):
        #self.get_car_list().append(new_car_list)
        self.__car_list=self.__car_list+new_car_list
        car_list = self.get_car_list()
        for i in range(0,len(car_list)):
            for j in range(0,len(car_list)-1):
                if car_list[j].get_year()>car_list[j+1].get_year():
                    temp=car_list[j]
                    car_list[j]=car_list[j+1]
                    car_list[j+1]=temp
        self.__car_list = car_list
        
        return self.__car_list
        
        
    
    def remove_cars_from_karnataka(self):
        new_list = []

        for cars_obj in self.get_car_list() :
            reg_string = cars_obj.get_registration_number()
            
            if "KA" == reg_string[:2] :
                print("Hello")
                continue
                #self.get_car_list().remove(cars_obj)
                 
            else : 
                print("Yellow")
                new_list.append(cars_obj)
                
                
        self.__car_list = new_list
        for cars_obj in self.get_car_list() :
            print("model : ",cars_obj.get_model() )
            print("year:" ,cars_obj.get_year() )
            print("registration_number" , cars_obj.get_registration_number())
            
        return self.__car_list
        


car1=Car("WagonR",2010,"KA09 3056")
car2=Car("Beat", 2011, "MH10 6776")
car3=Car("Ritz", 2013,"KA12 9098")
car4=Car("Polo",2013,"GJ01 7854")
car5=Car("Amaze",2014,"KL07 4332")
new_car_list = [car2, car4]
#Add different values to the list and test the program
car_list=[car1, car2, car3, car4 ,car5]
ser = Service(car_list)
ser.add_cars(new_car_list)
print(ser.find_cars_by_year(2013))
ser.remove_cars_from_karnataka()
print(ser.get_car_list())

#Create object of Service class, invoke the methods and test your program