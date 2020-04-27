#DSA-Assgn-4

class Player:
    def __init__(self,name,experience):
        self.__name=name
        self.__experience=int(experience)
    
    def get_name(self):
        return self.__name
    
    def get_experience(self):
        return self.__experience
    
    def __str__(self):
        return(self.__name+" "+(str)(self.__experience))



class Game :
    
    def __init__(self,players_list):
        self.__players_list = players_list
        
    
    
    def sort_players_based_on_experience(self):
        player_names = []
        player_exp = []
        for player_obj in self.__players_list :
            player_names.append(player_obj.get_name())
            player_exp.append(player_obj.get_experience())
            
        str_list = []
        
        while(1) :
            temp_max = max(player_exp)
            index_max = player_exp.index(temp_max)
            str_list.append(self.__players_list[index_max])
            player_exp.pop(index_max)
            self.__players_list.pop(index_max)
            
            if len(self.__players_list) == 0 :
                break

        self.__players_list = str_list
        return self.__players_list


    def shift_player_to_new_position(self,old_index_position , new_index_position):
    
        temp=self.__players_list.pop(old_index_position)
        self.__players_list.insert(new_index_position, temp)
    
    def display_player_details(self):
        print(self.__players_list)

    
    
player1=Player("Dhoni",15)
player2=Player("Virat",10)
player3=Player("Rohit",12)
player4=Player("Raina",11)
player5=Player("Jadeja",12)
player6=Player("Ishant",9.5)
player7=Player("Shikhar",8)
player8=Player("Axar",7.5)
player9=Player("Ashwin",6)
player10=Player("Stuart",7)
player11=Player("Bhuvneshwar",5)
#Add different values to the list and test the program
players_list=[player1,player2,player3,player4,player5,player6,player7,player8,   player9,player10,player11]

game2 = Game(players_list)
game2.sort_players_based_on_experience()
game2.shift_player_to_new_position(0, 3)
game2.display_player_details()
#Create object of Game class, invoke the methods and test your program