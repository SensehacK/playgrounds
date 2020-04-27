
from DataAccess.bean import Customer,Address,DTH, Broadband, VoIP, Deal
#from DataAccess.DAO import customerDAO
import pickle


#--------------------------Important Note----------------------------------------------------------------

''' This module loads the Customer , Products and Deals data in the form of objects.
Pickle Framework available in python is used , which is not covered as a part of the Foundation program;
Hence consider this to be a blackbox and you may refer python documentation for further details on the framework  
''' 

#--------------------------End of Note-------------------------------------------------------------------



def load_data():
    load_customers()
    load_products_and_deals()

def load_customers():    
    ''' >>>>>>>>>>>>>>>Create address objects <<<<<<<<<<<<<'''     
    comm_address1 = Address()
    comm_address1.set_address_line_1("123, 3rd main")
    comm_address1.set_address_line_2("Park Street")
    comm_address1.set_city("Bangalore")
    comm_address1.set_state("KA")
    comm_address1.set_pin_code(560002)
    
    comm_address2 = Address()
    comm_address2.set_address_line_1("765, 4th main")
    comm_address2.set_address_line_2("Bakers street")
    comm_address2.set_city("Mumbai")
    comm_address2.set_state("MH")
    comm_address2.set_pin_code(400002)
    
    comm_address3 = Address()
    comm_address3.set_address_line_1("House number 14, 5th main")
    comm_address3.set_address_line_2("Sankranthi Circle")
    comm_address3.set_city("Mysore")
    comm_address3.set_state("KA")
    comm_address3.set_pin_code(570002)
    
    comm_address4 = Address()
    comm_address4.set_address_line_1("301, 3rd floor, Sankalp Apts")
    comm_address4.set_address_line_2("Banjara Hills")
    comm_address4.set_city("Pune")
    comm_address4.set_state("MH")
    comm_address4.set_pin_code(410002)
    
    comm_address5 = Address()
    comm_address5.set_address_line_1("50, 7th cross")
    comm_address5.set_address_line_2("MG Road")
    comm_address5.set_city("Bangalore")
    comm_address5.set_state("KA")
    comm_address5.set_pin_code(560001)
    
    comm_address6 = Address()
    comm_address6.set_address_line_1("70, 8th main")
    comm_address6.set_address_line_2("Station Road")
    comm_address6.set_city("Mysore")
    comm_address6.set_state("KA")
    comm_address6.set_pin_code(570002)
    
    '''>>>>>>>>>>>>>>>>Create Customer Objects <<<<<<<<<<<<<<<<<<<<<'''                         
    c1 = Customer()
    c1.set_customer_id('1001')
    c1.set_password('qwe@123')
    c1.set_name('Jack')
    c1.set_communication_address(comm_address1)
    c1.set_mobile_number(9442253123)
    c1.set_installation_address(comm_address1)
    c1.set_subscription_amount(0)
    
    c2 = Customer()
    c2.set_customer_id('1002')
    c2.set_password('abc$44')
    c2.set_name('James')
    c2.set_communication_address(comm_address2)
    c2.set_mobile_number(9451237896)
    c2.set_installation_address(comm_address2)
    c2.set_subscription_amount(0)
    
    c3 = Customer()
    c3.set_customer_id('1003')
    c3.set_password('mary_1003')
    c3.set_name('Mary')
    c3.set_communication_address(comm_address3)
    c3.set_mobile_number(9662235657)
    c3.set_installation_address(comm_address3)
    c3.set_subscription_amount(0)
    
    c4 = Customer()
    c4.set_customer_id('1004')
    c4.set_password('xyz@321')
    c4.set_name('Mike')
    c4.set_communication_address(comm_address4)
    c4.set_mobile_number(9442221533)
    c4.set_installation_address(comm_address4)
    c4.set_subscription_amount(0)
    
    c5 = Customer()
    c5.set_customer_id('1005')
    c5.set_password('john_123')
    c5.set_name('Johnathan')
    c5.set_communication_address(comm_address5)
    c5.set_mobile_number(9442253144)
    c5.set_installation_address(comm_address6)
    c5.set_subscription_amount(0)
    
    cust_object_list=[]
    cust_object_list.append(c1)
    cust_object_list.append(c2)
    cust_object_list.append(c3)
    cust_object_list.append(c4)
    cust_object_list.append(c5)
    add_customer(cust_object_list)    

def load_products_and_deals():    
    '''>>>>>>>>>>>>>>>>>Create product objects<<<<<<<<<<<<<<'''
    p1 = DTH("D1001", "TIVO_HD", 500, "TiVo", "Silver")
    p2 = Broadband("B1001", "IB_500/40", 1200, 500, 40)
    p3 = VoIP("V1001", "IS_120", 500, "Skype", 450, 120)
    
    p4 = DTH("D1002", "HORGO_SD", 1000, "Horizon Go", "Gold")
    p5 = Broadband("B1002", "IB_400/30", 1000, 400, 30)
    p6 = VoIP("V1002", "IH_100", 400, "H.323", 550, 100)
    
    add_product([p1,p2,p3,p4,p5,p6])
    
    
    '''>>>>>>>>>>>>>>>>Create Deal objects<<<<<<<<<<<<<<<'''
    d1 = Deal("DEAL-001", [p1, p2], 250)
    d2 = Deal("DEAL-002", [p2, p3], 300)
    d3 = Deal("DEAL-003", [p1, p2, p3], 400)
    
    d4 = Deal("DEAL-004", [p4, p5], 350)
    d5 = Deal("DEAL-005", [p5, p6], 325)
    d6 = Deal("DEAL-006", [p1, p2, p6], 450)
    
    d7 = Deal("DEAL-007", [p1, p5], 200)
    d8 = Deal("DEAL-008", [p2, p6], 225)
    d9 = Deal("DEAL-009", [p4, p5, p6], 550)
    d10 = Deal("DEAL-010",[p1, p3], 150)
    
    deal_list = [d1,d2,d3,d4,d5,d6,d7,d8,d9,d10]
    add_deal(deal_list)

# function to read a file
def read_file(file_to_read):
    if file_to_read == "products" or file_to_read == "deals":
        load_products_and_deals()
    try:
        file = open("..\\" + file_to_read + ".pkl", "rb")
    except FileNotFoundError:
        load_data()
        file = open("..\\" + file_to_read + ".pkl", "rb")
    list_of_objects = []
    while 1:
        try:
            list_of_objects.append(pickle.load(file))
        except IOError:
            break
        except EOFError:
            break
    
    file.close()
    return list_of_objects

# function to add objects to a file
def add_obj(obj_list, file_to_add_to):
    with open("..\\" + file_to_add_to + ".pkl", mode='w+b') as file:    
        for obj in obj_list:
            pickle.dump(obj, file)
    
# function to update customer file
def update_customer(cust_obj_list): #accepts a list of customers
    with open('..\\customers.pkl',mode='wb') as cust_file:
            for cust in cust_obj_list:
                pickle.dump(cust,cust_file)

read_customers_file = lambda : read_file("customers")
read_products_file  = lambda : read_file("products")
read_deals_file     = lambda : read_file("deals")
add_customer        = lambda cust_obj_lst : add_obj(cust_obj_lst, "customers")
add_product         = lambda prod_obj_lst : add_obj(prod_obj_lst, "products")
add_deal            = lambda deal_obj_lst : add_obj(deal_obj_lst, "deals")   
