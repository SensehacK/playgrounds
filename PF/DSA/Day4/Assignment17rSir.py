#DSA-Assgn-17

def find_matches(country_name):
    new_list=[]
    for data in match_list:
        list1=data.split(':')
        if list1[0]==country_name:
            new_list.append(data)
    return new_list

def max_wins():
    dict1={}
    dict2={}
    #dict1={}
    #dict2={}
    for data in match_list:
        list1=data.split(':')
        temp=int(list1[3])
        if list1[1] not in dict1.keys():
            dict1.update({list1[1]:[list1[0]]})
            dict2.update({list1[1]:list1[3]})
            #dict1={'CHAM':['AUS],'WOR':'AUS}
            #dict2={'CHAM':2,'WOR':1}
            
        elif list1[1] in dict1.keys() and temp>=int(dict2[list1[1]]):
            
            dict1.update({list1[1]:[list1[0]]})
            dict2.update({list1[1]:list1[3]})
            #dict1={'CHAM':['AUS','IND'],'WOR':'AUS}
            #dict2={'CHAM':3,'WOR':1}
        #dict1={'CHAM':['AUS','IND','ENG'],'WOR':'AUS}
        #dict2={'CHAM':3,'WOR':1}
        
    return dict1         
def find_winner(country1,country2):
    country1_details=find_matches(country1)
    country2_details=find_matches(country2)
    count1=0
    count2=0
    for data in country1_details:
        list1=data.split(':')
        count1+=int(list1[3])
    for data in country2_details:
        list1=data.split(':')
        count2+=int(list1[3])
    if count1>count2:
        return country1
    elif count2>count1:
        return country2
    else:
        return 'Tie'
        
#Consider match_list to be a global variable
match_list=["AUS:CHAM:5:2","AUS:WOR:2:1","ENG:WOR:2:0","IND:T20:5:3","IND:WOR:2:1","PAK:WOR:2:0","PAK:T20:5:1","SA:WOR:2:0","SA:CHAM:5:1","SA:T20:5:0"]
     
#Pass different values to each function and test your program
print("The match status list details are:")
print(match_list)
print()