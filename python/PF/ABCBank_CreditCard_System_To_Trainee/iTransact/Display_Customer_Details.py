
'''This function displays the details of all customers reward details. 
   
   Input: Customer rewards details as a dictionary contains customer id(string) as key, 
   card type(string) and reward points(string) as values in form of a list.
   
   Output: Displays the details of all customers rewards on console.
'''

def display_customer_details(cust_reward_details_dict):
    
    print(" -------------------------------------------------------------")
    print("|    Customer ID    |       Card Type      |   Reward Points |")
    print(" -------------------------------------------------------------")
    for k,v in cust_reward_details_dict.items():
        print("|"+" "*((20-len(k))//2)+k+" "*((19-len(k))//2)+"|"," "*((21-len(v[0]))//2)+v[0]+" "*((22-len(v[0]))//2)+"|"," "*((17-len(v[1]))//2)+v[1]+" "*((16-len(v[1]))//2)+"|")
        print(" -------------------------------------------------------------")
    
