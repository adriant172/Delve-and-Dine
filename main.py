from characters import Player, Monster
from actions import apply_damage

def main():
    player = Player(name="jin",health=200,stamina=50,attack=5,defense=2)
    goblin = Monster(name="goblin",health=75,stamina=20,attack=2,defense=1)
    player_turn = True
    
    while True:
        while player_turn:
            action = input("Would you like to attack or defend?")
            if action.lower() == "attack":
                player.basic_attack()
                damage_taken = apply_damage(player,goblin)
                print(f"The {goblin.get_name()} has taken {damage_taken} damage!")
            else:
                print("You can only enter ATTACK or DEFEND")
                if goblin.get_health() <= 0:
                    print(f"The {goblin.get_name()} has been defeated!")
                    print("--------------------------------------------")
                    return
                print(f"{goblin.get_name()} has {goblin.get_health()} remaining.")     
            player_turn = False
        goblin.attack()
        damage_taken = apply_damage(goblin,player)
        print(f"The player has taken {damage_taken} damage!")
        if player.get_health() <= 0:
            print("You have been fainted")
            print("GAME OVER")
            return
        print(f"The player has {player.get_health()} remaining.")
        player_turn = True
        
        
        
    print("------------------------------")
    damage_taken = player.take_damage(8)
    print(f"The player has taken {damage_taken} damage!")
    print(f"The player has {player.get_health()} remaining.")

main()