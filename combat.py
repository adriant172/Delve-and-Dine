from actions import apply_damage
import time
from helper_functions import slow_print
from rich.prompt import Prompt
from pick import pick
# from actions_textual import ActionsList


TEXT_PRINT_TIME = 0.005
combat_options_title = "What would you like to do ?"
combat_options = ["Attack", "Defend", "Eat Food", "Equip"]

def basic_combat_interaction(player, enemy):
    """Basic turn based combat loop between the player and one enemy"""
    player_turn = True
    while True:
        while player_turn:
            time.sleep(1)
            action, action_index = pick(combat_options, combat_options_title, indicator="=>")
            # action = Prompt.ask(combat_options_title, choices=combat_options, default="Attack")        
            if action.lower().strip() == "attack":
                player.basic_attack()
                time.sleep(1)
                damage_taken = apply_damage(player,enemy)
                slow_print(f"The {enemy.get_name()} has taken {damage_taken} damage!", TEXT_PRINT_TIME)
                time.sleep(1)
            elif action.lower() == "defend":
                player.toggle_guard()
            elif action.lower() == "eat food":
                selected_item = player._inventory.choose_item("food")
                player.eat_food(selected_item)
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