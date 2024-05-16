import time
from rich.console import Console

console = Console()
# import sys, time

def slow_print(text, delay=0.010, style=None):
    """Custom print function that takes delay time and style string as parameters"""
    for character in text:
        console.print(character, end='', style=style)
        time.sleep(delay)
    console.print()  # for newline