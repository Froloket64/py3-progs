###  A function that defines whether you can wrap a given word  ###

## Thoughts:
# 1. If there is only 1- vowel --> False


def wrapCheck(word):
    ## Words:
    # - kill
    # - do
    # - people
    # - sample
    # - prerequisites


    vowels = 0


    if len(word) <= 5:  ## Pretty self-explanatory
        return False


    for char in 'aeyou':  ## Check if there are any vowels in the word
        vowels += word.count(char)  ## Count vowels there


    if vowels <= 0:
        return False


    return True


## ~Random Tests
#for word in :
#    wrapCheck()

## Fixed Tests
print( [wrapCheck('kill'),  ## GTG
    wrapCheck('do'),  ## GTG
    wrapCheck('people'),
    wrapCheck('sample'),
    wrapCheck('prerequisites')] )

## Add. Tests
print(wrapCheck('prepare'))
