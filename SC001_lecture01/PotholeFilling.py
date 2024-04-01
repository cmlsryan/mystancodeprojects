"""
File: PotholeFilling.py
Name: TODO:
--------------------------
This program shows karel filling 3
potholes. Students learn the concept of
decomposition through the process.
"""

from karel.stanfordkarel import *


def main():
    """
    TODO:
    """
    for i in range(3):
       go_in()
       put_99_beepers()
       go_out()

def go_in():
    """
    pre-condition:karel is at the upper left of the pothole, facing East.
    post-condition:karel is in the pothole, facing South.
    """
    move()
    turn_right()
    move()

def go_out():
    """
    pre-condition:karel is in the pothole, facing South.
    post-condition:karel is at the upper left of the pothole, facing East.
    """
    turn_around()
    move()
    turn_right()
    move()
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def turn_around():
    turn_left()
    turn_left()
def put_99_beepers():
    for i in range(99):
        put_beeper()





# ----- DO NOT EDIT CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
