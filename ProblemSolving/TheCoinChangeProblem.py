import math
import os
import random
import re
import sys

from collections import defaultdict


def splitCoins(val, coins, coinList, ret, patternSet):
    coins.sort(reverse = True)
    if len(coinList) > 0:
        limit = coinList[-1]
    else:
        limit = val

    splitted = [i for i in coins if i <= limit and val - i >= min(coins)]
    for coin in splitted:
        if val % coin == 0:
            appended = sorted(coinList + [coin] * (val // coin))
            if appended not in ret:
                ret.append(appended)
            if coin == 1:
                break
        change = val - coin
        if change not in patternSet:
            isPatternSet = True
        if change < min(coins):
            break
        else:
            coinList += [coin]

            if change in coins:
                appended = sorted(coinList + [change])
                if appended not in ret:
                    ret.append(appended)
            splitCoins(change, coins, coinList, ret, patternSet)
        a = coinList.pop(-1)
    return ret

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
    combination = defaultdict(set)
    getPatterns = splitCoins(n, c, [], [], combination)

    return len(getPatterns)

if __name__ == '__main__':
    inputs = [
        [10, [1,2,3,5,6], 13],
        [69, [25, 27, 40, 38, 17, 2, 28, 23, 9, 43, 18, 49, 15, 24, 19, 11, 1, 39, 32, 16, 35, 30, 48, 34, 20, 3, 6, 13, 44], 101768],
        [4, [1, 2, 3], 4],
        [10, [2, 5, 3, 6], 5],
        [166, [5, 37, 8, 39, 33, 17, 22, 32, 13, 7, 10, 35, 40, 2, 43, 49, 46, 19, 41, 1, 12, 11, 28], 96190959],
        [75, [25, 10, 11, 29, 49, 31, 33, 39, 12, 36, 40, 22, 21, 16, 37, 8, 18, 4, 27, 17, 26, 32, 6, 38, 2, 30, 34], 16694],
        [219, [36, 10, 42, 7, 50, 1, 49, 24, 37, 12, 34, 13, 39, 18, 8, 29, 19, 43, 5, 44, 28, 23, 35, 26], 168312708],
        [18, [49, 9, 40, 17, 46, 24, 42, 26, 43, 41, 35, 1, 47, 28, 20, 38, 2, 44, 32, 22, 18, 45, 25], 18],
        [15, [49, 22, 45, 6, 11, 20, 30, 10, 46, 8, 32, 48, 2, 41, 43, 5, 39, 16, 28, 44, 14, 4, 27, 36], 10],
        [2, [44, 5, 9, 39, 6, 25, 3, 28, 16, 19, 4, 49, 40, 22, 2, 12, 45, 33, 23, 42, 34, 15, 46, 26, 13, 31, 8], 1],
            ]
    for i in range(len(inputs)):
        result = getWays(inputs[i][0], inputs[i][1])
        isTrue = (result == inputs[i][2])
        print(str(i) + ":" + str(result) + ":" + str(isTrue))
