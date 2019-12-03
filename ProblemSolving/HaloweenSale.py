#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the howManyGames function below.


def howManyGames(p, d, m, s):
    ret = 0
    balance = s
    if s - p > 0:
        ret += 1
        balance -= p

    cutted = p
    while cutted > m:
        cutted -= d
        if cutted < m:
            break
        if balance - cutted > 0:
            ret += 1
            balance -= cutted

    ret += balance // m

    return ret


if __name__ == '__main__':
    inputs = [
                [20, 3, 6, 80],
                [20, 3, 6, 85]
    ]
    for input in inputs:
        print(howManyGames(input[0], input[1], input[2], input[3]))
