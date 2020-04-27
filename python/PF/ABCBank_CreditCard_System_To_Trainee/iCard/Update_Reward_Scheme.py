
from iCard.Validation import validate_card_availability

'''This function should add a new reward scheme in the card_reward_details_dict and returns the updated dictionary.
   It checks if reward scheme with specified card is already available or not and min transaction amount and 
   reward points are greater than 0 or not before adding the reward scheme.
   
   Input: Card type, Min. transaction amount, reward points as strings and card reward details as a dictionary
   which contains card type(string) as key, minimum transaction amount(string) and reward points(string) as 
   values in form of a list.
   
   Output: If valid card type returns the updated dictionary, otherwise returns -1 with error message.
'''
def add_reward_scheme(card_type,min_transaction_amt, reward_point,card_reward_details_dict):
    #You may use validate_card_availability() function for validating card type
    print("Implement the given exercises")#Remove this print statement and write your code
  
  
  
'''This function deletes the reward scheme of specified card_type from the card_reward_details_dict and returns 
   the updated dictionary. It checks if reward scheme with specified card is already 
   available or not  before deleting the reward scheme.
   
   Input: Card type  as string and card reward details as a dictionary which contains card type(string) as 
   key, minimum transaction amount(string) and reward points(string) as values in form of a list.
   
   Output: If valid card type returns the updated dictionary, otherwise returns -1 with error message.
'''
def delete_reward_scheme(card_type,card_reward_details_dict):
    if(card_reward_details_dict!=None):
        if(validate_card_availability(card_type,card_reward_details_dict)):
            card_reward_details_dict.pop(card_type)
            return card_reward_details_dict
        else:
            print("ERROR:Invalid Card Type ")
            return -1
    else:
        print("Implement the given exercises")#Remove this print statement and write your code
    
        
  
'''This function should update the reward scheme of specified card_type from the card_reward_details_dict and returns 
   the updated dictionary. It checks if reward scheme with specified card_type is already 
   available or not and min. transaction amount and reward points are greater than 0 or not before updating 
   the reward scheme.
   
   Input: Card type, Min. transaction amount, reward points as string and card reward details as a 
   dictionary which contains card type(string) as key, minimum transaction amount(string) and 
   reward points(string) as values in form of a list
   
   Output: If details are valid returns the updated dictionary, otherwise returns -1 with error message
'''
def update_reward_scheme(card_type,min_transaction_amt, reward_point,card_reward_details_dict):
    if(card_reward_details_dict!=None):
        if(validate_card_availability(card_type,card_reward_details_dict)):
            if(int(min_transaction_amt)>0 ):
                if(int(reward_point)>0):
                    card_reward_details_dict[card_type]=[min_transaction_amt, reward_point]
                    return card_reward_details_dict
                else:
                    print("ERROR: Invalid reward points")
                    return -1
            else:
                print("ERROR: Invalid min. transaction amount")
                return -1
        else:
            print("ERROR:Invalid Card Type ")
            return -1
    else:
        print("Implement the given exercises")#Remove this print statement and write your code
        
      
