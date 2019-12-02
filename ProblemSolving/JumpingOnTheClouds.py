#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    ret = 100

    i = 0
    while i < len(c):
        i += k
        ret -= 1
        if i >= len(c):
            i -= len(c)
        if c[i] > 0:
            ret -= 2
        if i == 0 or ret < 0:
            break

    if ret < 0:
        ret = 0
    return ret

if __name__ == '__main__':
    clouds = [
                [0, 0, 1, 0, 0, 1, 1, 0],
                [1, 1, 1, 0, 1, 1, 0, 0, 0, 0]
            ]
    steps = [
                2,
                3
            ]

    for i in range(len(clouds)):
        result = jumpingOnClouds(clouds[i], steps[i])
        print(result)
