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

## Keybinds mb ?..
# kb = {}


## Drawing a ball!!
ball = pygame.image.load('img/ball.gif')
rect_size = (640, 320)
# width, height = rext_size
speed = [0, 0]

rect = ball.get_rect()


## The whole "gaming" (?) process
running = True
while running:
    ## Adding the background
    screen.fill(bg)
    pygame.display.update()

    for event in pygame.event.get():
        ## Debug
        print(event)

        ## Keybinds
        if event.type == KEYDOWN:    ## Would be pygame.KEYDOWN if pygame.locals wasn't imported
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


        ## Set window title
        pygame.display.set_caption('Lul kek')

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

        pygame.display.update()

        ## End game if smth...
        if event.type == pygame.QUIT:
            running = False
