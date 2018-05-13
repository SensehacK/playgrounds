from DataAccess.loader import read_customers_file,update_customer,read_deals_file,read_products_file


class CustomerDAO:    
    # static variables: 
    # lists to hold data objects for products and deals offered by ILG telecom 
    # and the details of registered customers
    product_list=[]
    deal_list=[]
    customer_list=[]
    
    def __init__(self,current_customer):
        # initialize current_customer 
        self.__current_customer = current_customer
        # fetch details of all products and deals from the file
        CustomerDAO.product_list = read_products_file()
        CustomerDAO.deal_list = read_deals_file()

    def get_current_customer(self):
        return self.__current_customer

       
    # static method to read customers details from the file
    @staticmethod
    def get_customer_details(): 
        CustomerDAO.customer_list = read_customers_file()
        return(CustomerDAO.customer_list)


# ========================================================================================================== #
#                                         EXERCISE 4 
# ========================================================================================================== #
            
    # method to display communication address of the Current Customer
    # Exer4-A: 
    #       Write code required to display communication address of current_customer   
    # 
    # NOTE: All the required objects are already created. Don't create any new object.
    # ----  Understand the relationship between classes and call appropriate methods to complete the functionality
    # 
    def display_communication_address(self):     
        current_customer = self.__current_customer           
        print("\n\n######## Exer4: Remove this print statement and display communication address as below \n\t File To Modify: DataAccess.DAO.py, Method To Modify: display_communication_address")
        print("\n\tCurrent communication address:")
        print("\t\tAddress Line 1 :")
        print("\t\tAddress Line 2 :")
        print("\t\tCity           :")
        print("\t\tState          :")
        print("\t\tPin code       :")
        

    # method to display Installation Address of the Current Customer
    # Exer4-B: 
    #       Write code required to display installation address of current_customer
    #
    # NOTE: All the required objects are already created. Don't create any new object.
    # ----  Understand the relationship between classes and call appropriate methods to complete the functionality 
    #
    def display_installation_address(self):
        current_customer = self.__current_customer
        print("\n\n######## Exer4: Remove this print statement and display installation address as below \n\t File To Modify: DataAccess.DAO.py, Method To Modify: display_installation_address")        
        print("\n\tCurrent installation address:")        
        print("\t\tAddress Line 1 :")
        print("\t\tAddress Line 2 :")
        print("\t\tCity           :")
        print("\t\tState          :")
        print("\t\tPin code       :")
              
    # method to Update Communication Address 
    # Exer4-C: 
    #       Write code required to update communication address of current_customer 
    #
    # NOTE: All the required objects are already created. Don't create any new object.
    # ----  Understand the relationship between classes and call appropriate methods to complete the functionality 
    #
    def update_communication_address(self,address):
        current_customer = self.__current_customer
        try:
            print("\n\n######## Exer4: Remove this print statement and write code required to update communication address \n\t File To Modify: DataAccess.DAO.py, Method To Modify: update_communication_address")
            return True
        except:
            return False
        
     
    # method to Update Installation Address    
    # Exer4-D: 
    #       Write code required to update installation address of current_customer   
    #
    # NOTE: All the required objects are already created. Don't create any new object.
    # ----  Understand the relationship between classes and call appropriate methods to complete the functionality 
    #
    def update_installation_address(self,address):
        current_customer = self.__current_customer
        try:
            print("\n\n######## Exer4: Remove this print statement and write code required to update installation address \n\t File To Modify: DataAccess.DAO.py, Method To Modify: update_installation_address")
            return True
        except:
            return False

# ========================================================================================================== #
#                                         END OF EXERCISE 4 
# ========================================================================================================== #


    # method to purchase product   
    def purchase_product(self,product_id):
        flag_prod=False
        
        for prod in CustomerDAO.product_list:
            if(prod.get_prod_id().upper()==product_id.upper()):
                product_purchased = prod
                flag_prod=True
                break
        if flag_prod == False:
            return -1           # error code if product id is invalid
        
        amount=0 #Local variable to store the current subscription amount
        current_customer = self.__current_customer
        if(current_customer.get_subscription_amount()):
            amount = current_customer.get_subscription_amount()
        try:
            #Adding amount of purchased product to existing amount
            current_customer.set_subscription_amount(amount + product_purchased.get_price())
            #Adding product purchased to the Product list of the customer
            current_customer.get_product_list().append(product_purchased)
            return 1     # success code
        except:
            return 0     # error code in case of any exception
        

# ========================================================================================================== #
#                                         EXERCISE 5 
# Write code in the method below to purchase the deal:  
#    1. add all the products of deal_purchased to product_list of current_customer, 
#    2. calculate total subscription amount of all products of selected_deal, 
#    3. add it to subscription amount of current_customer and 
#    4. deduct discount of the deal from subscription amount  
#
# NOTE: All the required objects are already created. Don't create any new object.
# ----  Understand the relationship between classes and implement the functionality.        
# ========================================================================================================== #
        
    # method to Purchase a deal
    def purchase_deal(self, deal_id):
        # searching for the deal id
        flag_deal = False   
        for deal in CustomerDAO.deal_list:
            if(deal.get_deal_id().upper()==deal_id.upper()):
                selected_deal = deal
                flag_deal=True
                break
        if flag_deal == False:
            return -1           # error code if product id is invalid
        
        # selected_deal contains the deal selected by the current_customer 
        
        current_customer = self.__current_customer     
        print("\n\n######## Exer5: Remove this print statement and write code required to purchase the deal: " +
              "\n\t add all the products of the selected deal to product_list of current customer, " + 
              "\n\t calculate total subscription amount of all products of selected deal, " + 
              "\n\t add it to subscription amount of current customer and \n\t deduct discount of the deal from subscription amount. " + 
              "\n\t File To Modify: DataAccess.DAO.py, Method To Modify: purchase_deal" +
              "\n\n"
            )
        
        
        # return 1 # if successful
        return 0 # if unsuccessful 

# ========================================================================================================== #
#                                         END OF EXERCISE 5 
# ========================================================================================================== #
    
    
    # method to display current customer's details    
    def view_profile(self):
        current_customer = self.__current_customer
        print("*Customer Details*".center(100,"*"))
        print()
        print("\t Name                  : ",current_customer.get_name())
        print("\t Mobile No             : ",current_customer.get_mobile_number())
        print("\t Subscription Amount   : ",current_customer.get_subscription_amount())
        
        self.display_communication_address()
        self.display_installation_address()
        print()
        
        if len(current_customer.get_product_list()) == 0:
            print("\t No products purchased")
        else:
            print("\t Products purchased   : ")
            from Presentation.menu import MainClass
            MainClass.disp_header(("Category", "ID", "Name", "Subscription Amount", "Other details"), (10,5,15,22,30),10)
            for prod in current_customer.get_product_list():
                print(" ".rjust(11," "),end=" ")
                print(prod.__class__.__name__.ljust(12), end="")
                print(prod)
        print("*".rjust(100,"*"))
        

    # method to write changes to the file when customer logs out
    def logout(self):
        update_customer(CustomerDAO.customer_list)
                           
