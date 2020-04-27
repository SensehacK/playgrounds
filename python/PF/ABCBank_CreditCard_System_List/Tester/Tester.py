from iCard.Display_Schemes import display_all_scheme_details
from iTransact.Compute_Reward import calculate_reward_points
from iTransact.Compute_Reward import update_customer_reward_points
from iTransact.Customer_Details import get_reward_points
from iTransact.Display_Customer_Details import display_customer_details
from iTransact.Read_Write_Customer_rewards import get_customer_reward_details,set_customer_reward_details
from iCard.Read_Write_Reward_Scheme import get_reward_scheme_details,set_reward_scheme_details


end=False
card_reward_details=get_reward_scheme_details()
cust_reward_details=get_customer_reward_details()
while(end==False):
    print()
    print("       Welcome to ABC Bank Credit Card System!!      ")
    print("*****************************************************") 
    print("                   Admin Module                      ")
    print("*****************************************************")
    print("Choose an option from below:")
    print("-----------------------------------------------------") 
    print("1. Display All Reward Schemes")
    print("2. Find Reward Points by Customer Id")
    print("3. Find Reward Points for a Transaction amount")
    print("4. Update Customer Reward Details for a Transaction")
    print("5. Display All Customers Details")
    print("6. Exit")
    print("*****************************************************")
    option=input("Enter your choice:")
    if(option.isdigit() and (int(option)>=1 and int(option)<=9)):
        if(int(option)==1):
            print("-------------------------------------------------")
            print("Display All Reward Schemes")
            print("-------------------------------------------------")
            display_all_scheme_details(card_reward_details)
            print("*****************************************************")
        if(int(option)==2):
            print("-------------------------------------------------")
            print("Find Reward Points by Customer Id")
            print("-------------------------------------------------")
            cust_id=input("Enter Customer Id:")
            print()
            print("-------------------------------------------------")
            reward=get_reward_points(cust_id,cust_reward_details)
            if(reward!=None):
                print("Reward Points for customer id",cust_id,"is: ",reward)
                print("-------------------------------------------------")
            print("*****************************************************") 
        if(int(option)==3):
            print("-------------------------------------------------")
            print("Find Reward Points for a Transaction amount")
            print("-------------------------------------------------")
            card_type=input("Enter Card Type:")
            transaction_amt=input("Enter Transaction Amount:")
            print()
            print("-------------------------------------------------")
            reward=calculate_reward_points(card_type,transaction_amt,card_reward_details)
            if(reward!=None):
                print("For",card_type, "card and transaction amount",transaction_amt,"reward points are:", reward)
                print("-------------------------------------------------")   
            print("*****************************************************")
        if(int(option)==4):
            print("-------------------------------------------------")
            print("Update Customer Reward Details for a Transaction")
            print("-------------------------------------------------")
            cust_id=input("Enter Customer Id:")
            card_type=input("Enter Card Type:")
            transaction_amt=input("Enter Transaction Amount:")
            print()
            print("-------------------------------------------------")
            cust_reward_details1=update_customer_reward_points(cust_id,card_type,transaction_amt,card_reward_details,cust_reward_details)
            print("-------------------------------------------------")
            if(cust_reward_details1!=None):
                cust_reward_details=cust_reward_details1
                print("Customer Rewards after updation") 
                print("-------------------------------------------------") 
                display_customer_details(cust_reward_details)
            print("*****************************************************")
        if(int(option)==5):
            print("-------------------------------------------------")
            print("Display All Customers Details")
            print("-------------------------------------------------")
            display_customer_details(cust_reward_details)
            print("*****************************************************") 
        if(int(option)==6):
            set_reward_scheme_details(card_reward_details[0],card_reward_details[1],card_reward_details[2])
            set_customer_reward_details(cust_reward_details[0],cust_reward_details[1],cust_reward_details[2])
            print("Thank you!")
            end=True
    else:
        print()
        print("********************************************")
        print(" Please enter a valid option ( 1,2,3,4,5,6 )")
        print("********************************************")
    

