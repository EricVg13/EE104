# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 15:04:11 2022

@author: Eric
"""


# implement your own Hacks and Tweaks for any 3 of the options below: 
# Change the Actor, // A Need for Speed (Done)  // Try Again (DONe).

import pgzrun
import pygame
import pgzero
import random
from pgzero.builtins import Actor
from random import randint

#Declare constants
FONT_COLOR = (51, 255, 0)
WIDTH = 800
HEIGHT = 600
CENTER_X = WIDTH / 2
CENTER_Y = HEIGHT / 2
CENTER = (CENTER_X, CENTER_Y)
FINAL_LEVEL = 6
snowflakeT_SPEED = 10
COLORS = ["green", "blue"]

# playing-game music
pygame.mixer.music.load('background_music.mp3')
pygame.mixer.music.play()# playing background music

#Declare global variables
game_over = False
game_complete = False
current_level = 1 # Keep track of what level the player’s on.
 
#Keep track of the snowflakes on the screen
snowflakes = []
animations = []

#Draw the snowflakes
def draw():
    global snowflakes, current_level, game_over, game_complete
    screen.clear()
    screen.blit("snow_background", (0,0)) #add a background image to the game window
    
    #When the game is over or complete, this block displays the relevant message on the screen
    if game_over: 
        display_message("GAME OVER!\n", "Try again by pressing 'Space bar'")
    elif game_complete:
        display_message("YOU WON!", "Well done.")
    else:
        #draws the snowflakes on the screen.
        for snowflake in snowflakes:
            snowflake.draw()

# Define the update() function
def update():
    global snowflakes, game_complete, game_over, current_level
    if len(snowflakes) == 0:
        snowflakes = make_snowflakes(current_level)
    if (game_complete or game_over) and keyboard.space:
        snowflakes = []
        current_level = 1
        game_complete = False
        game_over = False

# Make the snowflakes
def make_snowflakes(number_of_extra_snowflakes):
    colors_to_create = get_colors_to_create(number_of_extra_snowflakes)
    new_snowflakes = create_snowflakes(colors_to_create)
    layout_snowflakes(new_snowflakes)
    animate_snowflakes(new_snowflakes)
    return new_snowflakes

# Add placeholders
def get_colors_to_create(number_of_extra_snowflakes):
    #return[]
    colors_to_create = ["red"] # makes the first snowflake in the list red
    for i in range(0, number_of_extra_snowflakes):
        random_color = random.choice(COLORS)
        colors_to_create.append(random_color) #adds the new color to the list.
    return colors_to_create

#Create the snowflakes
def create_snowflakes(colors_to_create):
    new_snowflakes = [] # This list will store the new snowflakes that are created
    for color in colors_to_create:
        snowflake = Actor("snowflake-" + color)
        new_snowflakes.append(snowflake)
    return new_snowflakes

# Place the snowflakes
def layout_snowflakes(snowflakes_to_layout):
    #pass
    number_of_gaps = len(snowflakes_to_layout) + 1
    gap_size = WIDTH / number_of_gaps
    random.shuffle(snowflakes_to_layout) 
    for index, snowflake in enumerate(snowflakes_to_layout):
        new_x_pos = (index + 1) * gap_size
        snowflake.x = new_x_pos

# Animate the snowflakes
def animate_snowflakes(snowflakes_to_animate):
    #pass
    for snowflake in snowflakes_to_animate:
        random_speed_adjustment = random.randint(0,2) # increase speed
        duration = snowflakeT_SPEED  - current_level + random_speed_adjustment
        snowflake.anchor = ("center", "bottom")
        animation = animate(snowflake, duration=duration, on_finished=handle_game_over, y=HEIGHT)
        animations.append(animation)

# Game over
def handle_game_over():
    global game_over 
    game_over = True
    
 
# Handle mouse clicks
def on_mouse_down(pos):
    global snowflakes, current_level
    for snowflake in snowflakes:
        if snowflake.collidepoint(pos):
            if "red" in snowflake.image:
                red_snowflake_click()
            else:
                handle_game_over()

# Click a red snowflake
def red_snowflake_click():
    global current_level, snowflakes, animations, game_complete 
    stop_animations(animations)
    if current_level == FINAL_LEVEL:
        game_complete = True
    else:
        current_level = current_level + 1
        snowflakes = []
        animations = []

# Stop the animations        
def stop_animations(animations_to_stop):
    for animation in animations_to_stop:
        if animation.running:
            animation.stop()

# Display messages            
def display_message(heading_text, sub_heading_text):
    screen.draw.text(heading_text, fontsize=60, center=CENTER, color=FONT_COLOR)
    screen.draw.text(sub_heading_text,
                     fontsize=30,
                     center=(CENTER_X, CENTER_Y+30),
                     color=FONT_COLOR)

# shuffle mode
def shuffle():
    global snowflakes
    if snowflakes:
        x_values = [snowflake.x for snowflake in snowflakes]
        random.shuffle(x_values)
        for index, snowflake in enumerate(snowflakes):
            new_x = x_values[index]
            animation = animate(snowflake, duration=0.1, x=new_x)
            animations.append(animation)

clock.schedule_interval(shuffle, 1)
pgzrun.go()