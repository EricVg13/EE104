# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 22:27:09 2022

@author: Eric
"""

## Leverage the base code from chapter Balloon Flight and 
## add your own Hacks and Tweaks for any 4 of the options below: 
# 1. More High Scores, (add more 0 in .txt)
# 2. Speed It Up,  (done)    
# 3. Add in Multiples of Each Obstacles,  (done)
# 4. Level Up,  (done)


import pgzrun
import pygame
import pgzero
import random
from pgzero.builtins import Actor
from random import randint

# define the size of the game window
WIDTH = 800
HEIGHT = 600

# Create new actors
balloon = Actor("balloon")
balloon.pos = 400, 300

# playing-game music
pygame.mixer.music.load('background_music.mp3')
pygame.mixer.music.play()# playing background music

## Prepare the obstacles
bird = Actor("bird-up")
bird.pos = randint(800, 1600), randint(10, 200)
bird2 = Actor("bird-up")
bird2.pos = randint(800, 1600), randint(10, 200)


house = Actor("house")
house.pos = randint(800, 1600), 460
house2 = Actor("house")
house2.pos = randint(800, 1600), 460

tree = Actor("tree")
tree.pos = randint(800, 1600), 450
tree2 = Actor("tree")
tree2.pos = randint(800, 1600), 450


## Create global variables
bird_up = True
up = False
game_over = False
score = 0
number_of_updates = 0
level = 1 
delay = 0.1


scores = []


##  Manage the high scores
def update_high_scores():
    global score, scores
    filename = r"S:/1.SJSU/EE104_ChristopherPham/Lab8/Submission/Part3_Game_Balloon.Flight/high-scores.txt"
    scores = []
    with open(filename, "r") as file:
        line = file.readline()
        high_scores = line.split()
        for high_score in high_scores:
            if(score > int(high_score)):
                scores.append(str(score) + " ")
                score = int(high_score)
            else:
                scores.append(str(high_score) + " ")
    with open(filename, "w") as file:
        for high_score in scores:
            file.write(high_score)

def display_high_scores():
    screen.draw.text("HIGH SCORES", (350, 150), color="black")
    y = 175
    position = 1
    for high_score in scores:
        screen.draw.text(str(position) + ". " + high_score, (350, y), color="black")
        y += 25
        position += 1


## Create the draw() function        
def draw():
    screen.blit("background", (0, 0))
    if not game_over:
        balloon.draw()
        bird.draw()
        bird2.draw()      
        house.draw()
        house2.draw()
        tree.draw()
        tree2.draw()
        screen.draw.text("Score: " + str(score), (700, 5), color="black") # Display scores on screen
        screen.draw.text("level: " + str(level), color="red", topleft=(10, 10),fontsize=50)
       
    else:
        display_high_scores()


## Reacting to mouse clicks        
def on_mouse_down():
    global up
    up = True
    balloon.y -= 50 # Handle mouse button presses
                    # a = a - 1 is the same as a -= 1
                    # a = a / 1 is the same as a /= 1
                    # a = a * 1 is the same as a *= 1  
def on_mouse_up():
    global up
    up = False


## Make the bird flap    
def flap():
    global bird_up
    if bird_up:
        bird.image = "bird-down" # if the bird's wings are up, change it to down
        bird2.image = "bird-down" # if the bird's wings are up, change it to down
        bird_up = False
    else:
        bird.image = "bird-up"  # if the bird's wings are down, change it to up
        bird.image = "bird-up"  # if the bird's wings are down, change it to up
        bird_up = True
        
## Create the update() function           
def update():
    global game_over, score, number_of_updates, level
    if not game_over:
        if not up:
            balloon.y += 1 # Add in gravity
        
        ## Move the bird
        if bird.x > 0 or bird2.x >0:
            bird.x -= 20 ## control the speed of bird
            bird2.x -= 15
            if number_of_updates == 9:
                flap()
                number_of_updates = 0
            else:
                number_of_updates += 1
        
        ## Handle the bird flying off the screen
        else:
            bird.x = randint(800, 1600) # places the bird at a random position off the right side of the screen
            bird.y = randint(10, 200)
            bird2.x = randint(800, 1600) # places the bird at a random position off the right side of the screen
            bird2.y = randint(10, 200)            
            score += 1
            number_of_updates = 0
        
        ## Move the house
        if house.right > 0 or house2.right >0:
            house.x -= 2
            house2.x -=3
            
        else:
            house.x = randint(800, 1600)
            house2.x = randint(800,1600)
            score += 1
        
        ## Move the tree    
        if tree.right > 0 or tree2.right >0:
            tree.x -= 2
            tree2.x -= 3
        else:
            tree.x = randint(800, 1600)
            tree2.x = randint(800, 1600)           
            score += 1
        
            
        ## Keep it steady      
        if balloon.top < 0 or balloon.bottom > 560: # checks if the balloon has touched the top or bottom of the screen
         #  lives -=1

           game_over = True
           update_high_scores()
        
            
        ## Handle collisions with obstacles
        if balloon.collidepoint(bird.x, bird.y) or \
           balloon.collidepoint(bird2.x, bird2.y) or\
           balloon.collidepoint(house.x, house.y) or \
           balloon.collidepoint(house2.x, house.y) or \
           balloon.collidepoint(tree.x, tree.y) or\
           balloon.collidepoint(tree2.x, tree.y):
                game_over = True
                update_high_scores()
        
        ## level up
        if score == 5 and level == 1:
            level += 1
        if score == 10 and level == 2:
            level += 1        
        if score == 30 and level == 3:
            level += 1
        if score == 60 and level == 4:
            level += 1

pgzrun.go()