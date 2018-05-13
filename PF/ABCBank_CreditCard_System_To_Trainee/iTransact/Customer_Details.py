
from iTransact.Validation import validate_customer_id


'''This function returns the accumulated reward points of specified customer. 
   
   Input: Customer Id as string and customer rewards details as a dictionary contains customer id(string) 
   as key,card type(string) and reward points(string) as values in form of a list.
   
   Output: If customer id is valid returns the accumulated reward points, otherwise returns -1 with error message
'''
def get_reward_points(customer_id,cust_reward_details_dict):    
    if(validate_customer_id(customer_id,cust_reward_details_dict)):
        return cust_reward_details_dict[customer_id][1]
    else:
        print("ERROR:Invalid Customer Id")
        return -1
    
    
'''This function should return the customer id of the customer who has maximum reward points accumulated. 

   Input: Customer rewards details as a dictionary contains customer id(string) as key, 
   card type(string) and reward points(string) as values in the form of a list
   
   Output: Customer id of the customer who has maximum reward points accumulated
''' 
def get_top_customer(cust_reward_details_dict):
    print("Implement the given exercise")#Remove this print statement and write your code
