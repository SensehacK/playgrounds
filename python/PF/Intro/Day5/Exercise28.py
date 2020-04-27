#PF-Exer-28
                                              
#This method accepts the name of winner of each match of the day
def find_winner_of_the_day(*match_tuple):
    #Remove pass and write the logic here
    Team1_count = 0
    Team2_count = 0
    for i in  match_tuple : 
        print(i)
        if i == "Team1" :
            Team1_count += 1 
        elif i == "Team2" :
            Team2_count += 1
        else :
            print("Different Team")
            
    if Team1_count > Team2_count :
        return "Team1"
    elif Team1_count < Team2_count :
        return "Team2"
    else :
        return "Tie"
    

#Invoke the function with each of the print statements given below
print("Winner: " , find_winner_of_the_day("Team1","Team2","Team1"))
print(find_winner_of_the_day("Team1","Team2","Team1","Team2"))