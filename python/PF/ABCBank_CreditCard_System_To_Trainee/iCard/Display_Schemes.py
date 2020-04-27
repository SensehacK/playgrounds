
'''This function displays the details of all reward schemes. 

   Input: Card reward details as a dictionary which contains card type(string) as key, 
   minimum transaction amount(string) and reward points(string) as values in form of a list.
   
   Output: Displays the details of all reward schemes on console.
'''
def display_all_scheme_details(card_reward_details_dict):
    if(card_reward_details_dict!=None):
        print(" ---------------------------------------------------------------------")
        print("|      Card Type     |   Min. Transaction Amount    |   Reward Points |")
        print(" ---------------------------------------------------------------------")
        for k,v in card_reward_details_dict.items():
            print("|"+" "*((21-len(k))//2)+k+" "*((20-len(k))//2)+"|"," "*((29-len(v[0]))//2)+v[0]+" "*((28-len(v[0]))//2)+"","|"+" "*((18-len(v[1]))//2)+v[1]+" "*((18-len(v[1]))//2)+"|")
            print(" ---------------------------------------------------------------------")
    else:
        print("No card details are available")
