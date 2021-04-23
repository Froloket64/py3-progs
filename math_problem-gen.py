###  Math problem Generator (for ~4-5th grades)  ###

## Rules:
## 1. Problems shouldn't have negative numbers neither floats
## 2. Numbers should be <= 10
## 3. Possible operations: +, -, *, /

from random import randint, choice
from operator import add, mul, truediv, sub
from math import sqrt


a = random.randint( 1, 10 )
b = random.randint( 1, 10 )
opers = [ add, sub, mul, truediv ]
i = 0
ii = 1000000


for i in range( 0, ii ) :
    oper = random.choice( opers )
    ans = oper( a, b )
    oper1 = str( oper )
    if ans == int( ans ) and ans == sqrt( ans**2 ):
        break
    else:
        continue


if oper1 == '<built-in function truediv>':
    oper = '/'
elif oper1 == '<built-in function add>':
    oper = '+'
elif oper1 == '<built-in function mul>':
    oper = '*'
else:
    oper = '-'


print( a, oper, b, '=', ans )
