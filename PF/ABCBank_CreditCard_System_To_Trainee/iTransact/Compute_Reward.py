
from iCard.Validation import validate_card_availability
from iTransact.Validation import validate_customer_id 


'''This function should calculate and return the reward points for a particular transaction amount.
   It should validate the availability of card_type in card_reward_details before doing the calculation.
   
   Input: card type, transaction amount as string, 
          card reward details as a dictionary which contains card type(string) as key, 
               minimum transaction amount(string) and reward points(string) as values in form of a list.
   
   Output: If valid card type returns the calculated reward points, otherwise returns -1 with error message.
'''
def calculate_reward_points(card_type,transaction_amt,card_reward_details_dict):
    
    
    print("Debug prints start ")
    print(card_type)
    print(transaction_amt)
    transaction_int = int(transaction_amt)
    print(card_reward_details_dict)
    print("Minimum Transaction")
    print(card_reward_details_dict[card_type][0])
    print("Minimum Rewards")
    print(card_reward_details_dict[card_type][1])
    
    min_trans = int(card_reward_details_dict[card_type][0])
    min_rewards = int(card_reward_details_dict[card_type][1])
    
    
    print("type(transaction_amt)")
    print(type(transaction_amt))
    print("type(min_rewards)")
    print(type(min_rewards))
    print("type(min_trans)")
    print(type(min_trans))
    
    div = transaction_int // min_trans
    print("div = transaction_int // min_trans")
    print(div)
    
    rewards_points = div * min_rewards
    print("rewards_points = div * min_rewards")
    print(rewards_points)
    
    print("Debug prints ends ")
    
    return rewards_points



'''This function should update the customer reward points and should return updated customer reward details 
   dictionary.It should validate the availability of card_type in card_reward_details and whether customer 
   has the specified card type or not before doing the update. If the customer is a new one then 
   add his details in the dictionary otherwise update his existing reward points by adding freshly earned ones.
   
   Input: customer Id, card type, transaction amount as string, 
          card reward details as a dictionary which contains card type(string) as key, 
               minimum transaction amount(string) and reward points(string) as values in form of a list, 
          customer rewards details as a dictionary which contains customer id(string) as key, 
               card type(string) and reward points(string) as values in form of a list
   
   Output: If details are valid returns the updated customer reward details dictionary, 
           otherwise returns -1 with error message.
'''
def update_customer_reward_points(customer_id, card_type, transaction_amt,card_reward_details_dict,cust_reward_details_dict):
    print("Implement the given exercises")#Remove this print statement and write your code
    print("cust_reward_details_dict")
    print(cust_reward_details_dict)
    print("Calculate Rewards , Calling Functions")
    print("/////////////////////////////////////////////////////")
    rewards_points =  calculate_reward_points(card_type,transaction_amt,card_reward_details_dict)
    print("/////////////////////////////////////////////////////")
    print("Calculate Rewards , Completed Functions")
    print("rewards_points")
    print(rewards_points)
    print(type(rewards_points))
    print("/////////////////////////////////////////////////////")
    print("/////////////////////////////////////////////////////")
    print("cust_reward_details_dict[customer_id]")
    print(cust_reward_details_dict[customer_id])
    print("Before Updating cust_reward_details_dict[customer_id][1]")
    print(cust_reward_details_dict[customer_id][1])
    old_rewards = int(cust_reward_details_dict[customer_id][1])
    print("Old rewards")
    print(old_rewards)
    new_rewards = str(old_rewards + rewards_points)
    print("New rewards")
    print(new_rewards)
    
    cust_reward_details_dict[customer_id][1] = new_rewards
    print("After Updating cust_reward_details_dict[customer_id][1]")
    print(cust_reward_details_dict[customer_id][1])
    
    
    
    print("/////////////////////////////////////////////////////")
    print("/////////////////////////////////////////////////////")
    print("Final Result")
    print("/////////////////////////////////////////////////////")
    print("/////////////////////////////////////////////////////")
    print("cust_reward_details_dict")
    print(cust_reward_details_dict)
    
    return cust_reward_details_dict
    
    
    
