import csv
'''This function fetches the details of all customers reward details from 
   CustomerRewardDetails CSV file in 3 lists and returns them as tuple of lists.
   Input: Path of CSV file.
   Output: A tuple of lists i.e. customer id list, card type list and  earned reward points list.
'''
def get_customer_reward_details():
    file_pointer=open("..\\SuppliedFiles\\CustomerRewardDetails.csv","r")
    cust_details=csv.reader(file_pointer)
    cust_id_list=[]
    card_type_list=[]
    reward_point_list=[]
    for cust in cust_details:
        cust_id_list.append(cust[0])
        card_type_list.append(cust[1])
        reward_point_list.append(cust[2])
    file_pointer.close()
    return (cust_id_list,card_type_list,reward_point_list)

'''This function updates the details of customers reward details in 
   CustomerRewardDetails CSV file which are received as parameters in form of lists.
   Input: A tuple of lists i.e. customer id list, card type list and  earned reward points list.
   Output: Updates the CSV file.
'''
def set_customer_reward_details(cust_id_list,card_type_list,reward_point_list):
    f=open("..\\SuppliedFiles\\CustomerRewardDetails.csv","w")
    f.write("")
    f.close()
    for i in range(len(cust_id_list)):
        f=open("..\\SuppliedFiles\\CustomerRewardDetails.csv","a")
        f.write(str(cust_id_list[i])+","+str(card_type_list[i])+","+str(reward_point_list[i])+'\n')
    f.close()

