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
import math

#Registering shapes
turtle.register_shape("Coin.gif")
turtle.register_shape("Wall.gif")
turtle.register_shape("Portal.gif")
turtle.register_shape("Threat.gif")

#Making screen
window = turtle.Screen()
window.bgcolor("Green")
window.update()
window.title("The Maze Game")
window.setup(650,650)
window.tracer(0) #User does not see screen load

#Creating Walls
class Wall(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("Wall.gif")
        self.color("white")
        self.penup()
        self.speed(0)
 
#Creating Player
class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("turtle")
        self.color("red")
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

    def collided(self, other):
        a = self.xcor() - other.xcor()
        b = self.ycor() - other.ycor()
        distance = math.sqrt((a ** 2) + (b ** 2))
        if distance < 3:
            return True
        else:
            return False

#Creating Coins
class Coin(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("Coin.gif")
        self.penup()
        self.speed(0)
        self.gold = 10 #Coin will award user with 10 Gold
        self.goto(x, y)
   
    #Defining a 'disappear from the map' instance     
    def Disappear(self):
        self.goto(1000, 1000)
        self.hideturtle()
        
#Creating threats
class Threat(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("Threat.gif")
        self.penup()
        self.speed(0)
        self.goto(x, y)
        self.direction = random.choice(["up", "down", "left", "right"])
    
    #Defining threat Movement    
    def threat_movement(self):
        if self.direction == "up":
            dx = 0
            dy= 24
        elif self.direction == "down":
            dx = 0
            dy =  - 24
        elif self.direction == "left":
            dx = - 24
            dy = 0
        elif self.direction == "right":
            dx = 24
            dy = 0
        else:
            dx = 0
            dy = 0
        
        move_x = self.xcor() + dx
        move_y = self.ycor() + dy
        
        if (move_x, move_y) not in Walls:
            self.goto(move_x, move_y)
        else:
            self.direction = random.choice(["up", "down", "left", "right"])
            
        turtle.ontimer(self.threat_movement, t = random.randint(90, 270))
        
        if self.close(player):
            if player.xcor() < self.xcor():
                self.direction = "left"
            elif player.xcor() > self.xcor():
                self.direction = "right"
            elif player.ycor() < self.ycor():
                self.direction = "down"
            elif player.ycor() > self.ycor():
                self.direction = "up"
                
    #Defining a 'disappear from the map' instance
    def Disappear(self):
        self.goto(1000, 1000)
        self.hideturtle()
        
    def close(self, other):
            a = self.xcor() - other.xcor()
            b = self.ycor() - other.ycor()
            distance = math.sqrt((a ** 2) + (b ** 2))
            if distance < 75:
                return True
            else:
                return False

#Creating magic exit portal
class Exit(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("Portal.gif")
        self.penup()
        self.speed(0)
        
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
"O         OO    OOO   OO",
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
"OM C       TOOOOO       O",
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
                
            if character == "M":
                exitportal.goto(screen_x, screen_y)
                
            #Locates coins positions
            if character == "C":
                Treasures.append(Coin(screen_x, screen_y))

            if character == "T":
                Threats.append(Threat(screen_x, screen_y))
        
    print("You are in Room 01")

threats = open("threats.txt","w")
threats.write("The magic portal has warped ou into an Angry Ogre." )
threats.write("\nThe magic portal has warped you into the rage of a Wild Boar.")
threats.write("\nThe magic portal has warped you into the Venomous Hissing snake.")
threats.write("\nThe magic portal has warped you into Lunatic Peter.")
threats.write("\nThe magic portal has warped you into the Cheeky Gremlin.")
threats.write("\nThe magic portal has warped you into Furious Troll.")
threats.close()

def random_line(threat_list):
    lines = open(threat_list).read().splitlines()
    return random.choice(lines)


#Class instances
wall = Wall()
player = Player()
exitportal = Exit()
#Walls coordinate list
Walls = []

#Portals list
Portals = []

#Setting up room
room_setup(Rooms[1])

#Binding keyboard for player movement
turtle.listen()
turtle.onkey(player.move_up, "Up")
turtle.onkey(player.move_down, "Down")
turtle.onkey(player.move_left, "Left")
turtle.onkey(player.move_right, "Right")

for threat in Threats:
    turtle.ontimer(threat.threat_movement, t = 230)
        
#Main game loop
while True:
    
    for coin in Treasures:
        if player.collided(coin):
            player.gold += coin.gold #Update player gold
            print ("You have", player.gold, "gold.")
            coin.Disappear()
            Treasures.remove(coin)
            
    for threat in Threats:
        if player.collided(threat):
            print(random_line("threats.txt")) #Print random threat
            print("What will you do?")
            threat.Disappear()
            Threats.remove(threat)
    
    if player.collided(exitportal):
        room_setup(Rooms[2])
        Rooms.remove(Room_1)
        Rooms.hideturtle(Room_1)
        print("You have made it to Room 02")

    window.update()