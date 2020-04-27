'''
Created on Nov 15, 2016

@author: Abhilash.S12
*** DO NOT MODIFY THIS FILE***
'''
import re
def get_userdetails_from_file(customer_id):
    f = open(r"../Files/CustomerData.txt")     
    for rows in f:
        rows=rows[:-1]
        if(rows.split(",")[0]==customer_id):
            f.close()
            return rows
    f.close()        
    return None

def update_customer_deatils_to_file(updated_customer_data,customer_data):
    f=open(r'../Files/CustomerData.txt','r')    
    old_data=f.read()
    f.close()
    f=open(r'../Files/CustomerData.txt','w')
    updated_data=re.sub(customer_data,updated_customer_data,old_data)
    f.write(updated_data)
    f.close()
