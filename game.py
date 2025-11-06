from core.player import *
from core.orc import Orc
from core.goblin import Goblin



class Game:
    def start(self):
        return self.show_menu()

    def show_menu(self):
        choice = input("\nGAME MENU:\n \nENTER--> \n0 to running away \nor 1 to fight\n")
        return choice

    def create_player(self):
        player_name = input("\nCHOOS A PLAYER NAME: ")
        new_player = Player(player_name)
        return new_player

    def choose_random_monster(self):
        lottery_monster_type = randint(0, 1)
        random_monster = Orc() if lottery_monster_type else Goblin()
        return random_monster

    def battle(self, player, monster):
        player_rolling = self.roll_dice(6) + player.speed
        monster_rolling = self.roll_dice(6) + monster.speed
        counter = 1
        while player.hp and monster.hp:
            if player_rolling >= monster_rolling and counter % 2:
                player.attack(monster)
                counter += 1
            else:
                monster.attack(player)
                counter += 1
        if player.hp and not monster.hp:
            winner = player
        else:
            winner = monster 
        return winner

    def roll_dice(self, max:int):
        return randint(1, max)