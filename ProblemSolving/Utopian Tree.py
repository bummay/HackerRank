#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the utopianTree function below.


def utopianTree(n):
    height = 1
    i = 0
    while i <= n:
        if i > 0:
            if i % 2 != 0:
                height *= 2
            else:
                height += 1
        i += 1
    return height

if __name__ == '__main__':
    lst = [0,1,4]
    for i in range(len(lst)):
        result = utopianTree(lst[i])
        print(result)
