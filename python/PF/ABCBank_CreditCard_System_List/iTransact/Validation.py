'''This function checks the availability of customer of specified cust_id.
   Input: Customer Id as string and customer rewards details as tuple of lists i.e. customer id list, 
   card type list and reward points list.
   Output: If customer id available returns True, otherwise False.
'''
def validate_customer_id(cust_id,cust_reward_details):
    if(cust_id not in cust_reward_details[0]):
        return False
    else:
        return True
'''This function checks the availability of customer of specified cust_id and if customer
   details are available whether it matches with specified card_type or not.
   Input: Customer Id, card type as string, card reward details as tuple of lists i.e. card type list, 
   min transaction amount list and  associated reward points list and customer rewards details as 
   tuple of lists i.e. customer id list, card type list and reward points list.
   Output: If details are valid returns True, otherwise False.
'''   
def validate_details(cust_id,card_type,card_reward_details,cust_reward_details):
    if(cust_id not in cust_reward_details[0]):
        return False
    elif(card_type not in card_reward_details[0]):
        print("ERROR:Invalid Card Type")
        return False
    else:
        for i in range(len(cust_reward_details[0])):
            if(cust_reward_details[0][i]==cust_id):
                index=i
                break
        if(cust_reward_details[1][index]==card_type):
            return True
        else:
            print("ERROR:Customer do not have specified Card Type")
            return False
    
    