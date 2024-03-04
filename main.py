from characters import Player, Monster
from actions import apply_damage
import time
from helper_functions import slow_print

def main():
    player = Player(name="jin",health=200,stamina=50,attack=5,defense=2, base_damage=3)
    goblin = Monster(name="goblin",health=75,stamina=20,attack=2,defense=1, base_damage=2)
    player_turn = True
    
    while True:
        while player_turn:
            action = input("Would you like to attack or defend?: ")
            if action.lower().strip() == "attack":
                player.basic_attack()
                time.sleep(1)
                damage_taken = apply_damage(player,goblin)
                slow_print(f"The {goblin.get_name()} has taken {damage_taken} damage!", 0.015)
                time.sleep(1)
            else:
                print("You can only enter ATTACK or DEFEND")
                continue
            if goblin.get_health() <= 0:
                print(f"The {goblin.get_name()} has been defeated!")
                print("--------------------------------------------")
                return
            slow_print(f"{goblin.get_name()} has {goblin.get_health()} health remaining.", 0.015)
            player_turn = False
        goblin.attack()
        time.sleep(1)
        damage_taken = apply_damage(goblin,player)
        slow_print(f"The player has taken {damage_taken} damage!", 0.015)
        time.sleep(1)
        if player.get_health() <= 0:
            print("You have been fainted")
            print("GAME OVER")
            return
        slow_print(f"The player has {player.get_health()} remaining.", 0.015)
        player_turn = True
        
        
        
    print("------------------------------")
    damage_taken = player.take_damage(8)
    print(f"The player has taken {damage_taken} damage!")
    print(f"The player has {player.get_health()} remaining.")

main()