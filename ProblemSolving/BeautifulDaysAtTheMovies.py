#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulDays function below.


def beautifulDays(i, j, k):
    ret = 0
    for m in range(i, j + 1):
        rev = int(str(m)[::-1])
        if abs(rev - m) % k == 0:
            ret += 1
    return ret


if __name__ == '__main__':
    lst = [[20,23,6], [13,45,3]]

    for i in range(len(lst)):
        result = beautifulDays(lst[i][0],lst[i][1],lst[i][2])
        print(result)
