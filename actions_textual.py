from typing import Coroutine
from textual.app import App, ComposeResult
from textual.events import Event, Key
from textual.widgets import Footer, Header, OptionList, Log
from textual.containers import Container
from textual.screen import Screen
import sys
from characters import Player, Monster
from items import Weapon, Armor, Item, Food
from combat import basic_combat_interaction_textual



class ActionsList(Screen):
    def compose(self) -> ComposeResult:
        yield Container(
            OptionList("Attack", "Defend"),
            id="actions"
        )
    def on_option_list_option_selected(self, message: OptionList.OptionSelected):
        value = message.option.prompt
        self.dismiss(result=value)

class MainApp(App):
    CSS_PATH = "styles/actions_list.tcss"
    TITLE = "Delve and Dine"

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
    
    async def on_compose(self):
            await self.mount(Log())
            self.start_game()


    def add_text(self, text):
        """ This will add a single line of text to the app """
        self.query_one(Log).write_line(text)
    
    def request_actions_list(self):
        """ This function prompts the user with the actions list screen"""
        # result = await self.push_screen(ActionsList())                              
        def check_action(action: str):
            if action:
                return action
        self.push_screen(ActionsList(), check_action)

    def start_game(self):

        player = Player(name="jin",health=200,stamina=50,attack=8,defense=2, base_damage=3)
        goblin = Monster(name="goblin",health=50,stamina=20,attack=2,defense=1, base_damage=2)
        steel_sword = Weapon("steel_sword", "sword", 5, "A simple steel sword")
        equipped_text = player.equip(steel_sword, app=self)
        self.add_text(equipped_text)
        basic_combat_interaction_textual(player, goblin, app=self)

 
if __name__ == "__main__":
    app = MainApp()
    app.run()
