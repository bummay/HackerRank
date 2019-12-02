#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kaprekarNumbers function below.
def isKapreka(n):
    length = len(str(n))

    sq = n ** 2
    digit = len(str(sq))
    if digit == 1:
        firstHalf = 0
        secondHalf = sq
    else:
        split = digit // 2
        firstHalf = str(sq)[:split]
        secondHalf = str(sq)[split:]

    if n == int(firstHalf) + int(secondHalf):
        return True
    else:
        return False

def kaprekarNumbers(p, q):
    lst = []
    for i in range(p, q + 1):
        if isKapreka(i):
            lst.append(str(i))

    ret = ' '.join(lst)
    if ret == '':
        ret = 'INVALID RANGE'
    print(ret)

if __name__ == '__main__':
    inputs = [
                [400, 700],
                [1, 100],
                [1, 1000],
                [1, 10000],
                [1, 100000],
                [1, 99999]
    ]
    for pair in inputs:
        kaprekarNumbers(pair[0], pair[1])

