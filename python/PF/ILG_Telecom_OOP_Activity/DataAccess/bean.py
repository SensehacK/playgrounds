
# ========================================================================================================== #
#                                         EXERCISE 3 
# VOIP, DTH and Broadband are the products which are currently offered by ILG telecom. 
# The classes have been provided below. Identify common attributes and methods.
# Modify these classes to implement inheritance introducing Product as the base class. 
# ========================================================================================================== #


class Product :
    def __init__(self,prod_id, prod_name, price):
        self.__prod_id = prod_id
        self.__prod_name = prod_name
        self.__price = price
        
    def get_prod_id(self):
        return self.__prod_id
    def get_prod_name(self):
        return self.__prod_name
    def get_price(self):
        return self.__price    
    
# classes for various products offered by ILG telecom
class VoIP(Product):
    def __init__(self,prod_id, prod_name, price, ip, latency, per_call_bandwidth):
        super().__init__(prod_id, prod_name, price)    # Subscription amount per month
        self.__ip = ip                  # example: H.323/Skype/SIP/MGCP/RTP/SRTP/IAX
        self.__latency = latency        # example: 450ms / 600ms / 550ms / range 400-600
        self.__per_call_bandwidth = per_call_bandwidth # unit kbps

    #Begin of getter methods---------------------------- 
    
    def get_ip(self):
        return self.__ip
    def get_latency(self):
        return self.__latency
    def get_per_call_bandwidth(self):
        return self.__per_call_bandwidth
    #End of getter methods------------------------------
    
    # str method to return attributes of VoIP object as a string
    def __str__(self):
        return (self.get_prod_id().center(5)+" "+
                self.get_prod_name().center(15)+" "+
                str(self.get_price()).center(22)+" "+
                self.get_ip().center(10)+" "+
                str(self.get_latency()).center(10)+" "+
                str(self.get_per_call_bandwidth()).center(20))
        

class DTH(Product):
    def __init__(self,prod_id, prod_name, price, service_provider, package):
        super().__init__(prod_id, prod_name, price)                # Subscription amount per month
        self.__service_provider = service_provider      # example: TiVo/Horizon Go-Go
        self.__package = package                        # example: Gold/silver
        
    #Begin of getter methods---------------------------- 
    
    def get_service_provider(self):
        return self.__service_provider
    def get_package(self):
        return self.__package
    #End of getter methods------------------------------
    
    # str method to return attributes of DTH object as a string
    def __str__(self):
        return (self.get_prod_id().center(5)+" "+
                self.get_prod_name().center(15)+" "+
                str(self.get_price()).center(22)+" "+
                self.get_service_provider().center(20)+" "+
                self.get_package().center(15))
    
class Broadband(Product):
    
    def __init__(self,prod_id, prod_name, price, speed, data_per_month):
        super().__init__(prod_id, prod_name, price)
        self.__speed = speed                        # unit Mbps 
        self.__data_per_month = data_per_month      # unit Gb
    
    #Begin of getter methods---------------------------- 
    
    def get_speed(self):
        return self.__speed
    def get_data_per_month(self):
        return self.__data_per_month
    #End of getter methods------------------------------
    
   
    # str method to return attributes of Broadband object as a string
    def __str__(self):
        return (self.get_prod_id().center(5)+" "+
                self.get_prod_name().center(15)+" "+
                str(self.get_price()).center(22)+" "+
                str(self.get_speed()).center(10)+" "+
                str(self.get_data_per_month()).center(20))    


# =========================================================================== #
#                          END OF EXERCISE 3 
# =========================================================================== #

# class to hold details of deals offered by ILG telecom
class Deal:
    def __init__(self,deal_id,product_list,discount):
        self.__deal_id = deal_id            # example : DEAL-004
        self.__discount = discount          # Discount in monthly subscription amount in Rs.
        self.__product_list = product_list  # List of products offered in the deal example : p4,p5
        
    #Begin of getter methods------------------------------
    def get_deal_id(self):
        return self.__deal_id

    def get_product_list(self):
        return self.__product_list

    def get_discount(self):
        return self.__discount
    #End of getter methods------------------------------

# classes to hold customer's address and other details
class Address:
    def __init__(self,address_line_1=None,address_line_2=None,city=None,state=None,pin_code=None):
        self.__address_line1=address_line_1        
        self.__address_line2=address_line_2
        self.__city=city
        self.__state=state
        self.__pin_code=pin_code
    #Begin of getter methods------------------------------    
    def get_address_line_1(self):
        return self.__address_line1    
    def get_address_line_2(self):
        return self.__address_line2    
    def get_city(self):
        return self.__city    
    def get_state(self):
        return self.__state    
    def get_pin_code(self):
        return self.__pin_code
    #End of getter methods------------------------------
        
    #Begin of setter methods------------------------------ 
    def set_address_line_1(self, value):
        self.__address_line1 = value    
    def set_address_line_2(self, value):
        self.__address_line2 = value    
    def set_city(self, value):
        self.__city = value    
    def set_state(self, value):
        self.__state = value    
    def set_pin_code(self, value):
        self.__pin_code = value  
    #End of setter methods------------------------------ 


class Customer:
    def __init__(self):
        self.__customer_id = None           # Unique ID given to each customer example: 1004
        self.__password=None                # Customers' Password to login into app
        self.__name = None                  # Customers' first name 
        self.__communication_address = None # Holds address of the customer 
        self.__mobile_number = None         
        self.__product_list = []            # List of products subscribed by the customer
        self.__installation_address =None   # Can be different from communication address
        self.__subscription_amount=None     # Amount paid by the customer per month in return for services availed 
    
    
    #Begin of getter methods------------------------------ 
    def get_customer_id(self):
        return self.__customer_id
    def get_password(self):
        return self.__password
    def get_name(self):
        return self.__name
    def get_communication_address(self):
        return self.__communication_address
    def get_mobile_number(self):
        return self.__mobile_number
    def get_product_list(self):
        return self.__product_list
    def get_installation_address(self):
        return self.__installation_address
    def get_subscription_amount(self):
        return self.__subscription_amount
    #End of getter methods------------------------------
    
    
    #Begin of setter methods------------------------------
    def set_customer_id(self, value):
        self.__customer_id = value       
    def set_password(self, value):
        self.__password = value
    def set_name(self, value):
        self.__name = value
    def set_communication_address(self, value):
        self.__communication_address = value
    def set_mobile_number(self, value):
        self.__mobile_number = value
    def set_product_list(self, value):
        self.__product_list = value
    def set_installation_address(self, value):
        self.__installation_address = value
    def set_subscription_amount(self, value):
        self.__subscription_amount = value
    #End of setter methods------------------------------
