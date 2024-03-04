import sys, time

def slow_print(line, speed):
    """This function is meant to 
    print words as if they are 
    being typed out on a screen"""
    for char in line:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print("\n")