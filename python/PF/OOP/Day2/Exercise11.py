#OOP-Exer-11
#Start writing your code here


class Customer :
    __customer_count = 0
    
    def __init__(self,customer_name):
        self.__customer_name = customer_name
        Customer.__customer_count += 1
        
    def check_customer_count(self):
        if Customer.__customer_count <= 5 :
            return True
        else :
            return False
            
    def get_early_bird_discount(self):
        if self.check_customer_count() :
            return 10
        else :
            return 0
        
    def get_customer_name(self) : 
        return self.__customer_name
    
    @staticmethod    
    def get_customer_count() : 
        return Customer.__customer_count


# mkr1 = Customer("Ledger")
# print("Customer Name:", mkr1.get_customer_name(), ", Discount : ",mkr1.get_early_bird_discount())
# 
# mkr2 = Customer("Kautilya")
# print("Customer Name:", mkr2.get_customer_name(), ", Discount : ",mkr2.get_early_bird_discount())
# 
# mkr3 = Customer("Gaurav")
# print("Customer Name:", mkr3.get_customer_name(), ", Discount : ",mkr3.get_early_bird_discount())
# 
# mkr4 = Customer("Viraj")
# print("Customer Name:", mkr4.get_customer_name(), ", Discount : ",mkr4.get_early_bird_discount())
# 
# mkr5 = Customer("Rahul")
# print("Customer Name:", mkr5.get_customer_name(), ", Discount : ",mkr5.get_early_bird_discount())
# 
# mkr6 = Customer("Rk")
# print("Customer Name:", mkr6.get_customer_name(), ", Discount : ",mkr6.get_early_bird_discount())
# 
# #print(Customer.get_customer_count())
# 
# # Trial list instances 
# # mkr = []
# # for i in range(0,6) :
# #     name = str(i*2)
# #     mkr[i] = Customer(name)
#     print("Customer Name:", mkr[i].get_customer_name(), "Discount : ",mkr[i].get_early_bird_discount() )
#     


    