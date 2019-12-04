import math
import os
import random
import re
import sys

from collections import defaultdict

def getCombination(n, arr):
    arr.sort()
    combination = defaultdict(list)
    for i in range(n):
        for j in range(math.floor(i / 2) + 1):
            k = i - j
            isJin = j in (arr) or len(combination[j]) > 0 or j == 0
            isKin = k in (arr) or len(combination[k]) > 0 or k == 0
            if isJin and isKin:
                if j == 0:
                    combination[i].append([k])
                elif k == 0:
                    combination[i].append([j])
                else:
                    combination[i].append([j, k])

    return 0

if __name__ == '__main__':
    print(getCombination(10, [2,5,3,6]))
