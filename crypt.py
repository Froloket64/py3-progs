###   !! WARNING: THIS IS JUST A JOKE. DON'T EVEN TRY TO USE THIS FOR SECURITY PURPOSES !!   ###

### SAbE -- Simple ASCII-based Encryption
### -Prototype- ver.PRE-ALPHA


from random import randint   ## For a (pseudo-)random key generation

## Asking for the mode to run the program in
while True:
    mode = input('Which mode to run?\n    1. Encrypt\n    2. Decrypt\n    Type the number: ')
    if mode == '1' or mode == '2':
        mode = int(mode)
        break
    print('Type either "1" or "2"')


## The encryption mode
if mode == 1:
    ## Asking for the phrase to encrypt
    phr = input('Phrase to encrypt: ')
    ## Asking for the...
    name = input('Name of the file to save the key in: ')

    ## Generationg a key
    key = randint(0, 255)
    # key = randint(0, 4096)

    with open(name, 'w') as keyfile:
        keyfile.write( str(key) )

    crypted = ''

    ## The "encryption" itself
    for char in phr:
        crypted += str( (ord(char) + 100) + key )

    print(crypted)


## The decryption mode
if mode == 2:
    ## Asking for the phrase to decrypt
    crypted = input('The encrypted phrase:')
    ## Asking for the...
    name = input('Name of the file to read the key from: ')

    with open(name, 'r') as keyfile:
        key = int( keyfile.read() )

    tmp = ''
    phr = ''
    ## The decryption itself
    for pos, char in enumerate(crypted):
        tmp += char
        if pos in range(2, 1000, 3):
            phr += str( chr( int(tmp) - 100 - key ) )
            tmp = ''

    print(phr)
