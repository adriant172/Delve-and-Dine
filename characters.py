
class Player:
    def __init__(self, health, stamina, attack, defense):
        self.__health = health
        self.__stamina = stamina
        self.__attack = attack
        self.__defense = defense
        inventory = []
        armor = None
        weapon = None

    def get_health(self):
        """Health points getter"""
        return self.__health
    
    def take_damage(self, damage):
        """This is to apply damage to the players health"""
        defense_modifier = 0.01 * self.__defense
        defense_buffer = defense_modifier * self.__health
        damage_taken = damage - defense_buffer
        self.__health -= damage_taken
        return damage_taken
