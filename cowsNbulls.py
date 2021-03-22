##  Create a Cows'n'Bulls game  ###

# TODO:
# 6. Count player's moves and print them at the end.
# 7. Comment the stuff better.

from random import randint

moves = 0

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

    moves += 1

    print(f'Your cows: {cows}; Your bulls: {bulls}')


print('You guessed the number!')
