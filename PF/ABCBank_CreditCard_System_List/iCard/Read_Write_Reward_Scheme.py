import csv
'''This function fetches the details of all reward schemes from SchemeDetails CSV file 
   in 3 lists and returns them as tuple of lists.
   
   Input: Path of CSV file.
   
   Output: A tuple of lists i.e. card type list, min transaction amount list and associated reward points list.
'''
def get_reward_scheme_details():
    file_pointer=open("..\\SuppliedFiles\\SchemeDetails.csv","r")
    reward_scheme_details=csv.reader(file_pointer)
    card_type_list=[]
    min_trasaction_amt_list=[]
    reward_point_list=[]
    for reward_detail in reward_scheme_details:
        card_type_list.append(reward_detail[0])
        min_trasaction_amt_list.append(reward_detail[1])
        reward_point_list.append(reward_detail[2])
    file_pointer.close()
    return (card_type_list,min_trasaction_amt_list,reward_point_list)

'''This function updates the details of reward schemes in SchemeDetails CSV file which 
   are received as parameters in form of lists.
  
   Input: A tuple of lists i.e. card type list, min transaction amount list and associated reward points list.
   
   Output: Updates the CSV file.
'''
def set_reward_scheme_details(card_type_list,min_trasaction_amt_list,reward_point_list):
    f=open("..\\SuppliedFiles\\SchemeDetails.csv","w")
    f.write("")
    f.close()
    for i in range(len(card_type_list)):
        f=open("..\\SuppliedFiles\\SchemeDetails.csv","a")
        f.write(str(card_type_list[i])+","+str(min_trasaction_amt_list[i])+","+str(reward_point_list[i])+'\n')
    f.close()

    