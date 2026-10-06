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

window = turtle.Screen()
window.bgcolor("green")
window.title("The Maze Game")
window.setup(650,650)

#Creating Walls
class Wall(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("Square")
        self.color("White")
        self.penup()
        self.speed(0)
 
#Creating Player
class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("Turtle")
        self.color("Red")
        self.penup()
        self.speed(0)
        self.gold = 0 #PLayer starts with 0 Gold
    
    #Defining player movement
    def move_up(self):
        self.setheading(90) #Make turtle face North
        
        #Calculates spot player will move to
        move_x = player.xcor()
        move_y = player.ycor() + 24
        
        if (move_x, move_y) not in Walls: #If coordinates are not in Walls list:
            self.goto(move_x, move_y)     #Player can move
            
    def move_down(self):
        self.setheading(270) #Make turtle face South
        
        #Calculates spot player will move to
        move_x = player.xcor()
        move_y = player.ycor() - 24
        
        if (move_x, move_y) not in Walls: #If coordinates are not in Walls list:
            self.goto(move_x, move_y)     #Player can move
            
    def move_left(self):
        self.setheading(180) #Make turtle face West
    
        #Calculates spot player will move to
        move_x = player.xcor() - 24
        move_y = player.ycor()
        
        if (move_x, move_y) not in Walls: #If coordinates are not in Walls list:
            self.goto(move_x, move_y)     #Player can move
    
    def move_right(self):
        self.setheading(360) #Make turtle face East

        #Calculates spot player will move to
        move_x = player.xcor() +24
        move_y = player.ycor()
        
        if (move_x, move_y) not in Walls: #If coordinates are not in Walls list:
            self.goto(move_x, move_y)     #Player can move        


#Creating Coins
class Coin(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("Circle")
        self.color("Gold")
        self.penup()
        self.speed(0)
        self.gold = 10 #Coin will award user with 10 Gold
        self.goto(x, y)
        
    def Disappear(self):
        self.hideturtle()
        self.goto(1000, 1000)
        
#Creating enemies
class Threat(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("Classic")
        self.color("Blue")
        self.penup()
        self.speed(0)
        self.goto(x, y)
        
def collided(self,other):
    a = self.xcor() - self.ycor()
    b = self.ycor() - self.xcor()
    touched(a ** 2) + (b ** 2)
    
    

#Adding Treasure lists
Treasures = []

#Adding Threats lists
Threats = []

#Create rooms list
Rooms = [""]

#Define Rooms
Room_1 = [
"OOOOOOOOOOOOOOOOOOOOOOOOO",
"OP OO T        COOO    TO",
"O  OO        OOOOOO     O",
"O  OOOOOO OOOOOO    O  CO",
"O                   OOOOO",
"O  OOOOOO        OOOOOOOO",
"O  OOOOOO        OOOCOOOO",
"OOOOOOOOO OOOOOO OOO  OOO",
"OOOOOOOOO OOOOOO OOO   OO",
"OC OOOOO  OOOOOOOOO    OO",
"O         OO     OOO   OO",
"O         OO     OOO   OO",
"OOOOOOO  TOOOOOOOOOO   OO",
"OOOOOOO     OOOO       TO",
"O           OOOO OOOOOOOO",
"OCOOOOOOOO  OOOO        O",
"OOOOOOOOOO   OOOO  OO   O",
"OOOOOO OOO          OOOOO",
"OC OOO OOO  OOOOO  OOOOOO",
"O  OOO OOO  OOOOO  OT   O",
"O           OOOOO  O    O",
"OOOOOOOO  OOOOOOO  O    O",
"OOOOOOOO  OOOOOOO  O    O",
"O  C       TOOOOO       O",
"OOOOOOOOOOOOOOOOOOOOOOOOO"
]

Room_2 = [
"OOOOOOOOOOOOOOOOOOOOOOOOO",
"O   OOOO  OO    O    O OO",
"O P OOOO  OO OOOO OO O OO",
"O         OO    O    O  O",
"OOOO OO                 O",
"OOO  OO  OOOOOOOOOOOOOOOO",
"OOO  OO  O       OOOO   O",
"O       O  O OO  OOOO OOO",
"O  O   O  O  OOO      OOO",
"O  O  O  O   OOO  OOOOOOO",
"O OO O  O    OOO       OO",
"O OO  O O  OOOOO OOO O  O",
"O  O   O   OOOOO OO     O",
"O OOOOOOOO  OOO   O  OOOO",
"O  O        OOOO OO  OOOO",
"OO O OOOOOOOOOO   O OOOOO",
"O  O OOOOOOOOOOO OO OOOOO",
"O OO   O   O         OOOO",
"O OO OOO   O OOO     OOOO",
"O  O OOO   O OOO       OO",
"O      OOOOO OOOOOO OO OO",
"OOOOO    OOO   OOOO O   O",
"O OOOO  OOOOOO O OO O   O",
"O       OOOOF  O    O   O",
"OOOOOOOOOOOOOOOOOOOOOOOOO"]

#Add room to Rooms list
Rooms.append(Room_1)
Rooms.append(Room_2)

#Create room setup function
def room_setup(room):
    for y in range(len(room)):
        for x in range(len(room[y])):
            
            #Select character at X and Y coordniates
            character = room[y][x]
            
            #This will calculate the screen's X and Y coordinates
            screen_x = -288 + (x * 24)
            screen_y = 288 - (y * 24)
            
            #Checks for a wall "O"
            if character == "O":
                wall.goto(screen_x, screen_y)
                wall.stamp()
                Walls.append((screen_x, screen_y)) #Add wall coordinates to Walls list
            
            #Locates Player starting position
            if character == "P":
                player.goto(screen_x, screen_y)
            
            #Locates coins positions
            if character == "C":
                Treasures.append(Coin(screen_x, screen_y))
                
            if character == "T":
                Threats.append(Threat(screen_x, screen_y))

#Class instances
wall = Wall()
player = Player()

#Walls coordinate list
Walls = []

#Setting up room
room_setup(Rooms[1])

#Binding keyboard for player movement
turtle.listen()
turtle.onkey(player.move_up, "Up")
turtle.onkey(player.move_down, "Down")
turtle.onkey(player.move_left, "Left")
turtle.onkey(player.move_right, "Right")

#Main game loop
while True:
    window.update()