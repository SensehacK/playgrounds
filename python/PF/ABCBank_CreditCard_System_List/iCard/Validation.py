
'''This function checks the availability of reward scheme of specified card_type, if available return True 
   otherwise False.
   
   Input: Card type as string and card reward details as tuple of lists i.e. card type list, 
   min. transaction amount list and  associated reward points list.
   
   Output: If valid card type returns True, otherwise False
'''
def validate_card_availability(card_type, card_reward_details):
    if(card_type not in card_reward_details[0]):
        return False
    else:
        return True    
    