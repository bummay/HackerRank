#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the chocolateFeast function below.


def chocolateFeast(n, c, m):
    ret = n // c
    wrapper = n // c

    while wrapper >= m:
        turn = wrapper // m
        ret += turn
        wrapper = turn + wrapper % m

    return ret

if __name__ == '__main__':
    inputs = [
                [15, 3, 2],
                [10, 2, 5],
                [12, 4, 4],
                [6, 2, 2]
    ]
    for input in inputs:
        print(chocolateFeast(input[0], input[1], input[2]))