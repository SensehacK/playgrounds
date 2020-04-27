#OOP-Assgn-25
#Start writing your code here

class FruitInfo:
    __fruit_name_list = ["Apple" , "Guava", "Orange" , "Grape" , "Sweet Lime"]
    __fruit_price_list = [200, 80, 70 , 110, 60]
    
    @staticmethod
    def get_fruit_name_list():
        return FruitInfo.__fruit_name_list

    @staticmethod
    def get_fruit_price_list():
        return FruitInfo.__fruit_price_list

    @staticmethod
    def get_fruit_price(fruit_name):
        for index,values in enumerate(FruitInfo.__fruit_name_list) :
            if fruit_name == values :
                return FruitInfo.__fruit_price_list[index]
            else :
                return -1
            


# fru = FruitInfo()
# print(FruitInfo.get_fruit_price("Orange"))

class Purchase:
    __counter = 101
    def __init__(self,customer,fruit_name,quantity):
        self.__purchase_id=None
        self.__customer=customer
        self.__fruit_name=fruit_name
        self.__quantity=quantity

    def get_purchase_id(self):
        return self.__purchase_id


    def get_customer(self):
        return self.__customer


    def get_quantity(self):
        return self.__quantity

        
           
    def calculate_price(self):

        print("Hello")  
        print(FruitInfo.get_fruit_price(self.__fruit_name))
        if FruitInfo.get_fruit_price(self.__fruit_name) != -1 :
            fruit_selected_price = FruitInfo.get_fruit_price(self.__fruit_name)
             
            max_fruit = max(FruitInfo.get_fruit_price_list)
             
            calculated_price = self.__quantity * fruit_selected_price
            Purchase.__counter += 1
            self.__purchase_id += "P" + str(Purchase.__counter)

            if self.get_quantity() > 1 and fruit_selected_price == max_fruit :
                qdiscounted_price = calculated_price - (calculated_price * 2 / 100)
                 
            elif self.get_quantity() > 5 and fruit_selected_price == max_fruit :
                qdiscounted_price = calculated_price - (calculated_price * 5 / 100)
                    
            if self.__customer.get_cust_type() == "WholeSeller" :
                discounted_price = qdiscounted_price - (qdiscounted_price * 10 / 100)
                 
            else :
                discounted_price = calculated_price - (calculated_price * 10 / 100)
                 
             
            return discounted_price
    
        else :
            
            return -1
          

        
class Customer(Purchase):
    def __init__(self,customer_name,cust_type):
        self.__customer_name=customer_name
        self.__cust_type=cust_type

    def get_customer_name(self):
        return self.__customer_name

    def get_cust_type(self):
        return self.__cust_type

cust = Customer("Kautilya", "WholeSeller")
pur = Purchase(cust,"Guava",100)
pur.calculate_price()
