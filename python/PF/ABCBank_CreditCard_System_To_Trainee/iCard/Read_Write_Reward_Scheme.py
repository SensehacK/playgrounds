import csv
'''This function fetches the details of all reward schemes from SchemeDetails CSV file 
   in 3 lists and returns them as tuple of lists.
   
   Input: Path of CSV file.
   
   Output: A dictionary which contains card type(string) as key, minimum transaction amount(string) and 
   reward points(string) as values in form of a list.
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
    return create_dict_from_lists (card_type_list,min_trasaction_amt_list,reward_point_list)

'''
   This function should create a dictionary from lists passed as input parameters.
   
   Input: 3 lists i.e. card type list, min transaction amount list and  associated reward points list.
   
   Output: A dictionary which contains card type(string) as key, minimum transaction amount(string) and 
   reward points(string) as values in form of a list.
'''
def create_dict_from_lists(card_type_list,min_trasaction_amt_list,reward_point_list):
    dict_list = {}
    for i in range(0 , len(min_trasaction_amt_list)) :
        dict_values = []
        dict_values.append(min_trasaction_amt_list[i])
        dict_values.append(reward_point_list[i])
        dict_list.update({card_type_list[i]:dict_values})
    return dict_list

'''This function updates the details of reward schemes in SchemeDetails CSV file. 
   
   Input: A tuple of lists i.e. card type list, min transaction amount list and associated reward points list.
   
   Output: A dictionary which contains card type(string) as key, minimum transaction amount(string) and 
   reward points(string) as values in form of a list.
'''

def set_reward_scheme_details(card_reward_details_dict):
    f=open("..\\SuppliedFiles\\SchemeDetails.csv","w")
    f.write("")
    f.close()
    for k,v in card_reward_details_dict.items():
        f=open("..\\SuppliedFiles\\SchemeDetails.csv","a")
        f.write(str(k)+","+str(v[0])+","+str(v[1])+'\n')
    f.close()