""" Contains the classes for player and NPC types"""
from random import randrange
from items import Weapon, Armor, HEAL, DEFENSE_INCREASE, DAMAGE_INCREASE
from helper_functions import slow_print
from inventory import Inventory

class Character:
    """Base class for all character types"""
    def __init__(self, name, health, stamina, attack, defense, base_damage):
        self._name = name
        self._health = health
        self._max_health = health
        self._stamina = stamina
        self._attack = attack
        self._defense = defense
        self._base_damage = base_damage
        self.inventory = Inventory()
        self._armor = None
        self._weapon = None
        self._defending = False

    def set_name(self, name):
        """character name setter"""
        self._name = name
    def get_name(self):
        """character name getter"""
        return self._name
    def get_max_health(self):
        """max health points getter"""
        return self._max_health
    def get_health(self):
        """Health points getter"""
        return self._health
    def get_stamina(self):
        """Stamina points getter"""
        return self._stamina
    def get_base_damage(self):
        """Base damage getter"""
        return self._base_damage
    def get_attack_level(self):
        """Attack level getter"""
        return self._attack
    def get_defense_level(self):
        """Defense level getter"""
        return self._defense
    def get_armor(self):
        """Currently equipped armor item getter"""
        return self._armor
    def get_weapon(self):
        """Currently equipped weapon item getter"""
        return self._weapon
    def get_basic_stats(self):
        """Returns an object containing all relevant stats"""
        return {
            "current_health": self._health,
            "max_health": self._max_health,
            "stamina": self._stamina,
            "attack": self._attack,
            "defense": self._defense
        }
    def take_damage(self, damage_points):
        """Apply damage to the current character 
        based on damage points parameter"""
        if self._defending:
            damage_points = damage_points - self._defense
            damage_points = max(damage_points, 0)
        self._health -= damage_points
        self._defending = False
        return damage_points
    def toggle_guard(self):
        """Toggles the guard action"""
        if not self._defending:
            self._defending = True
        else:
            self._defending = False
    def equip(self, item):
        """Takes an equipment item as a parameter and equips said item"""
        if isinstance(item, Weapon):
            self._weapon = item
            self._attack += item.attack
        elif isinstance(item, Armor):
            self._armor = item
            self._defense += item.defense
        slow_print(f"You have equipped {item.get_name()}", 0.02)
    def unequip(self, item):
        """Takes an equipment item as a parameter and unequip said item"""
        if isinstance(item, Weapon):
            self._weapon = None
            self._attack -= item.attack    
        elif isinstance(item, Armor):
            self._armor = None
            self._defense -= item.defense
        slow_print(f"You have unequipped {item.get_name()}", 0.02)
    def eat_food(self, food):
        """Takes a food item as a parameter and consumes it"""
        if food.buff_type == HEAL:
            new_health = self._health + food.buff_amount
            if new_health > self._max_health:
                self._health = self._max_health
            else:
                self._health += food.buff_amount
            slow_print(f"You ate {food._name}. Gained {food.buff_amount} hp.", 0.02)
            slow_print(f"Current HP at {self._health}", 0.02)
        elif food.buff_type == DEFENSE_INCREASE:
            self._defense += food.buff_amount
        elif food.buff_type == DAMAGE_INCREASE:
            self._attack += food.buff_amount

class Player(Character):
    """The players sub-class meant for the current player of the game"""
    def __init__(self, name, health, stamina, attack, defense, base_damage):
        super().__init__(name, health, stamina, attack, defense, base_damage)
    def basic_attack(self):
        """basic attack text"""
        if self._weapon:
            name = self._weapon.get_name()
            slow_print(f"You attack with {name}", 0.02)
            
        else:
            possible_actions = [" a punch"," a kick", " a dropkick", " an uppercut"]
            random_num = randrange(len(possible_actions))
            slow_print(f"You attack with {possible_actions[random_num]}", 0.02)


class Enemy(Character):
    """ Subclass for all basic monsters or enemies in game"""
    def attack(self):
        """Enemy attack text"""
        slow_print(f"The {self.get_name()} attacks the player", 0.02)