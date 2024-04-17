from actions import apply_damage
import time
from helper_functions import slow_print

TEXT_PRINT_TIME = 0.005

def basic_combat_interaction(player, enemy):
    """Basic turn based combat loop between the player and one enemy"""
    player_turn = True
    while True:
        while player_turn:
            action = input("Would you like to attack or defend?: ")
            if action.lower().strip() == "attack":
                player.basic_attack()
                time.sleep(1)
                damage_taken = apply_damage(player,enemy)
                slow_print(f"The {enemy.get_name()} has taken {damage_taken} damage!", TEXT_PRINT_TIME)
                time.sleep(1)
            elif action.lower() == "defend":
                player.toggle_guard()
            else:
                print("You can only enter ATTACK or DEFEND")
                continue
            if enemy.get_health() <= 0:
                print(f"The {enemy.get_name()} has been defeated!")
                print("--------------------------------------------")
                return
            slow_print(f"{enemy.get_name()} has {enemy.get_health()} health remaining.", TEXT_PRINT_TIME)
            player_turn = False
        enemy.attack()
        time.sleep(1)
        damage_taken = apply_damage(enemy,player)
        slow_print(f"You have taken {damage_taken} damage!", TEXT_PRINT_TIME)
        time.sleep(1)
        if player.get_health() <= 0:
            print("You have fainted")
            print("GAME OVER")
            return
        slow_print(f"You have {player.get_health()} remaining.", TEXT_PRINT_TIME)
        player_turn = True