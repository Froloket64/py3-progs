###  Claqulator!! ###

from math import factorial, sqrt


math = input('Your math: ')  ## Asking for the math to perform


math_lst = math.split()
for pos, item in enumerate( math_lst ):  ## Doing things for our user-friendly language to understand the math operations
    if item == '^':           ## |- Changing "^" (power symbol) to "**"
        math_lst[pos] = '**'  ## |
    elif '!' in item:                                            ## |- Changing "!" (factorial symbol) to "factorial()" (from "math" lib)
        math_lst[pos] = f'factorial({item[:-1]})'                ## |


## Debug:
# print(math_lst)


if math_lst == []:
    pass
else:
    ## (Trying to) catch the possibe errors
    try:
        print( f'Answer: {eval( " ".join(math_lst) )}' )  ## Evaluating the math and printing the result
    except NameError:  ## Messing the math operation syntax
        print('No such operation')
#   except SyntaxError:
#       pass
