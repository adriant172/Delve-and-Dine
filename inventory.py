from pick import pick

class Inventory:
    def __init__(self):
        self.all_items = {
            "food": {},
            "other": {},
            "weapons": {},
            "armor":{}
        }
    def choose_item(self, item_category):
        all_category_items = []
        for name in self.all_items[item_category]:
            all_category_items.append(name)
        selected_item, item_index = pick(all_category_items, "Items", indicator="=>")
        selected_item = self.all_items[item_category][selected_item]
        return selected_item



