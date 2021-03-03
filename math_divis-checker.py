##  AIM --> Print all number divisors  ##


num = int( input( 'Your number : ' ) )
divis = list()
all_nums = list( range( 0, 1001 ) )


for i in all_nums :
	x = int( all_nums[ i ] )
	ans = x / num
	if ans == int( ans ) :
		divis.append( x )
                # If you want to print divisors one by one:
                print( x )
	else :
		continue

# Print all divisors at once:
# print( ' '.join(divis) )
