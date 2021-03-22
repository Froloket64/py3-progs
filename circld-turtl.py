## Fill a shape (circle) with a random color

### TODO:
## 1. The only one left is to leave previously colored circles visible

from random import randint, choice
import turtle as t


## Our turtle shaping (set to the -TRUE- turtle)
t.shape('turtle')
## Our turtle speed (fastest is 'fastest')
t.speed('fast')


## Asking which mode to use
while True:
    mode = input('In which mode to run?\n' + '  1. Increasing circles (Beta)\n' + '  2. Decreasing circles\n' + 'Type the number of the mode to run: ')
    if mode == '1' or mode == '2':
        break
    print('You need to type the number of the mode you wish to run!')


## Characters for use in HEX color values
alph = ['A', 'B', 'C', 'D', 'E', 'F']

## (First) circle radius
if mode == '1':
    rad = 26.66

if mode == '2':
    rad = 26.66 + 75


## Drawing circles (Yay!)
for i in range(15):

    ## Setting numbers for  HEX coloring later
    r = str( randint(0, 9) ) + choice(alph)
    g = str( randint(0, 9) ) + choice(alph)
    b = str( randint(0, 9) ) + choice(alph)

    ## Setting a color to use for filling (reset with each iteration)
    t.fillcolor(f'#{r}{g}{b}')

    ## 
    t.begin_fill()
    t.circle(rad)
    t.end_fill()

    ## Increasing radius w/ each iteration (just for fun..?)
    if mode == '1':
        rad += 5
    if mode == '2':
         rad -= 5

## Just to not terminate the window automatically
## after executing
t.end()
