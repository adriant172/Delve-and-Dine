import time
from rich.console import Console
from rich.theme import Theme
from pick import pick

console = Console()
# import sys, time

# def slow_print(line, speed):
#     """This function is meant to 
#     print words as if they are 
#     being typed out on a screen"""
#     for char in line:
#         sys.stdout.write(char)
#         sys.stdout.flush()
#         time.sleep(speed)
#     print("\n")



def slow_print(text, delay=0.010, style=None):
    for character in text:
        console.print(character, end='', style=style)
        time.sleep(delay)
    console.print()  # for newline