
from iCard.Validation import validate_card_availability
from iTransact.Validation import validate_details,validate_customer_id 


'''This function calculates and returns the reward points for a particular transaction amount.
   It validates the availability of card_type in card_reward_details before doing the calculation
   
   Input: Card type, transaction amount as string and card reward details as tuple of lists i.e. 
   card type list, min. transaction amount list and  associated reward points list.
   
   Output: If valid card type returns the calculated reward points, otherwise returns None with error message.
'''
def calculate_reward_points(card_type,transaction_amt,card_reward_details):
    card_type_list=card_reward_details[0]
    min_trasaction_amt_list=card_reward_details[1]
    reward_point_list=card_reward_details[2]
    index=-1
    if(validate_card_availability(card_type,card_reward_details)):
        for i in range(len(card_type_list)):
            if(card_type_list[i]==card_type):
                index=i
                break
        reward_point=reward_point_list[index]
        min_transaction=min_trasaction_amt_list[index]
        total_reward_points=int(int(transaction_amt)*int(reward_point)/int(min_transaction))
        return total_reward_points
    else:
        print("ERROR:Invalid Card Type ")
        return None

'''This function updates the customer reward points and returns a tuple of updated lists for a particular 
   transaction amount. It validates the availability of card_type in card_reward_details and whether 
   customer have the specified card_type before doing the update. If the customer is a new one then add his 
   details in the lists otherwise update his existing reward points by adding freshly earned ones.
   
   Input: Customer Id, card type, transaction amount as string, card reward details as tuple of lists i.e. 
   card type list, min transaction amount list and  associated reward points list and customer rewards details
   as tuple of lists i.e. customer id list, card type list and reward points list.
   
   Output: If details are valid returns the updated customer reward details, otherwise returns None 
   with error message.
'''
def update_customer_reward_points(customer_id, card_type, transaction_amt,card_reward_details,cust_reward_details):
    if(validate_details(customer_id,card_type,card_reward_details,cust_reward_details)):
        
        cust_id_list=cust_reward_details[0]
        card_type_list=cust_reward_details[1]
        reward_point_list=cust_reward_details[2]
        reward_earned=calculate_reward_points(card_type,transaction_amt,card_reward_details)
        index=-1
        for i in range(len(cust_id_list)):
            if(cust_id_list[i]==customer_id):
                index=i
                break
        reward_point_list[index]=str(int(reward_point_list[index])+int(reward_earned))
        print("Reward points for the transaction is:",reward_earned)
        return (cust_id_list,card_type_list,reward_point_list)
    elif(not validate_customer_id(customer_id,cust_reward_details)):
        if( validate_card_availability(card_type,card_reward_details)):
            cust_id_list=cust_reward_details[0]
            card_type_list=cust_reward_details[1]
            reward_point_list=cust_reward_details[2]
            reward_earned=calculate_reward_points(card_type,transaction_amt,card_reward_details)
            cust_id_list.append(customer_id)
            card_type_list.append(card_type)
            reward_point_list.append(str(int(reward_earned)))
            print("Customer added successfully with Id",customer_id)
            print("Reward points for the transaction is:",reward_earned) 
            return (cust_id_list,card_type_list,reward_point_list)
        else:
            print("ERROR:Invalid Card Type ")
            return None  
    else:
        return None
