from DataAccess.DAO import CustomerDAO
from BusinessLogic.validation import Validator
from DataAccess.bean import Address
import time

class MainClass:
    # login screen
    @staticmethod
    def main_menu():
        # Login Screen 
        print('Welcome to ILG Telecom!'.center(50))
        print("===========".rjust(50,'='))
        option=53
        print()
        print("--------------".center(50))
        print("|    Menu    |".center(50))
        print("--------------".center(50))
        print('\n'*2)
        # Loop to display login until customer chooses to exit.
        while (1):
            
            print("1. Login ".rjust(24,' '))
            print("2. Exit".rjust(22,' '))
            try:
                flag=True
                # Customer Input
                option=int(input("Enter your option : ".rjust(30,' ')))
                print()
            except Exception:
                # Exception to catch typographical error 
                print("Enter a valid digit".rjust(30,' '))
                flag=False
            if((option<1 or option>5) and flag):
                # Exception to catch a number which is not listed in menu
                print("Wrong option! Choose again".rjust(30,' '))
                
            elif(option==1 and flag == True): 
                try:      
                    # accept customer id and password  
                    customer_id = input("Enter Customer ID : ".rjust(30,' '))  
                    password =    input("Enter Password    : ".rjust(30,' '))
                    print()
                    print(" ".rjust(10," "),end=' ')
                    
                    # introduce delay
                    print("Loading",end="")
                    for i in range(10,0,-1):
                        print(".",end='')
                        time.sleep(i*.1/2)
                    print()
                    
                    # validate customer id and password
                    customer_dao = Validator.login_check(customer_id,password)
                    
                    # display success message for valid credentials
                    print("_".rjust(50,'_'))
                    # Success message on Login
                    print("Login Successful".center(50))
                    print("_".rjust(50,'_'))
                    time.sleep(1)
                    print('\n'*2)
                    print('\n'*70)
                    
                    # display menu for customer operations
                    MainClass.show_sub_menu(customer_dao) 
                    
                # handle exceptions                  
                except Exception as e:
                    # Invalid Customer ID error
                    if(str(e)=="Invalid Customer"):
                        print("_".rjust(50,'_'))
                        print("Invalid Customer ID")
                        print("_".rjust(50,'_'))
                        time.sleep(1)
                        print('\n'*70)
                    # Invalid Password error
                    elif(str(e)=="Password Mismatch"):
                        print("_".rjust(50,'_'))
                        print("Customer ID and password do not match")
                        print("_".rjust(50,'_'))
                        time.sleep(1)
                        print('\n'*70) 
                    # Invalid product Id error
                    elif(str(e)=="Invalid Product ID") :
                        print("Invalid Product ID") 
                    # Invalid deal Id error
                    elif(str(e)=="Invalid Deal ID") :
                        print("Invalid Deal ID" )
                    # Default exception to catch exceptions which are not listed above
                    else:
                        print("Sorry some error occurred")
                print("\n"*2)
                input("Press enter to continue...")
                print("\n"*70)
            elif(option==2 and flag ):
                print("Thank you !")
                return
    
    @staticmethod
    # display menu for Customer operations
    def show_sub_menu(customer_dao):
        choice= 100
        print("===========".rjust(50,'='))
        # To display the Customer Name
        print(("Hi "+customer_dao.get_current_customer().get_name()+"!").center(50))
        print("===========".rjust(50,'='))
        while(1):            
            try:
                print("1. Purchase Product            ".rjust(40," "))
                print("2. Update Communication Address".rjust(40," "))
                print("3. Update Installation Address ".rjust(40," "))
                print("4. View Profile                ".rjust(40," "))
                print("5. Log Off                     ".rjust(40,' '))
                print()
                
                try:
                    choice=int(input("Enter your option : ".rjust(25,' ')))
                except Exception:
                    print("Enter a valid digit".rjust(25,' '))
                if((choice<1 and choice>5)):
                    print("Wrong option! Choose again".rjust(35,' '))  
                elif(choice==1):
                    # display product list 
                    MainClass.show_product_list(customer_dao)  
                    
                    # accept the id of product / deal to buy
                    prod_or_deal_id = input("Enter the product/deal ID to purchase:")
                    
                    # call appropriate method to purchase deal / product
                    if(prod_or_deal_id[:4].upper()=='DEAL'):
                        purchased=customer_dao.purchase_deal(prod_or_deal_id)
                    else:
                        purchased=customer_dao.purchase_product(prod_or_deal_id) 
                                           
                    if (purchased==-1):
                        raise Exception("     Invalid ID. Try again")
                    elif(purchased==1):
                        # display success message and updated subscription amount
                        print()
                        print('='.rjust(100,'='))    
                        print("     Transaction Successful !  ") 
                        print("     Updated Monthly Subscription Amount:",customer_dao.get_current_customer().get_subscription_amount())
                        print('='.rjust(100,'=')) 
                    else:
                        raise Exception("     Transaction failed!")        # display error message
                elif(choice==2):
                    # display the current address
                    customer_dao.display_communication_address()
                    print()
                    # accept input for updated address
                    address = MainClass.accept_new_address()
                    # update address and display updated address
                    if(customer_dao.update_communication_address(address)):
                        print('='.rjust(100,'='))                        
                        print()
                        print("     Communication address updated successfully ")
                        print()
                        customer_dao.display_communication_address()
                        print('='.rjust(100,'='))
                    else:
                        # display error message 
                        print("     Operation failed !  ") 
                                    
                elif(choice==3):
                    # display the current address
                    customer_dao.display_installation_address()
                    print()
                    # accept the input for updated address
                    address = MainClass.accept_new_address()
                    # update address and display updated address
                    if(customer_dao.update_installation_address(address)):
                        print('='.rjust(100,'='))
                        print()
                        print("     Installation address updated successfully ")
                        print()
                        customer_dao.display_installation_address()
                        print('='.rjust(100,'='))
                    else:
                        # display error message
                        print("\n     Operation failed !  ")
                    
                elif(choice==4):
                    # call method to display customer details
                    customer_dao.view_profile()
                    
                elif(choice==5):
                    customer_dao.logout()
                    print("\n\n     Logged off successfully!")
                    break
            except Exception as e:
                print(e)
                
            print("\n"*2)
            input("Press enter to continue...")
            print("\n"*70)
    
    @staticmethod  
    # method to print the products and deals
    def show_product_list(customer):
        # create separate lists based on product category
        product_list = CustomerDAO.product_list
        dth_list=[]
        broadband_list=[]
        voip_list=[]
        for product in product_list:
            if(product.get_prod_id()[0]=='D'):
                dth_list.append(product)
            elif(product.get_prod_id()[0]=='B'):
                broadband_list.append(product)
            elif(product.get_prod_id()[0]=='V'):
                voip_list.append(product)
        
        #print DTH products
        print()
        print('-'.rjust(100,'-'))
        print("PRODUCTS".center(100))
        print('-'.rjust(100,'-'))
        print()
        
        # display all the products category-wise
        MainClass.disp_list("DTH Plans", ("ID", "Name", "Subscription Amount", "Service Provider", "Package"), (5,15,22,20,15), dth_list)
        MainClass.disp_list("Broadband Plans", ("ID", "Name", "Subscription Amount", "Speed", "Data Per Month"), (5,15,22,10,20), broadband_list)
        MainClass.disp_list("VoIP Plans", ("ID", "Name", "Subscription Amount", "IP", "Latency", "Per Call Bandwidth"), (5,15,22,10,10,20), voip_list)
        
        # display deals
        print("Deals: Buy multiple products and avail DISCOUNT!!!") 
        MainClass.disp_deal_header()  
        deal_list = CustomerDAO.deal_list
        for deal in deal_list:
            print(" ".rjust(5," "),end=" ")
            print(deal.get_deal_id().center(10)+str(deal.get_discount()).center(15), end="    ")
            # display products that are part of current deal
            for prod in deal.get_product_list():
                print((prod.get_prod_id() + " : " + prod.__class__.__name__).ljust(20) , end="  ")                 
            print()
        print("\n\n")

    
    @staticmethod
    # method to accept customer's new address
    def accept_new_address():
        print()
        print("Enter New Address ".rjust(25," "))
        address_line1 = input("Address Line1 : ".rjust(32," "))
        address_line2 = input("Address Line2 : ".rjust(32," "))
        city = input         ("City          : ".rjust(32," "))
        state = input        ("State         : ".rjust(32," "))
        pincode= input       ("Pincode       : ".rjust(32," "))
        print()
        # create a new address object with values accepted from the user 
        address = Address(address_line1, address_line2 ,city ,state , pincode)
        return address
    
    @staticmethod
    # method to display header and product list    
    def disp_list(prod_category, col_headers, col_width, prod_list_to_display):
        print(prod_category)
        MainClass.disp_header(col_headers, col_width, 5)        
        for prod in prod_list_to_display:
            print(" ".rjust(5," "),end=" ")
            print(prod)
        print('\n'*2)

    @staticmethod
    # method to display header    
    def disp_header(col_headers, col_width, initial_space):
        print(" ".rjust(initial_space," "),end=" ")
        print("----------------------------------------------------------------------------------------")
        print(" ".rjust(initial_space," "),end=" ")
        for index in range(len(col_headers)):
            print(col_headers[index].center(col_width[index]), end=" ")
        print()
        print(" ".rjust(initial_space," "),end=" ")
        print("----------------------------------------------------------------------------------------")
    
    @staticmethod
    # method to print deal header
    def disp_deal_header():
        print(" ".rjust(5," "),end=" ")
        print("----------------------------------------------------------------------------------------")
        print(" ".rjust(5," "),end=" ")
        print("ID".center(10),end=' ')
        print("Discount/month".center(15),end='   ')
        print("Product-1".ljust(20),end='  ')
        print("Product-2".ljust(20),end='  ')
        print("Product-3")
        print(" ".rjust(5," "),end=" ")
        print("----------------------------------------------------------------------------------------")  
        