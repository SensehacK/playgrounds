
from iCard.Validation import validate_card_availability


'''This function adds a new reward scheme in the lists and returns the tuple of updated lists.
   It checks if reward scheme with specified card is already available or not before adding 
   the reward scheme.
   
   Input: Card type, Min. transaction amount, reward points as string and card reward details as tuple of 
   lists i.e. card type list, min. transaction amount list and  associated reward points list.
   
   Output: If valid card type returns the tuple of updated lists, otherwise returns None with error message.
'''
def add_reward_scheme(card_type,min_transaction_amt, reward_point,card_reward_details):
    if(not validate_card_availability(card_type, card_reward_details)):
        card_type_list=card_reward_details[0]
        min_trasaction_amt_list=card_reward_details[1]
        reward_point_list=card_reward_details[2]
        card_type_list.append(card_type)
        min_trasaction_amt_list.append(min_transaction_amt)
        reward_point_list.append(reward_point)
        return (card_type_list,min_trasaction_amt_list,reward_point_list)
    else:
        print("ERROR:Card Type is already available")
        return None
  
  
'''This function deletes the reward scheme of specified card_type from the lists and returns 
   the tuple of updated lists. It checks if reward scheme with specified card is already 
   available or not before deleting the reward scheme .
   
   Input: Card type as string and card reward details as tuple of lists i.e. card type list, min. transaction 
   amount list and  associated reward points list.
   
   Output: If valid card type returns the tuple of updated lists, otherwise returns None with error message.
'''
def delete_reward_scheme(card_type,card_reward_details):
    if(validate_card_availability(card_type,card_reward_details)):
        card_type_list=card_reward_details[0]
        min_trasaction_amt_list=card_reward_details[1]
        reward_point_list=card_reward_details[2]
        for i in range(len(card_type_list)):
            if(card_type_list[i]==card_type):
                index=i
                break
        card_type_list.pop(index)
        min_trasaction_amt_list.pop(index)
        reward_point_list.pop(index)
        return (card_type_list,min_trasaction_amt_list,reward_point_list)
    else:
        print("ERROR:Invalid Card Type ")
        return None
    
    
  
'''This function updates the reward scheme of specified card_type from the lists and returns 
   the tuple of updated lists. It checks if reward scheme with specified card_type is already 
   available or not before updating the reward scheme.
   
   Input: Card type, Min. transaction amount, reward points as string and card reward details as tuple of 
   lists i.e. card type list, min. transaction amount list and  associated reward points list.
   
   Output: If valid card type returns the tuple of updated lists, otherwise returns None with error message.
'''
def update_reward_scheme(card_type,min_transaction_amt, reward_point,card_reward_details):    
    if(validate_card_availability(card_type,card_reward_details)):        
        card_type_list=card_reward_details[0]
        min_trasaction_amt_list=card_reward_details[1]
        reward_point_list=card_reward_details[2]
        
        for i in range(len(card_type_list)):
            if(card_type_list[i]==card_type):
                index=i
                break
        reward_point_list[index]=reward_point
        min_trasaction_amt_list[index]=min_transaction_amt
        
        return (card_type_list,min_trasaction_amt_list,reward_point_list)
    
    else:
        print("ERROR:Invalid Card Type ")
        return None
    
      
