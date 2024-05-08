
from characters import Player, Monster
from items import Weapon, Armor, Item, Food, HEAL, DEFENSE_INCREASE, DAMAGE_INCREASE
from combat import basic_combat_interaction

PLAYER = Player(name="jin",health=125,stamina=50,attack=8,defense=5, base_damage=3)
    


steel_sword = Weapon("Short Sword", "sword", 5, "A simple steel sword")
pork_roast = Food("pork roast", HEAL, 25, is_ingredient=False)
leather_armor = Armor("Weathered Leather Armor", "Medium Armor", 5, "A basic leather armor")

PLAYER._inventory.all_items["food"]["pork_roast"] = pork_roast
PLAYER._inventory.all_items["equipment"][steel_sword.get_name()] = steel_sword
PLAYER._inventory.all_items["equipment"][leather_armor.get_name()] = leather_armor