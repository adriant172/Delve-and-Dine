from characters import Player

def main():
    player = Player(health=100,stamina=50,attack=5,defense=2)
    print("a monster swipes at the player")
    print("------------------------------")
    damage_taken = player.take_damage(5)
    print(f"The player has taken {damage_taken} damage!")
    print(f"The player has {player.get_health()} remaining.")

main()