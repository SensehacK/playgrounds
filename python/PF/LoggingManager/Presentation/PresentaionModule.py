'''
Created on Nov 15, 2016

@author: Abhilash.S12
*** DO NOT MODIFY THIS FILE***
'''
from Business.BuisnessModule import validate_phone,update_phone,validate_pan,update_pan,validate_emailid,update_emailid

def kyc_menu():
    choice=None
    while(choice!="4"):
        print()
        print(" 1. Update Phone Number")
        print(" 2. Update PAN ")
        print(" 3. Update Email Id")
        print(" 4. Exit")
        print()
        print("Select an option")
        choice=input("")
        if(choice=="4"):
            exit()
        while(not(choice in ["1","2","3","4","5"])):
            print("Invalid Choice")
            print()
            print(" 1. Update Phone Number")
            print(" 2. Update PAN ")
            print(" 3. Update Email Id")
            print(" 4. Exit")
            print()
            print("Select an option")
            choice=input("")
        cust_id=input("Enter the customer ID:")
        if(choice=="1"):
            print("Enter the new Phone Number you wish to register")
            phone_no=input("")
            if(not validate_phone(phone_no)):
                print(" Invalid phone number ")
            else:            
                update_phone(cust_id,phone_no)            
        if(choice=="2"):
            print("Enter the new PAN you wish to register")
            pan=input("")
            if(validate_pan(pan)):
                update_pan(cust_id,pan)
            else:
                print("Invalid Pan")            
        if(choice=="3"):
            print("Enter the new Email Id you wish to register")
            emailid=input("")
            if(not validate_emailid(emailid)):
                print("Invalid Email Id")
            else:
                update_emailid(cust_id,emailid)
        
        
    
kyc_menu()