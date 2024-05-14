from pick import pick
import random
from items import Weapon, Armor, Item, Food, HEAL, DEFENSE_INCREASE, DAMAGE_INCREASE
from rich.style import Style

class Inventory:
    def __init__(self):
        self.all_items = {
            "food": {},
            "other": {},
            "equipment": {},
        }
    def choose_category(self):
        all_categories = []
        for category in self.all_items:
            all_categories.append(category)
        all_categories.append("EXIT")
        selected_item, item_index = pick(all_categories, "Inventory", indicator="—>")
        
        if selected_item == "EXIT":
            return None
        return selected_item
    def choose_item(self, item_category):
        """Used to select equippable items , such as weapons and armor""" 
        all_category_items = []
        for item in self.all_items[item_category]:
            if item_category != "food" and self.all_items[item_category][item].is_equipped is True:
                item = f"{item} - [Equipped]"
            all_category_items.append(item)
        all_category_items.append("Go Back")
        selected_item, item_index = pick(all_category_items, "Items", indicator="—>")
        if selected_item == "Go Back":
            return None
        selected_item = self.all_items[item_category][selected_item.replace(" - [Equipped]", "")]
        return selected_item
    def insert_item(self, item):
        if isinstance(item, Food):
            self.all_items["food"][item._name] = item
        elif isinstance(item, Weapon) or isinstance(item, Armor):
            self.all_items["equipment"][item._name] = item
        else:
            self.all_items["other"][item._name] = item
        return
    def remove_item(self, item):
        if isinstance(self.all_items["food"][item], Food):
            return self.all_items["food"].pop(item)
        if isinstance(self.all_items["equipment"][item], (Weapon, Armor)):
            return self.all_items["equipment"].pop(item)
        return self.all_items["other"].pop(item)
    def pick_random_item(self, category):
        item_names = list(self.all_items[category])
        num_of_items = len(item_names)
        picked_item = item_names[random.randrange(num_of_items)]
        return picked_item

        





