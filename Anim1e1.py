# Anim1e1.py
#In Python code it looks like this:
"""
If you click the mouse on this game window, a little bot is born.
It will move about randomly.  If it collides with another, it will devour
the other and grow.
"""
import os
import pygame, sys
# from numpy import random
import random
import math
from pygame.locals import *
# from ButtonCLASS import *

class myagent:
    def __init__(self, x, y, id,isALIVE=True):
        self.x = x
        self.y = y
        self.diam = 11.0
        self.w = int(self.diam)
        self.h = int(self.diam)

        self.ALIVE = isALIVE
        self.speed = 0
        self.angle = 0

        self.rect = Rect(x,y,self.w,self.h)
        self.id = id

    def eat(self ):
        agent.diam *= 2
        self.w = int(self.diam)
        self.h = int(self.diam)

    def display(self ):
        aliveColor = (255,0,0)
        deadColor = (100,100,100)
        sparkle = (255,255,255)
        width = 0  #line width.  if 0, circle is filled

        x = int(self.x)
        y = int(self.y)
        if self.ALIVE:
            #circle(Surface, color, pos, radius, width=0) returns a Rect
            pygame.draw.circle(myscreen, aliveColor, (x,y),self.w,width)    #Light
            pygame.draw.circle(myscreen, sparkle, (x+5,y-5),4,width) #sparkle
        else: #Dead
            print "off"
            #circle(Surface, color, pos, radius, width=0) returns a Rect
            pygame.draw.circle(myscreen, deadColor, (x,y),self.w,width)   #Light

    def move(self ):
        self.x += math.sin(self.angle) * self.speed
        self.y -= math.cos(self.angle) * self.speed
        if self.x > 400: self.speed = -self.speed
        if self.x < 0: self.speed = -self.speed
        if self.y < 0: self.y = 300
        if self.y > 300: self.y = 0

#---------------------------------
# THE GAME


pygame.init()
myscreen = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Simple Animation!')
UP_DN = "UP"
BUTTON_DOWN = False

red = (255,0,0)   # Color is defined as (Red, Green, Blue)
green = (0,255,0)  # Each parameter is an integer between 0 and 255.
radius = 15
cur_x = 0
cur_y = 0
keyPress = ""
LED_ON_OFF = "OFF"
numagents = 0
agents = []
agentid=0

while True: # main game loop
    # Note Indents let the inperpreter know the following code is a subset
    # of the while command.
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()


        #########################################################
        #  MOUSE EVENTS (always active independent of game mode)
        #########################################################
        elif (event.type == pygame.MOUSEMOTION ):#
            pass #Move Mouse

        elif (event.type == pygame.MOUSEBUTTONDOWN ):#Mouse Clicked
            # get current mouse position of Click event
            cur_x,cur_y = pygame.mouse.get_pos()

            newagent = myagent(cur_x,cur_y,agentid, True)
            agentid+=1
            agents.append(newagent)

        elif (event.type == pygame.MOUSEBUTTONUP ):#Mouse Clicked
            pass

    myscreen.fill((0,0,0))

    for agent in agents:
        if agent.ALIVE:
            agent.speed = random.random()
            agent.angle = random.uniform(0, math.pi*2)
            agent.move()
            agent.display()
            for another_agent in agents:
                #print (agent.id, another_agent.id)
                if agent.id != another_agent.id:
                    dist = math.sqrt((agent.x-another_agent.x)**2 + (agent.y-another_agent.y)**2)

                    #print (agent.id, another_agent.id, len(agents),dist)
                    if dist<12:
                        agent.eat()
                        agents.remove(another_agent)

                        print ("collision")

    pygame.display.flip()
