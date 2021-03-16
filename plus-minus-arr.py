## AIM --> Gen an arr with random pos & neg ints, where amount of pos-s is equal to amount of neg-s
# Size of array is 6

from random import choice

nums = [-1, 1]
ans = []


while True:
    ans.append( choice(nums) )

    if sum(ans) == 0 and len(ans) == 6:
        break

    # Not letting the array be bigger than 6
    if len(ans) == 7:
        ans = []

print(ans)
