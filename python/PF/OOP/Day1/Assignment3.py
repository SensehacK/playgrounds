#OOP-Assgn-3
#Start writing your code here


     
class Customer :
    
    def __init__(self) :
        self.bill_amount = None
        self.customer_name = None

    def pays_bill(self,amount):
        print("", self.customer_name , "pays bill amount of Rs.", amount)
    
    def purchases(self):
        amount = self.bill_amount -  (self.bill_amount * 5/100)
        self.pays_bill(amount)

class Employee :
    def __init__(self) :
        self.emp_name = None
        self.designation = None
class Item :
    def __init__(self) :
        self.description  = None
        self.item_id = None
        self.price_per_unit = None

        
cust = Customer()
cust.customer_name = "Kautilya Save"
cust.bill_amount = 100
cust.purchases()