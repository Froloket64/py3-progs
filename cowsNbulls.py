## AIM --> Create a cows'n'bulls game ##

# TODO:
# DONE! 1. Make a random 4-digit number generator.
# DONE! 2. Ask player for a guess of the number.
# 3. For correct guess of a digit -- give him a cow.
# 4. For correct guess of a digit, but in a wrong position -- bull.
# 5. When player guessed the full number correctly -- end the game.
# 6. Count player's moves and print them at the end.

from random import randint


def gsplit( word ):
    lst = []
    for char in word:
        lst.append(char)
    return lst


num = str( randint( 1000, 9999 ) )

while True:
    cows = 0
    bulls = 0
    br = 0

    #Debug:
    print(num)

    guess = input("What's the number? ")

    for pos, char in enumerate(guess):
        if guess[pos] == num[pos]:
            cows += 1
        elif char in gsplit(num):
            bulls += 1

    if guess == num:
        break

    print(f'Your cows: {cows}; Your bulls: {bulls}')


print('You guessed the number!')
