###  A function that defines whether you can wrap a GIVEN word from a GIVEN point (index) or inside it.  ###


## Thoughts:
# 1. If there are no vowels in the part of the word given, it can't be wrapped. [DONE]
# 2. If there is only 1 vowel AND first character isn't a vowel AND the next one is, it'll not be wrapped.
# 3. If the part has a vowel, after which we get a non-vowel AND a syllable of 3+ chars, it can be.


def wrapCheck(word, n):
    ## Words:
    # - kill
    # - do
    # - people
    # - sample


    w1 = word[n:]
    isHere = False
    vowels = 0


    if len(word) <= 5:  ## Pretty self-explanatory
        return False
    if len(w1) <= 3:  ## Same here
        return False


    for char in 'aeyou':  ## Check if there are any vowels after nth character in the word
        if char in w1:
            isHere = True
            break

        vowels += w1.count(char)  ## Count vowels in the part


#     if 


    if not isHere:  ## If there are no vowels (in the part), return False without further ado
        return False
#    if [word.count(char) for char in 'aeyou'] == 1:

    return True


#for word in :
#    wrapCheck()

## ~Random Tests
print( [wrapCheck('kill', 0),  ## GTG
    wrapCheck('do', 0),  ## GTG
    wrapCheck('people', 0),
    wrapCheck('sample', 0)] )

## Fixed Tests
print(wrapCheck('prepare', 3))
