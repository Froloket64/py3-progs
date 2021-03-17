## AIM --> Count pos nums in arr

arr = input('Note: you should give numbers separated by spaces without other symbols (such as commas)\nArray: ')
real_arr = []
temp = ''


for char in arr:
    if char != ' ':
        temp += char
        if arr[ arr.index(char) ] == arr[ len(arr) - 1 ]:
            real_arr.append(temp)
    else:
        real_arr.append(temp)
        temp = ''

print(f'old: {real_arr}')

for num in real_arr:
    if int(num) < 0 :
        del real_arr[ real_arr.index(num) ]

final = len(real_arr)

print(f'new: {real_arr}')
print(final)
