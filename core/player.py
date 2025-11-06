from random import *

class Player:
    professions = ["doctor", "fighter"]
    profession = choice(professions)

    def __init__(self, name, profession=profession, ):
        self.name = name
        self.profession = profession
        self.speed = randint(5, 10)
        self.armor_rating = randint(5, 15)
        self.hp = 50
        if self.profession == "doctor":
            self.hp += 10
        self.power = randint(5, 10)
        if self.profession == "fighter":
            self.power += 2

    def speak(self):
        print(f"\nTHE PLAYER {self.name} IS FEARLESS!\n")

    def attack(self, attacked):
        if self.roll_dice(20) + self.speed > attacked.armor_rating:
            attacking = self.roll_dice(6) + self.power
            attacked.hp -= attacking
        return attacked
            

    def roll_dice(self, max:int):
        return randint(1, max)

