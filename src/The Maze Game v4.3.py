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
        self.gold = 0 #Player starts with 0 Gold
    
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

#Creating Treasure
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

class Chest(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("circle")
        self.penup()
        self.speed(0)
        self.gold = 100 #Chest will award user with 100 Gold
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
        self.gold = - 1
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
    
    #Defining 'proximity sensor' for Threat
    def close(self, other):
            a = self.xcor() - other.xcor()
            b = self.ycor() - other.ycor()
            distance = math.sqrt((a ** 2) + (b ** 2))
            if distance < 75:
                return True
            else:
                return False

#Creating level 2 Threat
class Threat2(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("Threat.gif")
        self.penup()
        self.speed(0)
        self.gold = - 2
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
    
    #Defining 'proximity sensor' for Threat    
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
    
    #Defining a 'disappear from the map' instance
    def Disappear(self):
        self.goto(1000, 1000)
        self.hideturtle()

#Creating magic exit portal for level 2
class Exit2(turtle.Turtle):
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
"OOOOOOOO  OOOOOOO  O   GO",
"OOOOOOOO  OOOOOOO  O    O",
"OM C       TOOOOO       O",
"OOOOOOOOOOOOOOOOOOOOOOOOO"
]

Room_2 = [
"OOOOOOOOOOOOOOOOOOOOOOOOO",
"O   OOOO  OO   CO    OtOO",
"O P OOOO  OO OOOO OO O OO",
"O         OO    O    O  O",
"OOOO OO                 O",
"OOO  OO  OOOOOOOOOOOOOOOO",
"OOO  OO  O       OOOO   O",
"O       O  O OO  OOOO OOO",
"O  O   O  O  OOO      OOO",
"O  O  O  O   OOO  OOOOOOO",
"O OO OC O    OOO       OO",
"O OO  O O  OOOOO OOO O  O",
"O  O   O   OOOOO OO     O",
"O OOOOOOOO  OOOt  O  OOOO",
"O  O        OOOOCOO  OOOO",
"OO O OOOOOOOOOO  tO OOOOO",
"O  O OOOOOOOOOOO OO OOOOO",
"O OO   O   O         OOOO",
"O OO OOO   O OOO     OOOO",
"O  O OOO   O OOO       OO",
"O      OOOOO OOOOOO OO OO",
"OOOOO    OOO   OOOO O  tO",
"OtOOOO  OOOOOO O OO O   O",
"O C     OOOOm CO    O G O",
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
            
            #Locates Level 1 portal position
            if character == "M":
                exitportal.goto(screen_x, screen_y)
             
            #Locates Level 1 portal position
            if character == "m":
                exitportal2.goto(screen_x, screen_y)
                
            #Locates coins positions
            if character == "C":
                Treasures.append(Coin(screen_x, screen_y))

            #Locates chest positions
            if character == "G":
                Treasures.append(Chest(screen_x, screen_y))
                
            #Locates Level 1 Threat position
            if character == "T":
                Threats.append(Threat(screen_x, screen_y))
                
            #Locates Level 2 Threat position
            if character == "t":
                Threats.append(Threat2(screen_x, screen_y)) 
        

threat1_text = open("threat1.txt","w")
threat1_text.write("\nOh no! You have run into the Venomous Hissing snake.")
threat1_text.write("\nYou have lost 1 coin.")
threat1_text.close()

def threat1_print(threat_read):
    lines = open(threat_read).read()
    return (lines)

threat2_text = open("threat2.txt","w")
threat2_text.write("\nOh no! You have run into the Venomous Hissing snake.")
threat2_text.write("\nYou have lost 2 coin.")
threat2_text.close()

def threat2_print(threat_read):
    lines = open(threat_read).read()
    return (lines)

congratulations = open("congrats.txt","w")
congratulations.write("\nCongratulations! You have completed the game.")
congratulations.close()

def congrats(congrats_read):
    lines = open(congrats_read).read()
    return (lines)

level2 = open("level2.txt","w")
level2.write("\nYou have made it to Room 02.")
level2.close()

def level_2(level2_read):
    lines = open(level2_read).read()
    return (lines)

#Class instances
wall = Wall()
player = Player()
exitportal = Exit()
exitportal2 = Exit2()
#Walls coordinate list
Walls = []

#Setting up room
room_setup(Rooms[1])

print("You are in Room 01")

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
            print(threat1_print("threat1.txt")) #Print threat encounter dialogue
            player.gold += threat.gold #Update player gold
            print ("You have", player.gold, "gold.")#Print player gold
            
    if player.collided(exitportal):
        player.gold = 0
        wall.clearstamps(1000) #Remove previous game's wall stamps
        Walls.clear() #Clears coordinates of last game's walls
        for all in Threats:
            all.Disappear() #Removes all Threat from previous game
        for all in Treasures:
            all.Disappear() #Removes all Treasures from previous game
        exitportal.Disappear() #Removes portal from previous game
        break
    
    window.update()
    


room_setup(Rooms[2])

print(level_2("level2.txt"))

for threat in Threats:
    turtle.ontimer(threat.threat_movement, t = 230)
    
while True:
    
    for coin in Treasures:
        if player.collided(coin):
            player.gold += coin.gold #Update player gold
            print ("You have", player.gold, "gold.")
            coin.Disappear()
            Treasures.remove(coin)
            
    for threat in Threats:
        if player.collided(threat):
            print(threat2_print("threat2.txt")) #Print threat encounter dialogue
            player.gold += threat.gold #Update player gold
            print ("You have", player.gold, "gold.")#Print player gold
    
    if player.collided(exitportal2):
        print(congrats("congrats.txt"))
        window.bye()
        
    window.update()
