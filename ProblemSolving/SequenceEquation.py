#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the permutationEquation function below.
def permutationEquation(p):
    ret = []
    pos1 = pos2 = 0
    for i in range(len(p)):
        pos1 = p.index(i + 1) + 1 if i + 1 in p else 0
        pos2 = p.index(pos1) + 1 if pos1 in p else 0
        ret.append(pos2)
    return ret

if __name__ == '__main__':
    input = [
            [2, 3, 1],
             [4, 3, 5, 1, 2]
            ]
    for lst in input:
        result = permutationEquation(lst)
        prt = '\n'.join(map(str, result))
        print(prt)
        print('\n')
