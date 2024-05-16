"""Main module that starts the game"""
from game_flow import run_game



def main():
    """Main function that starts the game"""
    player = Player(name="Traveler",health=100,stamina=50,attack=8,defense=5, base_damage=3)
    run_game(player)


main()
