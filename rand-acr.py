## AIM --> Gen rand arr which is also an acronym

from random import choice


arr = []
chars = []

for i in range(65, 123):
    chars.append( chr(i) )

chars = chars[:26] + chars[32:]

while True:
    arr.append( choice(chars) )

    if arr == list( reversed(arr) ) and len(arr) == 5:
        break

    if len(arr) > 5:
        arr = []


print(arr)
