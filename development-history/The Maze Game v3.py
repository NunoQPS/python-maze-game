# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Nuno Santos
# The Maze Game

import random
import time
import turtle

#Window Setup
window = turtle.Screen()
window.bgcolor("Green")
window.title("The Maze Game")
window.setup(700,700)

class Pen(turtle.Turtle):
    def __init(self):
        turtle.Turtle.__init__(self)
        pen.shape("square")
        pen.speed(0)
        penup()

#Creating Rooms        
Rooms = [""]

Room1 = [
"OOOOOOOOOOOOOOOOOOOOOOOOO",
"O  OO           OOO     O",
"O  OO        OOOOOO     O",
"O  OOOOOO OOOOOO    O   O",
"O                   OOOOO",
"O  OOOOOO        OOOOOOOO",
"O  OOOOOO        OOO OOOO",
"OOOOOOOOO OOOOOO OOO  OOO",
"OOOOOOOOO OOOOOO OOO   OO",
"O  OOOOO OOOOOOOOOO    OO",
"O         OOOOOOOOOO   OO",
"O         OOOOOOOOOO   OO",
"OOOOOOO   OOOOOOOOOO   OO",
"OOOOOOO     OOOO        O",
"O           OOOO OOOOOOOO",
"O OOOOOOOO  OOOO        O",
"OOOOOOOOOO   OOOO  OO   O",
"OOOOOO OOO          OOOOO",
"O  OOO OOO  OOOOO  OOOOOO",
"O  OOO OOO  OOOOO  O    O",
"O           OOOOO  O    O",
"OOOOOOOO  OOOOOOO  O    O",
"OOOOOOOO  OOOOOOO  O    O",
"O           OOOOO       O",
"OOOOOOOOOOOOOOOOOOOOOOOOO"]



Room2 = [
"OOOOOOOOOOOOOOOOOOOOOOOOO",
"O   OOOO  OO    O    O OO",
"O S OOOO  OO OOOO OO O OO",
"O         OO    O    O  O",
"OOOO OO                 O",
"OOO  OO  OOOOOOOOOOOOOOOO",
"OOO  OO  O       OOOO   O",
"O       O  OOOO  OOOO OOO",
"O  O   O  O  OOO      OOO",
"O  O  O  O   OOO  OOOOOOO",
"O OO O  O    OOO      OOO",
"O OO  O O  OOOOO OOO O  O",
"O  O   O   OOOOO OO     O",
"O OOOOOOOO  OOO   O  OOOO",
"O  O        OOOO OO  OOOO",
"OO O OOOOOOOOOO   O OOOOO",
"O OO OOOOOOOOOOO OO OOOOO",
"O OO   OOOOO         OOOO",
"O OO OOOOOOO OOO     OOOO",
"O  O OOOOOOO OOO       OO",
"O      OOOOO OOOOOO OO OO",
"OOOOO    OOO   OOOO O   O",
"O OOOO  OOOOOO O OO O   O",
"O       OOOOF  O    O   O",
"OOOOOOOOOOOOOOOOOOOOOOOOO"
]    
    # Game Intro
Player = input("Enter username: ")
print ("\nHi", Player,", welcome to The Maze Game.")


Start = "Yes" or "yes"    #Start validation

while True:
    
    def StartRoom():
    # Game Instructions:

        print("\nGame Instructions:")
        print("\nThe rules are simple. Aim to finish with as much gold as possible.")
        print("You will enter rooms. Rooms may have either Treasure or Threat")
        print("You must clear the room before you can leave.")
        print("A Threat will require you to choose the right action.")
        print("The game is finished when you exit the Maze.")
        PlayerChoice = ""
        RoomChoice = ["1", "2", "3", "4"]
        while PlayerChoice != RoomChoice:
            PlayerChoice = str.input("Which room would you like to enter?"))
        return StartRoom

