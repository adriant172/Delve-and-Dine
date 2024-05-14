
from characters import Player, Enemy
from items import Weapon, Armor, Item, Food, HEAL, DEFENSE_INCREASE, DAMAGE_INCREASE
from combat import basic_combat_interaction
from helper_functions import slow_print, console
from time import sleep
from rich.style import Style
from rich.prompt import Prompt
from food import salt, boar_meat, roast_boar
from pick import pick

TEXT_PRINT_TIME = 0.010

PLAYER = Player(name="Traveler",health=100,stamina=50,attack=8,defense=5, base_damage=3)
base_style = Style(color="red", blink=True, bold=True)

steel_sword = Weapon("Short Sword", False,"sword", 5, "A simple steel sword")
pork_roast = Food("pork roast",is_ingredient=False, buff_type=HEAL, buff_amount=25)
leather_armor = Armor("Weathered Leather Armor", False, "Medium Armor", 5, "A basic leather armor")

goblin = Enemy(name="goblin",health=50,stamina=20,attack=4,defense=1, base_damage=3)
cave_boar = Enemy(name="Boar", health=40, stamina=10, attack=3, defense=1, base_damage=2)
goblin._inventory.all_items["food"][salt._name] = salt
cave_boar._inventory.all_items["food"][boar_meat._name] = boar_meat
PLAYER._inventory.all_items["equipment"][steel_sword.get_name()] = steel_sword


def run_game():
    console.print("DELVE & DINE", style=base_style, justify="center")
    sleep(1)
    slow_print(" Welcome traveler, since you are here I assume you are in search of adventure?")
    sleep(1)
    slow_print("Or perhaps maybe just hungry?")
    sleep(1)
    slow_print("Well whatever the reason, just try to make it out in one piece.")
    sleep(1)
    slow_print("Oh I almost forgot, what are you called traveler ?")
    sleep(1)
    name = Prompt.ask("Enter your name:", default="Traveler")
    PLAYER._name = name
    slow_print(f"All right, {name} Enter at your own risk!")
    sleep(1)
    slow_print("You slowly descend down a spiral staircase, once you reach the bottom you come across two paths. Which do you take?", style="italic cyan")
    current_direction = Prompt.ask("Which way ? ", choices=["left", "right"], default="left")
    slow_print(f"You decide to take the {current_direction} path", style="italic cyan")
    slow_print("You enter a darkly lit room, and hear squeals and footsteps speeding towards you...", style="italic cyan")
    sleep(1)
    result = basic_combat_interaction(PLAYER, cave_boar)
    if result is False:
        return
    slow_print("You light a torch so you can have a better look at what is inside the room?")
    sleep(1)
    print("Press enter to continue...")
    input()
    room_searched = False
    while True:
        action, action_index = pick(["Search the room", "Check Inventory", "Move to next room"], "What do you do next ?", indicator="—>")
        if action == "Search the room":
            if room_searched:
                slow_print("Room is already been searched")
                continue
            slow_print("As you search the room you find something tucked under a pile of bones")
            PLAYER._inventory.insert_item(leather_armor)
            slow_print(f" You have found {leather_armor._name}")
            answer = Prompt.ask("Would you like to equip this item now? ", choices=["Yes", "No"], default="Yes")
            if answer == "Yes":
                if PLAYER._armor:
                    PLAYER.unequip(PLAYER._armor)
                PLAYER.equip(leather_armor)

            
        elif action == "Check Inventory":
            while True:
                category = PLAYER._inventory.choose_category()
                if category is None:
                    break
                if category == "food":
                    if len(PLAYER._inventory.all_items["food"]) == 0:
                        slow_print("Your bag is empty..")
                        continue
                    item = PLAYER._inventory.choose_item(category)
                    if item is None:
                        continue
                    PLAYER.eat_food(item)
                elif category == "equipment":
                    if len(PLAYER._inventory.all_items["equipment"]) == 0:
                        slow_print("No items to equip")
                        continue
                    item = PLAYER._inventory.choose_item(category)
                    if item is None:
                        continue
                    if item.is_equipped == True:
                        item.is_equipped = False
                        PLAYER.unequip(item)
                    else:
                        item.is_equipped = True
                        PLAYER.equip(item)
        elif action == "Move to next room":
            break
    slow_print("You decide to move forward...You squeeze through a tight corridor into the next room", style="italic cyan")
    slow_print("You find what appears to be old dungeon cells, and you murmuring and grunts coming from one of the cells.")
    slow_print("Looks like you stumbled upon something trying to loot this place as well..")
    result = basic_combat_interaction(PLAYER, goblin)
    if result is False:
        return



                    
                    

            
    
    
        



run_game()