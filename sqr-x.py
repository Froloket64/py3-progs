###  AIM --> Generate random square equations ###


## TODO:
## All done, I suppose. ::CONGRATS!!::


from random import randint, randrange
from math import sqrt # Gonna be needed for square root
from os import system # Gonna be needed for terminal 'clear'ing


# Enabling Debug
isDebug = input('Shall I solve it for you? [y/n]\n> ')

# Asking for the following:
while True:
    isDneg = input('Let equations with no roots generate? [y/n]\n> ')
    if isDneg == 'y' or isDneg == 'n':
        break
    else:
        print('You should type either "y" or "n"')


# Asking for amount of characters to be a, b and c
chr_num = int( input('How much characters would you prefer? (Not more than 5)\n> ') )

assert chr_num <= 5 , 'Number of chars should be less or equal to 5'
assert chr_num > 0 , 'Number of chars should be more than zero'


# Avoiding the NameError later
a = ''
b = ''
c = ''

# A little refactoring of code via var's (rang)
rang = (0, 9)

# Generating random a, b and c
for num in range( chr_num ):
    while True:
        a += str( randint( *rang ) ) # x^2
        b += str( randint( *rang ) ) # x
        c += str( randint( *rang ) ) # k
        # Recounting a, b and c if D equals to negative
        # and user asked for no such tricks
        if ( isDneg == 'n' ) and ( ( int(b)**2 - 4 * int(a) * int(c) ) < 0 ):
            a = ''
            b = ''
            c = ''
            continue
        # Firstly, if it's the last iteration and the leftmost char isn't equal to 0
        # Secondly, if it's just not the last iteration
        elif ( num == ( chr_num - 1 ) and int(a) != 0 ) or ( num != ( chr_num - 1 ) ):
            break


# I don't think I need to comment that btw
# ( For dummies such as myself:
# Converting a, b and c into integers for further use )
a = int(a)
b = int(b)
c = int(c)


# Generating the full equation within a variable
eq = f"{a}x^2 + {b}x + {c}"


# Counting D via formula
discr = b**2 - 4 * a * c


# Counting roots (if D != 0, of course)
if discr < 0:
    pass
else:
    x1 = ( -b + sqrt(discr) ) / ( 2 * a )
    x2 = ( -b - sqrt(discr) ) / ( 2 * a )


# Defying whether to print both roots, the only one, or none
# depending on the situation (discriminant value)
if discr > 0:
    roots = f'x1 = {x1} ; x2 = {x2}'
elif discr < 0:
    roots = 'Нет корней!'
elif discr == 0:
    roots = f'x = {x1}'


# Clearing the terminal
system('cls|clear')

# Printing the Equation itself:
print( f'Equation : {eq}' )


# Debug (if asked for):
if isDebug == 'y' :
    system('cls|clear')
    print( f'\n  --|DEBUG:|-- \nD = {discr} ;\n{roots}')
