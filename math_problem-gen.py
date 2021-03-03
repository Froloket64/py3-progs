# Условие :
#
# Нужно, чтобы:
# 1. Генерировались числа от 1 до 10;       +
# 2. Знак между ними ( +, -, *, / );        +
# 3. Ответ не являлся отрицательным числом или дробью ( В любом проявлении ).                               + -

import random
from operator import add, mul, truediv, sub
from math import sqrt

a = random.randint( 1, 11 )
b = random.randint( 1, 11 )
opers = [ add, sub, mul, truediv ]
i = 0
ii = 1000000

for i in range( 0, ii ) :
    oper = random.choice( opers )
    ans = oper( a, b )
    oper1 = str( oper )
    if ans == int( ans ) and ans == sqrt( ans**2 ) :
        #print( 'Da' )
        break
    else :
        #print( 'Net' )
        continue

if oper1 == '<built-in function truediv>' :
    oper = '/'
elif oper1 == '<built-in function add>' :
    oper = '+'
elif oper1 == '<built-in function mul>' :
    oper = '*'
else :
    oper = '-'

# Debug :
# print( a, b )
# print( ans )

print ( a, oper, b, '=', ans )
#print( 'x = ?' )
