"""This will contain any food items that can be added to the game"""
from items import Food, HEAL, DEFENSE_INCREASE, DAMAGE_INCREASE

salt = Food("Rock Salts",is_ingredient=True, description="Simple and common salt crystals mined from underground deposits")
boar_meat = Food("cave boar meat",is_ingredient=True, description="Raw wild cave boar meat. Not recommended to eat raw.")
roast_boar = Food("roast boar", is_ingredient=False, buff_type=HEAL, buff_amount=50, description="Roasted boar cooked to perfection.")
goblin_bread = Food("crunchy goblin bread", is_ingredient=False, buff_type=HEAL, 
                    buff_amount=5, description="""A small loaf of stale and tough bread 
                    often carried by goblins. While edible it offers minimal sustenance""")