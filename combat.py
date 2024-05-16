"""This contains all functions that relate to the core combat loop"""
import time
from pick import pick
from actions import apply_damage
from helper_functions import slow_print
from console_menu import show_stats_menu


TEXT_PRINT_TIME = 0.010
combat_options_title = "What would you like to do ?"
combat_options = ["Attack", "Defend", "Eat Food", "Equip", "Stats"]

def basic_combat_interaction(player, enemy):
    """Basic turn based combat loop between the player and one enemy"""
    slow_print(f"A {enemy.get_name()} has appeared", TEXT_PRINT_TIME)
    time.sleep(1)
    player_turn = True
    while True:
        while player_turn:
            time.sleep(1)
            action, action_index = pick(combat_options, combat_options_title, indicator="—>")
            if action.lower().strip() == "attack":
                player.basic_attack()
                time.sleep(1)
                damage_taken = apply_damage(player,enemy)
                slow_print(f"The {enemy.get_name()} has taken {damage_taken} damage!", TEXT_PRINT_TIME)
                time.sleep(1)
            elif action.lower() == "defend":
                player.toggle_guard()
            elif action.lower() == "eat food":
                if len(player.inventory.all_items["food"]) == 0:
                    slow_print("Your bag is empty..")
                    continue
                selected_item = player.inventory.choose_item("food")
                player.eat_food(selected_item)
            elif action.lower() == "equip":
                if len(player.inventory.all_items["equipment"]) == 0:
                    slow_print("No items to equip")
                    continue
                selected_item = player.inventory.choose_item("equipment")
                if selected_item is None:
                    continue
                if selected_item.is_equipped is True:
                    selected_item.is_equipped = False
                    player.unequip(selected_item)
                else:
                    selected_item.is_equipped = True
                    player.equip(selected_item)
            elif action.lower() == "stats":
                stats = player.get_basic_stats()
                show_stats_menu(stats)
                continue
            if enemy.get_health() <= 0:
                print(f"The {enemy.get_name()} has been defeated!")
                random_item = enemy.inventory.pick_random_item("food")
                loot = enemy.inventory.remove_item(random_item)
                player.inventory.insert_item(loot)
                slow_print(f" You have found {loot.get_name()}")
                return player
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
            return False
        slow_print(f"You have {player.get_health()} remaining.", TEXT_PRINT_TIME)
        player_turn = True