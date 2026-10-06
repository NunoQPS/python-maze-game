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
            print (str.input("Which room would you like to enter?"))
        return StartRoom

