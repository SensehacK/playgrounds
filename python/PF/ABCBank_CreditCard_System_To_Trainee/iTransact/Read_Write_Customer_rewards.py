import csv

'''This function fetches the details of all customers reward details from 
   CustomerRewardDetails CSV file in a dictionary and returns the same.
   
   Input: Path of CSV file.
   
   Output: Customer rewards details as a dictionary contains customer id(string) as key, 
   card type(string) and reward points(string) as values in form of a list.
'''
def get_customer_reward_details():
    file_pointer=open("..\\SuppliedFiles\\CustomerRewardDetails.csv","r")
    reward_scheme_details=csv.reader(file_pointer)
    cust_reward_details_dict={}
    for reward_detail in reward_scheme_details:
        card_type=reward_detail[0]
        min_transaction=reward_detail[1]
        reward_point=reward_detail[2]
        cust_reward_details_dict[card_type]=[min_transaction,reward_point]
    return cust_reward_details_dict

'''This function updates the details of customers reward details in 
   CustomerRewardDetails CSV file which are received as parameters in form of a dictionary.
   
   Input: Customer rewards details as a dictionary contains customer id(string) as key, 
   card type(string) and reward points(string) as values in form of a list.
   
   Output: Updates the CSV file.
'''
def set_customer_reward_details(cust_reward_details_dict):
    f=open("..\\SuppliedFiles\\CustomerRewardDetails.csv","w")
    f.write("")
    f.close()
    for k,v in cust_reward_details_dict.items():
        f=open("..\\SuppliedFiles\\CustomerRewardDetails.csv","a")
        f.write(str(k)+","+str(v[0])+","+str(v[1])+'\n')
    f.close()

