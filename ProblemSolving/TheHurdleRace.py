#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hurdleRace function below.


def hurdleRace(k, height):
    ret = 0
    qualify = max(height)
    if qualify >= k:
        ret = qualify - k
    return ret

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # nk = input().split()

    # n = int(nk[0])

    # k = int(nk[1])

    # height = list(map(int, input().rstrip().split()))
    k = [4,7]

    height = [[1,6,3,5,2],[2,5,4,5,2]]
    for i in range(2):
        result = hurdleRace(k[i], height[i])
        print(result)
    # fptr.write(str(result) + '\n')

    # fptr.close()
