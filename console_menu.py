"""Contains console menu functions 
that provide a simple menu interface for 
displaying static information"""
from consolemenu import ConsoleMenu


def show_stats_menu(stats):
    """Receives stats object as a parameter and displays basic user stats"""
    menu = ConsoleMenu("Stats",prologue_text=f"""HP: {stats['current_health']}/{stats['max_health']} 
                       \nATK: {stats['attack']} \nDEF: {stats['defense']}""",exit_menu_char="q")
    menu.show()