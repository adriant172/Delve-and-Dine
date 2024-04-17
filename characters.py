from math import floor
from random import randrange
from helper_functions import slow_print
from items import Weapon, Armor, Item, Food

class Character:
    def __init__(self, name, health, stamina, attack, defense, base_damage):
        self.__name = name
        self.__health = health
        self.__stamina = stamina
        self.__attack = attack
        self.__defense = defense
        self.__base_damage = base_damage
        self.__inventory = []
        self.__armor = None
        self.__weapon = None
        self.__defending = False

    def get_name(self):
        return self.__name

    def get_health(self):
        """Health points getter"""
        return self.__health
    def get_base_damage(self):
        """Base damage getter"""
        return self.__base_damage
    def get_attack_level(self):
        """Attack level getter"""
        return self.__attack
    def get_defense_level(self):
        """Defense level getter"""
        return self.__defense
    def take_damage(self, damage_points):
        if self.__defending:
            damage_points = damage_points - self.__defense
            damage_points = max(damage_points, 0)
        self.__health -= damage_points
        self.__defending = False
        return damage_points
    def toggle_guard(self):
        if not self. __defending:
            self.__defending = True
        else:
            self.__defending = False
    def equip(self, item):
        if isinstance(item, Weapon):
            self.__weapon = item
            self.__attack += item.attack
        elif isinstance(item, Armor):
            self.__armor = item


    

class Player(Character):
    def basic_attack(self):
        possible_actions = [" a punch"," a kick", " a dropkick", " an uppercut"]
        random_num = randrange(len(possible_actions))
        slow_print(f"You attack the enemy with {possible_actions[random_num]}", 0.02)



class Monster(Character):
    def attack(self):
        slow_print(f"The {self.get_name()} swipes at the player", 0.02)