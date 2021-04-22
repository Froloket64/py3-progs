###   This is the SAbEncryption cracker, made to show the weakness of the SAbE (why? well, just for fun)   ###

## General principles:
## - Make math operation, with each guess of the key
## Output format:
## - Wrong guess prints a line with format -<key>: [Err: values too high for ASCII]-
## - A possible guess prints -<key>: <phrase>-


from blessings import Terminal   ## |-- Some prettyfied terminal output with Blessings
t = Terminal()                   ## |


crypted = input('The phrase to decrypt: ')


## The HACK-ing process
for key in range(0, 255 + 1):
    guess = ''
    tmp = ''
    for pos, char in enumerate(crypted):
        tmp += char
        try:
            ## Makes sure that -tmp- currently has 3 digits, for any plaintext symbol is always encrypted into a 3-digit number
            if pos in range(2, 10000, 3):
                ## Adds a character (stored in -tmp-) to a final guess (for the current key), via
                guess += str( chr( int(tmp) - 100 - key ) )
                tmp = ''
        ## It may (and, is likely to do frequently) be so, that the number would be too large for the -chr()- func, so let's leave those blank
        except ValueError:
            break
    if guess == '':
        print( f'{key}: ' + t.bold_red('[Err: values too high for ASCII]') )
    else:
        print(f'{key}: {guess}')
