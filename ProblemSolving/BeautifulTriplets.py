#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulTriplets function below.


def beautifulTriplets(d, arr):
    cnt = 0
    for i in arr:
        if arr.index(i) >= len(arr) - 2:
            break
        second = arr.count(i + d)
        third = arr.count(i + 2 * d)
        if second * third > 0:
            cnt += 1
    return cnt

if __name__ == '__main__':
    inputs = [
                [3, [1, 2, 4, 5, 7, 8, 10]]
            ]
    for input in inputs:
        result = beautifulTriplets(input[0], input[1])
        print(result)
