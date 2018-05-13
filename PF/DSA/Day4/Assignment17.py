#DSA-Assgn-17

def find_matches(country_name):
    country = []
    for match in match_list :
        country_match = match[0:3]
        if country_match in country_name :
            country.append(match)
        
    
    return country

def max_wins():
    #Remove pass and write your logic here
    pass
             
def find_winner(country1,country2):
    count1 = 0
    count2 = 0
    country1_list = find_matches(country1)
    country2_list = find_matches(country2)
    
    for match in match_list :
        country_match = match[0]
    
    
    
    if count1 > count2 :
        return country1
    elif count2 >count1 :
        return country2
    else :
        return "Tie"
#Consider match_list to be a global variable
match_list=["AUS:CHAM:5:2","AUS:WOR:2:1","ENG:WOR:2:0","IND:T20:5:3","IND:WOR:2:1","PAK:WOR:2:0","PAK:T20:5:1","SA:WOR:2:0","SA:CHAM:5:1","SA:T20:5:0"]
     
#Pass different values to each function and test your program
print("The match status list details are:")
print(match_list)
print()
find_matches("AUS")