from math import floor
from random import randrange

class Character:
    def __init__(self, name, health, stamina, attack, defense):
        self.__name = name
        self.__health = health
        self.__stamina = stamina
        self.__attack = attack
        self.__defense = defense
        inventory = []
        armor = None
        weapon = None

    def get_name(self):
        return self.__name

    def get_health(self):
        """Health points getter"""
        return self.__health
    def get_attack_level(self):
        """Attack level getter"""
        return self.__attack
    def get_defense_level(self):
        """Defense level getter"""
        return self.__defense
    def take_damage(self, damage_points):
        self.__health -= damage_points

    

class Player(Character):
    def basic_attack(self):
        possible_actions = ["punch","kick", "dropkick", "uppercut"]
        random_num = randrange(len(possible_actions))
        print(f"You attack the enemy with a {possible_actions[random_num]}")


class Monster(Character):
    def attack(self):
        print("a monster swipes at the player")