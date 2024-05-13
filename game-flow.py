
from characters import Player, Enemy
from items import Weapon, Armor, Item, Food, HEAL, DEFENSE_INCREASE, DAMAGE_INCREASE
from combat import basic_combat_interaction
from helper_functions import slow_print, console
from time import sleep
from rich.style import Style
from rich.prompt import Prompt
from food import salt

TEXT_PRINT_TIME = 0.005

PLAYER = Player(name="Traveler",health=125,stamina=50,attack=8,defense=5, base_damage=3)
base_style = Style(color="red", blink=True, bold=True)

steel_sword = Weapon("Short Sword", False,"sword", 5, "A simple steel sword")
pork_roast = Food("pork roast",is_ingredient=False, buff_type=HEAL, buff_amount=25)
leather_armor = Armor("Weathered Leather Armor", "Medium Armor", 5, "A basic leather armor")

goblin = Enemy(name="goblin",health=50,stamina=20,attack=5,defense=1, base_damage=2)
goblin._inventory.all_items["food"][salt._name] = salt
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
    slow_print("You enter a darkly lit room, and hear rattling behind you...")
    sleep(1)
    result = basic_combat_interaction(PLAYER, goblin)
    if result is False:
        return
    slow_print("You light a torch so you can have a better look at what is inside the room?")
    action, action_index = pick(["Search the room.", "Check Inventory", "Move to another room"], "What do you do next ?", indicator="—>")



run_game()