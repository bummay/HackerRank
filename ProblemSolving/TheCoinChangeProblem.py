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
        if i in (arr):
            combination[i].append([i])
        for j in range(1, math.floor(i / 2) + 1):
            k = i - j
            for p in range(len(combination[j])):
                for q in range(len(combination[k])):
                    toAppend = sorted(combination[j][p] + combination[k][q])
                    if toAppend not in combination[i]:
                        combination[i].append(toAppend)

    return combination


def getWays(n, c):
    dictPatterns = getCombination(n, c)
    ret = []

    for i in range(1, math.floor(n / 2) + 1):
        j = n - i
        for p in range(len(dictPatterns[i])):
            for q in range(len(dictPatterns[j])):
                toAppend = sorted(dictPatterns[i][p] + dictPatterns[j][q])
                if toAppend not in ret:
                    ret.append(toAppend)
    return len(ret)

if __name__ == '__main__':
    inputs = [
                [10, [2, 5, 3, 6]],
                [4, [1, 2, 3]]
            ]
    for input in inputs:
        print(getWays(input[0], input[1]))
