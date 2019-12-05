import math
import os
import random
import re
import sys

from collections import defaultdict


def getCombination2(n, arr):
    arr.sort()
    combination = defaultdict(list)
    for i in range(n + 1):
        if i in (arr):
            combination[i].append([i])
        else:
            combination[i] = []

        for j in range(1, math.floor(i / 2) + 1):
            k = i - j
            lenJ = len(combination[j])
            lenK = len(combination[k])
            sumLength = lenJ * lenK
            if sumLength > 0:
                cntJ, cntK = 0, 0
                if combination[j][0] == list([j]):
                    cntJ += 1
                if len(combination[j]) - cntJ == 1:
                    cntJ += 1

                if combination[k][0] == list([k]):
                    cntK += 1
                if len(combination[k]) - cntK == 1:
                    cntK += 1

                for p in range(cntJ):
                    for q in range(cntK):
                        toAppend = sorted(
                            combination[j][p] + combination[k][q])
                        if toAppend not in combination[i]:
                            combination[i].append(toAppend)

    return combination

def getCombination(n, arr):
    arr.sort()
    combination = defaultdict(list)
    for i in range(n + 1):
        if i in arr:
            for j in range(1, math.floor(n // i) + 1):
                idx = i * j
                combination[idx].append([i] * j)

            for arg in arr:
                if arg > i:
                    combination[i + arg].append(sorted([i] + [arg]))

                # for k in range(n):
                #     for arg in combination[k]:
                #         toAppend = sorted(list([i]) + arg)
                #         sumArg = sum(arg) + i
                #         if sumArg <= n and toAppend not in combination[sumArg]:
                #             combination[sumArg].append(toAppend)
            j = 0
        else:
            if len(combination[i]) == 0:
                combination[i].append([])





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
        [166, [5, 37, 8, 39, 33, 17, 22, 32, 13, 7, 10, 35, 40, 2, 43, 49, 46, 19, 41, 1, 12, 11, 28], 96190959],
        [75, [25, 10, 11, 29, 49, 31, 33, 39, 12, 36, 40, 22, 21, 16, 37, 8, 18, 4, 27, 17, 26, 32, 6, 38, 2, 30, 34], 16694],
        [219, [36, 10, 42, 7, 50, 1, 49, 24, 37, 12, 34, 13, 39, 18, 8, 29, 19, 43, 5, 44, 28, 23, 35, 26], 168312708],
        [69, [25, 27, 40, 38, 17, 2, 28, 23, 9, 43, 18, 49, 15, 24, 19, 11, 1, 39, 32, 16, 35, 30, 48, 34, 20, 3, 6, 13, 44], 101768],
        [18, [49, 9, 40, 17, 46, 24, 42, 26, 43, 41, 35, 1, 47, 28, 20, 38, 2, 44, 32, 22, 18, 45, 25], 18],
        [4, [1, 2, 3], 4],
        [10, [2, 5, 3, 6], 5],
        [15, [49, 22, 45, 6, 11, 20, 30, 10, 46, 8, 32, 48, 2, 41, 43, 5, 39, 16, 28, 44, 14, 4, 27, 36], 10],
        [2, [44, 5, 9, 39, 6, 25, 3, 28, 16, 19, 4, 49, 40, 22, 2, 12, 45, 33, 23, 42, 34, 15, 46, 26, 13, 31, 8], 1],
            ]
    for i in range(len(inputs)):
        result = getWays(inputs[i][0], inputs[i][1])
        isTrue = (result == inputs[i][2])
        print(str(i) + ":" + str(result) + ":" + str(isTrue))
