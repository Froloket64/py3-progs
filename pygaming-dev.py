###  THIS IS ONLY MY EXPERIMENTS!  UNDER CONSTRUCTION!  ###

import pygame
from pygame.locals import *

## Initialization
pygame.init()

## Setting the resolution for the game window
res = (800, 600)
## Creating the "game" window
screen = pygame.display.set_mode(res)

## Background color
bg = (70, 70, 70) # Gray

color = None

## Keybinds mb ?..   [not yet]
# kb = {}


### Drawing a ball!!

## Creating our -ball- object (ball image in "img" dir)
ball = pygame.image.load('img/ball.gif')
## Setting a -speed- var for moving our objects (rect)
speed = [0, 0]

## Creating the -ball-'s container (neccessary in Pygame)
rect = ball.get_rect()


## The whole "gaming" (?) process
running = True
while running:
    ## Adding the background
    screen.fill(bg)
    ## Set window title
    pygame.display.set_caption('Lul kek')

    pygame.display.update()

    for event in pygame.event.get():
        ## Debug
        print(event)

        ## Keybinds
        if event.type == KEYDOWN:    ## Would be -pygame.KEYDOWN- if -pygame.locals- wasn't imported
            if event.key == K_d:
                ## Asking for a color (just pick one)
                color = ( int(input('Red: ')), int(input('Green: ')), int(input('Blue: ')) )
            elif event.key == K_ESCAPE:
                running = False
            elif event.key == K_RIGHT:
                speed[0] += 2
            elif event.key == K_LEFT:
                speed[0] -= 2
            elif event.key == K_UP:
                speed[1] -= 2
            elif event.key == K_DOWN:
                speed[1] += 2


        ## The Ball
        rect = rect.move(speed)
        pygame.draw.rect(screen, bg, rect, 5)
        screen.blit(ball, rect)
        ## Resetting our rectangle's speed
        if speed[0] != 0 or speed[1] != 0:
            speed[0], speed[1] = 0, 0

        ## Filling the screen with -color-
        if color != None:
            screen.fill(color)

        ## Updating the screen (displaying the changes)
        pygame.display.update()

        ## End game if the close button (of the window) is pressed
        if event.type == pygame.QUIT:
            running = False
