class Item:
    """Base class for all items in the game"""
    def __init__(self, name, description=None):
        self.__name = name
        self.description = description
    def get_name(self):
        return self.__name


class Weapon(Item):
    """Base class for weapons"""
    def __init__(self, name, weapon_type, attack, description=None):
        super().__init__(name, description)
        self.weapon_type = weapon_type
        self.attack = attack

class Armor(Item):
    """Base class for """
    def __init__(self, name, armor_type, defense, description=None):
        super().__init__(name, description)
        self.armor_type = armor_type
        self.defense = defense

class Food(Item):
    def __init__(self, name, buff_type, buff_amount, duration, is_ingredient, description=None):
        super().__init__(name, description)
        self.buff_type = buff_type
        self.buff_amount = buff_amount
        self.duration = duration
        self.is_ingredient = is_ingredient

