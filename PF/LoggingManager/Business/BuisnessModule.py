'''
Created on Nov 15, 2016

@author: Abhilash.S12
*** READ THE FUNCTION HEADER TO IDENTIFY THE FUNCTIONS TO BE MODIFIED***
'''
from Persistence.FileHandling import get_userdetails_from_file, \
     update_customer_deatils_to_file
import re




'''
Function to validate the phone number.  
MODIFY the regular expression according to the requirements given
in Exercise 2  
'''
def validate_phone(phone):
    if(re.search(r'^[1-9][0-9]{9}$',phone)==None):
        return False
    return True
    

'''
Function to validate the PAN.  
MODIFY the regular expression according to the requirements given
in Exercise 3
'''

def validate_pan(pan):
    if(re.search(r'(^[A-Z]{5}[0-9]{4}[A-Z]$)',pan)==None):
        return False
    return True


'''
Function to validate the email id.  
MODIFY the regular expression according to the requirements given
in Exercise 4  
'''
# ab_c@d.co.in ^[A-Za-z0-9]
def validate_emailid(emailid):
    if(re.search("^[a-zA-Z]\w*[a-zA-Z0-9]{1}@[a-zA-Z]+(\.[a-z][a-z]+)?\.[a-z][a-z]+$")==None):
            return False
    return True

#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------
'''
Function to get the user data
*** DO NOT MODIFY THIS FUNCTION***
'''
def get_user_details(customer_id):    
    users_data=get_userdetails_from_file(customer_id) 
    return users_data  


'''
Function to update the PAN in customer record
*** DO NOT MODIFY THIS FUNCTION***
'''

def update_pan(cust_id,pan):    
    customer_data=get_user_details(cust_id)
    old_pan=customer_data.split(",")[2]
    updated_customer_data=re.sub(old_pan,pan,customer_data)
    update_customer_deatils_to_file(updated_customer_data,customer_data)       

'''
Function to update the Phone number in customer record
*** DO NOT MODIFY THIS FUNCTION***
''' 
def update_phone(cust_id,ph_no):        
    customer_data=get_user_details(cust_id)
    old_ph_no=customer_data.split(",")[3]
    updated_customer_data=re.sub(old_ph_no,ph_no,customer_data)
    update_customer_deatils_to_file(updated_customer_data,customer_data)
    
'''
Function to update the Email id in customer record
*** DO NOT MODIFY THIS FUNCTION***
'''  
def update_emailid(cust_id,emailid):        
    customer_data=get_user_details(cust_id)
    old_emailid=customer_data.split(",")[1]
    updated_customer_data=re.sub(old_emailid,emailid,customer_data)
    update_customer_deatils_to_file(updated_customer_data,customer_data)

'''
Function to process the match object
*** DO NOT MODIFY THIS FUNCTION***
'''
def get_match(m,string):
    try:
        match=""        
        match=m.group()
        match=match[1:]
    except AttributeError:
        print("No match found")
    finally:
        return match
