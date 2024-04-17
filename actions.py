from random import randrange


def apply_damage(attacker,defender):
    """This is to apply damage to the players health"""
    base_damage = attacker.get_base_damage()
    attack_level = attacker.get_attack_level()
    defense_level = defender.get_defense_level()
    actual_attack = randrange(base_damage, base_damage + attack_level)
    if attack_level >= defense_level:
        damage_taken = actual_attack * 2 - defense_level
    else:
        damage_taken = actual_attack * actual_attack / defense_level
    return defender.take_damage(damage_taken)

