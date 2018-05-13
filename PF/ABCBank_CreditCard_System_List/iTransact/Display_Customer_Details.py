
'''This function displays the details of all customers reward details. 
   Input: Customer reward details as tuple of lists i.e. customer id list, card type list and 
   reward points list.
   Output: Displays the details of all customers rewards on console.
'''
def display_customer_details(cust_reward_details):
    cust_id_list=cust_reward_details[0]
    card_type_list=cust_reward_details[1]
    reward_point_list=cust_reward_details[2]
    print(" -------------------------------------------------------------")
    print("|    Customer ID    |       Card Type      |   Reward Points |")
    print(" -------------------------------------------------------------")
    for i in range(len(cust_id_list)):
        print("|"+" "*((20-len(cust_id_list[i]))//2)+cust_id_list[i]+" "*((19-len(cust_id_list[i]))//2)+"|"," "*((21-len(card_type_list[i]))//2)+card_type_list[i]+" "*((22-len(card_type_list[i]))//2)+"|"," "*((17-len(reward_point_list[i]))//2)+reward_point_list[i]+" "*((16-len(reward_point_list[i]))//2)+"|")
        print(" -------------------------------------------------------------")
    
