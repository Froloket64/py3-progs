## Fill a shape (circle) with a random color

### TODO:
## 1. The only one left is to leave previously colored circles visible

from random import randint, choice
import turtle as t


## Asking which mode to use
while True:
    mode = input('In which mode to run?\n' + '  1. Increasing circles (Beta)\n' + '  2. Decreasing circles\n' + 'Type the number of the mode to run: ')
    if mode == '1' or mode == '2':
        break
    print('You need to type the number of the mode you wish to run!')

## Asking for amount of circles (pt. 1)
steps = input('How much circles to draw (default is 15): ')

## Amount of circles (pt. 2)
if steps == '':
    steps = 15
else:
    steps = int(steps)


## Our turtle shaping (by default set to the -TRUE- turtle)
t.shape('turtle')
## Our turtle speed (fastest is 'fastest')
t.speed('fastest')

## Characters for use in HEX color values
alph = ['A', 'B', 'C', 'D', 'E', 'F']

## (First) circle radius
if mode == '1':
    rad = 26.66

if mode == '2':
    rad = 26.66 + 75


## Drawing circles (Yay!)
for i in range(steps):

    ## Setting numbers for  HEX coloring later
    r = str( randint(0, 9) ) + choice(alph)
    g = str( randint(0, 9) ) + choice(alph)
    b = str( randint(0, 9) ) + choice(alph)

    ## Setting a color to use for filling (reset with each iteration)
    t.fillcolor(f'#{r}{g}{b}')

    ## Drawing a circle
    ##        +
    ## Filling the (current) circle with a (random) color
    t.begin_fill()
    t.circle(rad)
    t.end_fill()

    ## In-/Decreasing radius with each iteration (just for fun..?)
    if mode == '1':
        rad += 5
    if mode == '2':
         rad -= 5


## Just to not terminate the window automatically
## after execution ends
t.done()
