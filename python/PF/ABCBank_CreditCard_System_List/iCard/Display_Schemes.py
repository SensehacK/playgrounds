
from iCard.Validation import validate_card_availability
'''This function displays the details of scheme for a specified card type.

   Input: Card type as string and card reward details as tuple of lists i.e. card type list, 
   min transaction amount list and  associated reward points list.
   
   Output: Displays the details of scheme for a specified card type on console.
'''
def display_scheme_details(card_type,card_reward_details):
    if(validate_card_availability(card_type,card_reward_details)):
        
        card_type_list=card_reward_details[0]
        min_trasaction_amt_list=card_reward_details[1]
        reward_point_list=card_reward_details[2]
        for i in range(len(card_type_list)):
            if(card_type_list[i]==card_type):
                index=i
                break
        reward_point=reward_point_list[index]
        min_transaction_amt=min_trasaction_amt_list[index]
        print(" ---------------------------------------------------------------------")
        print("|      Card Type     |   Min. Transaction Amount   |   Reward Points  |")
        print(" ---------------------------------------------------------------------")
        print("|"+" "*((21-len(card_type))//2)+card_type+" "*((21-len(card_type))//2)+"|", "             "+min_transaction_amt+"             |", "        "+reward_point+"        |")
        print(" ---------------------------------------------------------------------")
    else:
        print("ERROR:Invalid Card Type ")

'''This function displays the details of all reward schemes. 
   Input: Card reward details as tuple of lists i.e. card type list, min transaction amount list and  
   associated reward points list.
   Output: Displays the details of all reward schemes on console.
'''
def display_all_scheme_details(card_reward_details):
    
    card_type_list=card_reward_details[0]
    min_trasaction_amt_list=card_reward_details[1]
    reward_point_list=card_reward_details[2]
    print(" ---------------------------------------------------------------------")
    print("|      Card Type     |   Min. Transaction Amount    |   Reward Points |")
    print(" ---------------------------------------------------------------------")
    for i in range(len(card_type_list)):
        print("|"+" "*((21-len(card_type_list[i]))//2)+card_type_list[i]+" "*((20-len(card_type_list[i]))//2)+"|"," "*((29-len(min_trasaction_amt_list[i]))//2)+min_trasaction_amt_list[i]+" "*((28-len(min_trasaction_amt_list[i]))//2)+"","|"+" "*((18-len(reward_point_list[i]))//2)+reward_point_list[i]+" "*((18-len(reward_point_list[i]))//2)+"|")
        print(" ---------------------------------------------------------------------")
    
