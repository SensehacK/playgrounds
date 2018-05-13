'''This function checks the availability of customer of specified cust_id.

   Input: Customer Id as string and Customer rewards details as a dictionary contains customer id(string) 
   as key, card type(string) and reward points(string) as values in form of a list.

   Output: If customer id available returns True, otherwise False.
'''
def validate_customer_id(cust_id,cust_reward_details_dict):
    if(cust_id not in cust_reward_details_dict.keys()):
        return False
    else:
        return True


    