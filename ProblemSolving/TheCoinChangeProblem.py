import math
import os
import random
import re
import sys

from collections import defaultdict

def getCombination(n, arr):
    arr.sort()
    combination = defaultdict(list)
    for i in range(n + 1):
        if i in (arr):
            combination[i].append([i])
        else:
            combination[i] = []
        for j in range(1, math.floor(i / 2) + 1):
            k = i - j
            for p in range(len(combination[j])):
                for q in range(len(combination[k])):
                    toAppend = sorted(combination[j][p] + combination[k][q])
                    if toAppend not in combination[i] and len(toAppend) > 0:
                        combination[i].append(toAppend)

    return combination


def getWays(n, c):
    dictPatterns = getCombination(n, c)
    ret = []

    for i in range(n):
        j = n - i
        if i > j:
            break
        if list([n]) in dictPatterns[i]:
            ret.append([n])
        elif list([n]) in dictPatterns[j]:
            ret.append([n])

        for p in range(len(dictPatterns[i])):
            for q in range(len(dictPatterns[j])):
                toAppend = sorted(dictPatterns[i][p] + dictPatterns[j][q])
                if toAppend not in ret:
                    ret.append(toAppend)
    return len(ret)

if __name__ == '__main__':
    inputs = [
        [166, [5, 37, 8, 39, 33, 17, 22, 32, 13, 7, 10,
               35, 40, 2, 43, 49, 46, 19, 41, 1, 12, 11, 28]],
                [18, [49, 9, 40, 17, 46, 24, 42, 26, 43, 41, 35,
                     1, 47, 28, 20, 38, 2, 44, 32, 22, 18, 45, 25]],
                [2, [44, 5, 9, 39, 6, 25, 3, 28, 16, 19, 4, 49, 40, 22,
                    2, 12, 45, 33, 23, 42, 34, 15, 46, 26, 13, 31, 8]],
                [10, [2, 5, 3, 6]],
                [4, [1, 2, 3]]
            ]
    for input in inputs:
        print(getWays(input[0], input[1]))
