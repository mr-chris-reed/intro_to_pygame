# STUDENT (1 pt): COMPLETE THE COMMENT ID BLOCK
####################################################
# Student Name: 
# Date Completed:
# Course Name: Intro to Computer Science
# Assignment: Intro to PyGame
# Original Authors: Mr. Alfonso & Mr. Reed
# Date Created: 10/13/2025
####################################################



# imports for pygame
import pygame, sys
from pygame.locals import *

# canvas variables

###
# STUDENT (2 pts): SET TWO VARIABLES, ONE FOR width AND ONE FOR height
# AND SET THESE TO THE VALUES YOU WANT FOR THE CANVAS
# SIZE
###

# other variables
# explanation: makes it so that the original position 
# of your image is in the middle of your screen
image_x_pos = width // 2
image_y_pos = height // 2

###
# STUDENT (2 pts): SET TWO VARIABLES, ONE FOR image_x_delta AND ONE FOR 
# image_y_delta AND SET THESE VALUES. THESE VALUES WILL
# DETERMINE HOW FAR YOU IMAGE MOVES FOR EACH KEY PRESS.
###

# frame rate
fps = 60

###
# STUDENT (3 pts): SET THREE VARIABLES, ONE FOR r, ONE for g, 
# ONE for b, AND SET THESE VALUES SUCH THAT EACH
# VARIABLE IS IN BETWEEN THE VALUES OF 0 TO 255
###


# Sets background color 
background_color = (r, g, b)

# initializing pygame, setting up the surface (canvas)
pygame.init()
canvas = pygame.display.set_mode((width, height))
pygame.display.set_caption("PYGAME TEST") # add a caption for your canvas

###
# STUDENT (4 pt): 
#
# 1. REPLACE "TEST.png" (keep the quotes)
# WITH THE ACTUAL FILE NAME AND EXTENSION OF THE 
# IMAGE YOU WANT TO USE
#
# 2. CREATE A VARIABLE NAMED "picScaledFactor" THAT
# STORES AN INTEGER OF YOUR CHOOSING
#
# 3. CREATE A VARIABLE NAMED "scaledPicHeight" THAT
# STORES THE VALUE OF myPicHeight * picScaledFactor
#
# 4. CREATE A VARAIBLE NAMED "scaledPicWidth" THAT
# STORES THE VALUE OF myPicWidth * picScaledFactor
###
myPic = pygame.image.load("TEST.png").convert_alpha()
myPicHeight = myPic.get_height()
myPicWidth = myPic.get_width()

# Insert Steps 2 - 4 within this space.

scaledPic = pygame.transform.scale(myPic, (scaledPicWidth, scaledPicHeight))

# clock to set FPS
clock = pygame.time.Clock()

# variable to control state of entire game
running = True

while running:
    # paint the canvas with background color
    canvas.fill(background_color)

    # poll for events
    for event in pygame.event.get():
        # if 'X' is clicked on the canvas
        if event.type == QUIT:
            running = False

    # get all keys that are currently pressed    
    keys = pygame.key.get_pressed()

    # check to see if any of the keys are w, a, s, or d
    # and perform an action
    if keys[pygame.K_w] and image_y_pos > 0:
        image_y_pos -= image_y_delta
    if keys[pygame.K_s] and image_y_pos < height - myPicHeight:
        image_y_pos += image_y_delta
    if keys[pygame.K_a] and image_x_pos > 0:
        image_x_pos -= image_x_delta
    if keys[pygame.K_d] and image_x_pos < width - myPicWidth:
        image_x_pos += image_x_delta

    # blit your image
    canvas.blit(scaledPic, (image_x_pos, image_y_pos))

    pygame.display.update()
    clock.tick(fps)

# close pygame down
pygame.quit()
sys.exit()