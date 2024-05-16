"""This is the primary module that contains the game flow and effectively how the game runs"""
from time import sleep
from rich.style import Style
from rich.prompt import Prompt
from pick import pick
from characters import Player, Enemy
from items import Weapon, Armor, Item, Food, HEAL, DEFENSE_INCREASE, DAMAGE_INCREASE
from combat import basic_combat_interaction
from helper_functions import slow_print, console
from food import salt, boar_meat, goblin_bread


### Initiate current games items and characters
TEXT_PRINT_TIME = 0.010

player = Player(name="Traveler",health=100,stamina=50,attack=8,defense=5, base_damage=3)
base_style = Style(color="red", blink=True, bold=True)
narration_style = Style(color="cyan", italic=True)

steel_sword = Weapon("Short Sword", False,"sword", 5, "A simple steel sword")
pork_roast = Food("pork roast",is_ingredient=False, buff_type=HEAL, buff_amount=25)
leather_armor = Armor("Weathered Leather Armor", False, "Medium Armor", 5, "A basic leather armor")

goblin = Enemy(name="goblin",health=50,stamina=20,attack=4,defense=1, base_damage=3)
cave_boar = Enemy(name="Boar", health=40, stamina=10, attack=3, defense=1, base_damage=2)
slime = Enemy(name="Slime", health=25, stamina=10, attack=3, defense=2, base_damage= 1)
goblin.inventory.all_items["food"][goblin_bread.get_name()] = goblin_bread
cave_boar.inventory.all_items["food"][boar_meat.get_name()] = boar_meat
player.inventory.insert_item(steel_sword)



### Define Helper Functions
def room_actions(room_search_text,loot):
    """This functions takes a string to be used when the room
      is searched and item object that will be found as loot"""
    room_searched = False
    while True:
        action, action_index = pick(["Search the room", "Check Inventory", "Move to next room"], "What do you do next ?", indicator="—>")
        if action == "Search the room":
            if room_searched:
                slow_print("Room is already been searched")
                sleep(1)
                continue
            room_searched = True
            slow_print(room_search_text)
            player.inventory.insert_item(loot)
            slow_print(f" You have found {loot.get_name()}")
            sleep(1)
            print("Press enter to continue...")
            input()
            if isinstance(loot,(Weapon, Armor)):
                answer = Prompt.ask("Would you like to equip this item now? ", choices=["Yes", "No"], default="Yes")
                if answer == "Yes":
                    if player.get_armor():
                        player.unequip(player.get_armor())
                    player.equip(leather_armor)
        elif action == "Check Inventory":
            while True:
                category = player.inventory.choose_category()
                if category is None:
                    break
                if category == "food":
                    if len(player.inventory.all_items["food"]) == 0:
                        slow_print("Your bag is empty..")
                        continue
                    item = player.inventory.choose_item(category)
                    if item is None:
                        continue
                    player.eat_food(item)
                elif category == "equipment":
                    if len(player.inventory.all_items["equipment"]) == 0:
                        slow_print("No items to equip")
                        continue
                    item = player.inventory.choose_item(category)
                    if item is None:
                        continue
                    if item.is_equipped is True:
                        item.is_equipped = False
                        player.unequip(item)
                    else:
                        item.is_equipped = True
                        player.equip(item)
        elif action == "Move to next room":
            break


def main(player):
    """ This is the main function that contains the games flow"""
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
    player.set_name(name)
    slow_print(f"All right, {name} Enter at your own risk!")
    sleep(1)
    slow_print("You slowly descend down a spiral staircase, once you reach the bottom you come across two paths. Which do you take?", style=narration_style)
    current_direction = Prompt.ask("Which way ? ", choices=["left", "right"], default="left")
    slow_print(f"You decide to take the {current_direction} path", style=narration_style)
    slow_print("You enter a darkly lit room, and hear squeals and footsteps speeding towards you...", style=narration_style)
    sleep(1)
    player = basic_combat_interaction(player, cave_boar)
    if player.get_health() <= 0:
        return
    slow_print("You light a torch so you can have a better look at what is inside the room?")
    sleep(1)
    print("Press enter to continue...")
    input()
    room_actions("As you search the room you find something tucked under a pile of bones", leather_armor)
    slow_print("You decide to move forward...You squeeze through a tight corridor into the next room", style=narration_style)
    slow_print("You find what appears to be old dungeon cells, and you murmuring and grunts coming from one of the cells.", style=narration_style)
    slow_print("Looks like you stumbled upon something trying to loot this place as well..", style=narration_style)
    print("Press enter to continue...")
    input()
    result = basic_combat_interaction(player, goblin)
    if result is False:
        return
    slow_print("With the area clear you decide to...")
    sleep(1)
    input()
    room_actions("You rummage through each cell to find something worthwhile. Alas your diligence was rewarded", salt)
    slow_print("As you make your way forward, it appears you found a shortcut to the surface", style=narration_style)
    slow_print("Since this your first time entering this place it is probably best to part and stock up on supplies", style=narration_style)

main(player)
