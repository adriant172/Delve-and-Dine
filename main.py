from characters import Player, Monster
from items import Weapon, Armor, Item, Food
from combat import basic_combat_interaction

def main():
    player = Player(name="jin",health=200,stamina=50,attack=8,defense=2, base_damage=3)
    goblin = Monster(name="goblin",health=50,stamina=20,attack=2,defense=1, base_damage=2)

    steel_sword = Weapon("steel_sword", "sword", 5, "A simple steel sword")
    player.equip(steel_sword)
    
    basic_combat_interaction(player, goblin)



main()
