
from iTransact.Validation import validate_customer_id
'''This function returns the accumulated reward points of specified customer. 

   Input: Customer Id as string and customer rewards details as tuple of lists i.e. 
   customer id list, card type list and reward points list.
   
   Output: If customer id is valid returns the accumulated reward points, otherwise returns None with 
   error message.
'''
def get_reward_points(customer_id,cust_reward_details):
    
    if(validate_customer_id(customer_id,cust_reward_details)):
        
        cust_id_list=cust_reward_details[0]
        reward_point=cust_reward_details[2]
        
        index=-1
        for i in range(len(cust_id_list)):
            if(cust_id_list[i]==customer_id):
                index=i
                break
        return reward_point[index]
    else:
        print("ERROR:Invalid Customer Id")
        return None
