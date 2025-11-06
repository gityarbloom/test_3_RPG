from random import *
class Orc:
    def __init__(self):
        weapons = ["Knife", "Sword", "Axe"]
        self.name = "orc_monster"
        self.hp = 50
        self.type = "orc"
        self.speed = randint(0, 5)
        self.power = randint(5, 10)
        self.armor_rating = randint(2, 8)
        self.weapon = choice(weapons)

    def speak(self):
        print(f"\nTHE {self.type}: {self.name} IS ANGRY!\n")

    def roll_dice(self, max:int):
        return randint(1, max)

    def attack(self, attacked):
        if self.weapon == "Knife":
            damage_power = 0.5
        elif self.weapon == "Sword":
            damage_power = 1
        else:
            damage_power = 1.5
        if self.roll_dice(20) + self.speed > attacked.armor_rating:
            attacking = (self.roll_dice(6) + self.power) * damage_power
            attacked.hp -= attacking
        return attacked

