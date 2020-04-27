'''This function checks the availability of reward scheme of specified card_type, if available return True 
   otherwise False.
   
   Input: Card type as string and as a dictionary which contains card type(string) as key, 
   minimum transaction amount(string) and reward points(string) as values in form of a list
   
   Output: If valid card type returns True, otherwise False
'''
   
def validate_card_availability(card_type, card_reward_details_dict):
    if(card_type not in card_reward_details_dict.keys()):
        return False
    else:
        return True    