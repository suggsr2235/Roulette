import random

class RussianRoulette:
    def __init__(self) -> None:
        self.players = 0
        self.numofplay = []
        self.choicelist = []
        self.bullet = [0,0,0,1,0,0]
        
        self.start_game()
        self.play_game()
        
    # Added this function as an example of how to use a try/except clause to verify that the number of players is 6 or fewer 
    @staticmethod
    def check_players(value):
        try:
            value = int(value)
        
        except ValueError as val_error:
                print("You must enter a number")
        
        else:
            if value > 6:
                print("too many players!")
            else:
                return value
                
    def set_num_players(self):
        num_players = input("how many players: ")
        num_players = self.check_players(num_players)
    
        while not num_players:
            num_players = input("how many players: ")
            num_players = self.check_players(num_players)
            
        self.players = num_players
    
    def set_player_names(self):
        
        for number in range(1, self.players+1):
            player_name = input(f"What's Player {number}'s name: ")
            self.numofplay.append(player_name)
            self.choicelist.append(player_name)
    
    def start_game(self):
        print(
            """Random Russian Roulette: Safe edition!\n
            Each turn is random instead of one after the other, so you may go twice in a row!\n
            """
        )
        
        self.set_num_players()
        self.set_player_names()
        
    def play_game(self):
        while len(self.numofplay) > 1:
            goes1 = random.choice(self.numofplay)
            go = self.numofplay[0]
            self.numofplay.pop(0)
            self.numofplay.append(go)
                
              
            
          
            
            print((go) + " goes now!")
            self.choicelist.remove(go)
            other = random.choice(self.choicelist)
            # print(choicelist)
            choice1 = int(input("hit yourself(1) or a random player(2)"))
            if choice1 == 1:
              shoot1 == self.bullet[0]
              
              self.numofplay.pop(0)
              self.numofplay.append(shoot1)
              if shoot1 == 1:
               self.numofplay.remove(go)
               print (go + " was hit!")
                    
              else:
                print(go + " was spared!")
                self.choicelist.append(go)
                    
            elif choice1 == 2:
                print(other + " was chosen to get aimed at")
                shoot2 = self.bullet[0]
              
                self.numofplay.pop(0)
                self.numofplay.append(shoot2)
                
                if shoot2 == 1:
                    self.numofplay.remove(other)
                    print(other + " was hit!")
                    self.choicelist.append(go)
                else:
                    print(other + " was spared! now it's " + go + "'s time to go!")
                    shoot3 = self.bullet[0]
              
                    self.numofplay.pop(0)
                    self.numofplay.append(shoot3)
                    
                    if shoot3 == 1:
                        self.numofplay.remove(go)
                        print(go + " was hit!")
                        
                    else:
                        print(go + " was spared!")
                        self.choicelist.append(go)
                        
        else:
            print(*str(*self.numofplay) + " wins!")
                    
                    
game = RussianRoulette()
