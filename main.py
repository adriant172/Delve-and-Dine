from characters import Player, Monster
from items import Weapon, Armor, Item, Food, HEAL, DEFENSE_INCREASE, DAMAGE_INCREASE
from combat import basic_combat_interaction



def main():
    player = Player(name="jin",health=200,stamina=50,attack=8,defense=2, base_damage=3)
    goblin = Monster(name="goblin",health=50,stamina=20,attack=2,defense=1, base_damage=2)

    steel_sword = Weapon("steel_sword", "sword", 5, "A simple steel sword")
    pork_roast = Food("pork roast", HEAL, 25, is_ingredient=False)
    
    player.equip(steel_sword)
    player._inventory.all_items["food"]["pork_roast"] = pork_roast

    basic_combat_interaction(player, goblin)


main()
