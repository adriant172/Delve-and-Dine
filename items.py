"""This contains the Items class and all of its subclasses"""
HEAL = "heal"
DEFENSE_INCREASE = "defense_buff"
DAMAGE_INCREASE = "damage_buff"

class Item:
    """Base class for all items in the game"""
    def __init__(self, name, description=None, is_equipped=False):
        self._name = name
        self.description = description
        self.is_equipped = is_equipped
    def get_name(self):
        return self._name


class Weapon(Item):
    """Base class for weapons"""
    def __init__(self, name, is_equipped, weapon_type, attack, description=None):
        super().__init__(name, description, is_equipped)
        self.weapon_type = weapon_type
        self.attack = attack

class Armor(Item):
    """Base class for """
    def __init__(self, name, is_equipped, armor_type, defense, description=None):
        super().__init__(name, description,is_equipped)
        self.armor_type = armor_type
        self.defense = defense

class Food(Item):
    def __init__(self, name, is_ingredient,buff_type=None, buff_amount=None, duration=None, description=None):
        super().__init__(name, description)
        self.buff_type = buff_type
        self.buff_amount = buff_amount
        self.duration = duration
        self.is_ingredient = is_ingredient
        self.req_ingredients = []
