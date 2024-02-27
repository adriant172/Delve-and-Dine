def apply_damage(attacker,defender):
    """This is to apply damage to the players health"""
    attack_level = attacker.get_attack_level()
    defense_level = defender.get_defense_level()
    if attack_level >= defense_level:
        damage_taken = attack_level * 2 - defense_level
    else:
        damage_taken = attack_level * attack_level / defense_level
    defender.take_damage(damage_taken)
    return damage_taken
