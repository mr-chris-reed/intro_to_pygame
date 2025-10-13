# imports for pygame
import pygame, sys
from pygame.locals import *

# canvas variables
###
# SET TWO VARIABLES, ONE FOR width AND ONE FOR height
# AND SET THESE TO THE VALUES YOU WANT FOR THE CANVAS
# SIZE
###

### WRITE YOUR CODE HERE FOR THE CANVAS VARIABLES ###

# other variables
image_x_pos = width // 2
image_y_pos = height // 2

###
# SET TWO VARIABLES, ONE FOR image_x_delta AND ONE FOR 
# image_y_delta AND SET THESE VALUES. THESE VALUES WILL
# DETERMINE HOW FAR YOU IMAGE MOVES FOR EACH KEY PRESS.
###

### WRITE YOUR CODE HERE FOR THE MOVEMENT VARIABLES ###

# frame rate
fps = 60

# colors
background_color = (255, 255, 255)

# initializing pygame, setting up the surface (canvas)
pygame.init()
canvas = pygame.display.set_mode((width, height))
pygame.display.set_caption("PYGAME TEST") # add a caption for your canvas

# import image
myPic = pygame.image.load("myImage.png").convert_alpha()
myPicHeight = myPic.get_height()
myPicWidth = myPic.get_width()

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
    canvas.blit(myPic, (image_x_pos, image_y_pos))

    pygame.display.update()
    clock.tick(fps)

# close pygame down
pygame.quit()
sys.exit()