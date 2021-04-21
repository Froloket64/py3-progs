## A list with support of Minkowski addition (summing every list's elements with every other list's ones):
class MList(list):
    def __init__(self, items):
        self.lst = items


    def __add__(self, other):
        tmp = []
        [[tmp.append(i + n) for i in other] for n in self.lst]

        return sorted(set(tmp))


    def get(self):
        return self.lst


## A float with a fixed amount of digits after the floating-point:
class Fixed(float):
    def __init__(self, num, n=3):
        self.num = round(num, n)


    def __add__(self, other):
        if type(other) == type(self.num):  ##                                  |
            return self.num + other  ##                                        |
        else:  ##                                                              |-  Not yet working ;(
            raise TypeError('Cannot sum Fixed numbers with normal floats')  ## |


    def get(self):
        return self.num
