#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the squares function below.
def squares(a, b):

    sqrt1 = int(math.sqrt(a))
    sqrt2 = int(math.sqrt(b))

    if sqrt1 == math.sqrt(a):
        sqrt1 -= 1

    return sqrt2 - sqrt1

if __name__ == '__main__':
    lst = [[3, 9],
            [17, 24],
            [35, 70],
            [100, 1000],
            [465868129, 988379794],
            [181510012, 293922871],
            [395151610, 407596310],
            [481403421, 520201871],
            [309804254, 776824625],
            [304742289, 566848910],
            [267554756, 828997506]
            ]

    for array in lst:
        result = squares(array[0], array[1])
        print(result)
