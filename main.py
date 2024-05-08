from characters import Player, Monster
from items import Weapon, Armor, Item, Food, HEAL, DEFENSE_INCREASE, DAMAGE_INCREASE
from combat import basic_combat_interaction


steel_sword = Weapon("Short Sword", "sword", 5, "A simple steel sword")
pork_roast = Food("pork roast", HEAL, 25, is_ingredient=False)
leather_armor = Armor("Weathered Leather Armor", "Medium Armor", 5, "A basic leather armor")


def main():
    player = Player(name="jin",health=125,stamina=50,attack=8,defense=5, base_damage=3)
    goblin = Monster(name="goblin",health=50,stamina=20,attack=5,defense=1, base_damage=2)

    
    player._inventory.all_items["food"]["pork_roast"] = pork_roast
    player._inventory.all_items["equipment"][steel_sword.get_name()] = steel_sword
    player._inventory.all_items["equipment"][leather_armor.get_name()] = leather_armor

    basic_combat_interaction(player, goblin)


main()
