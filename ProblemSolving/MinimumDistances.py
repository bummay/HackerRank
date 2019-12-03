#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumDistances function below.


def minimumDistances(a):
    ret = -1
    matched = []
    distinct = list(set(a))

    for i in distinct:
        list_index = [m for m, x in enumerate(a) if x == i]
        for j in range(len(list_index)):
            for k in range(j + 1,len(list_index)):
                matched.append(abs(list_index[j] - list_index[k]))

    if len(matched) > 0:
        ret = min(matched)

    return ret

if __name__ == '__main__':
    inputs = [
                [7, 1, 3, 4, 1, 7],
                [1, 2, 3, 4, 10]
            ]
    for input in inputs:
        print(minimumDistances(input))
