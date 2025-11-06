from game import *

if __name__ == "__main__":
    new_game = Game()
    play_now = new_game.start()
    if play_now:
        player = new_game.create_player()
        monster = new_game.choose_random_monster()
        print(f"{new_game.battle(player, monster)}")