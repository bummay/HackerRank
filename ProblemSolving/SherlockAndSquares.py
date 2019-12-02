#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the squares function below.
def squares(a, b):
    ret = 0

    for i in range(a, b + 1):
        sq = math.sqrt(i)
        if sq == int(sq):
            ret += 1

    return ret

if __name__ == '__main__':
    lst = [[3, 9],
            [17, 24],
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
