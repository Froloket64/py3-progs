## AIM --> Count even nums

def listify(word):
    out = []
    temp = ''
    for char in word:
        if char != ' ':
            temp += char
            if word.index(char) == len(word) - 1:
                out.append( int(temp) )
        else:
            out.append( int(temp) )
            temp = ''
    return out


# arr = range(0, 4 + 1)
inp = input('Numbers: ')
evens = []

# Converting -input- into an array
arr = listify(inp)

for char in arr:
    if char % 2 == 0:
        evens.append( str(char) )


final = ', '.join(evens)


print(f'Numbers: {list(arr)}')
print(f'Even ones: {final}')
