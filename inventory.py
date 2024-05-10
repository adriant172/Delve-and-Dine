from pick import pick
import random
from items import Weapon, Armor, Item, Food, HEAL, DEFENSE_INCREASE, DAMAGE_INCREASE

class Inventory:
    def __init__(self):
        self.all_items = {
            "food": {},
            "other": {},
            "equipment": {},
        }
    def choose_item(self, item_category):
        all_category_items = []
        for item in self.all_items[item_category]:
            if item.is_equipped is True:
                continue
            all_category_items.append(item)
        selected_item, item_index = pick(all_category_items, "Items", indicator="—>")
        selected_item = self.all_items[item_category][selected_item]
        return selected_item
    def get_item(item_category, item):
        return
    def drop_item(self, item):
        if isinstance(item, Food):
            return self.all_items["food"].pop(item)
        elif isinstance(item, Weapon) or isinstance(item, Armor):
            return self.all_items["equipment"].pop(item)
        else:
            return self.all_items["other"].pop(item)
    def pick_random_item(self, category):
        item_names = list(category)
        num_of_items = len(item_names)
        picked_item = item_names[random.randrange(num_of_items)]
        return picked_item

        





