import math
import os
import random
import re
import sys

from collections import defaultdict


def splitCoins(val, coins, coinList, ret, dict):
    coins.sort(reverse = True)
    if len(coinList) > 0:
        limit = coinList[-1]
    else:
        limit = val
    if len(coinList) == 0 and val in coins:
        ret += 1

    splitted = [i for i in coins if i <= limit and val - i >= min(coins)]
    for coin in splitted:
        if coin == 1:
            appended = sorted(coinList + [coin] * (val // coin))
            # print(appended)
            ret += 1
            break
        change = val - coin
        # ret += dict[change]

        coinList += [coin]
        if change <= coin and change in coins:
            appended = sorted(coinList + [change])
            # print(appended)
            ret += 1
        ret += splitCoins(change, coins, coinList, 0, dict)
        a = coinList.pop(-1)
    return ret

def getWays(n, c):
    ret = 0
    c.sort(reverse = True)
    stock = defaultdict(int)
    return splitCoins(n, c, [], ret, stock)


if __name__ == '__main__':
    inputs = [
        [18, [49, 9, 40, 17, 46, 24, 42, 26, 43, 41, 35, 1, 47, 28, 20, 38, 2, 44, 32, 22, 18, 45, 25], 18],
        [20, [1,2,5,7,8,10,11,12],103],
        [2, [44, 5, 9, 39, 6, 25, 3, 28, 16, 19, 4, 49, 40, 22, 2, 12, 45, 33, 23, 42, 34, 15, 46, 26, 13, 31, 8], 1],
        [4, [1, 2, 3], 4],
        [10, [2, 5, 3, 6], 5],
        [15, [49, 22, 45, 6, 11, 20, 30, 10, 46, 8, 32, 48, 2, 41, 43, 5, 39, 16, 28, 44, 14, 4, 27, 36], 10],
        [10, [1,2,3,5,6], 24],
        [75, [25, 10, 11, 29, 49, 31, 33, 39, 12, 36, 40, 22, 21, 16, 37, 8, 18, 4, 27, 17, 26, 32, 6, 38, 2, 30, 34], 16694],
        [69, [25, 27, 40, 38, 17, 2, 28, 23, 9, 43, 18, 49, 15, 24, 19, 11, 1, 39, 32, 16, 35, 30, 48, 34, 20, 3, 6, 13, 44], 101768],
        [166, [5, 37, 8, 39, 33, 17, 22, 32, 13, 7, 10, 35, 40, 2, 43, 49, 46, 19, 41, 1, 12, 11, 28], 96190959],
        [219, [36, 10, 42, 7, 50, 1, 49, 24, 37, 12, 34, 13, 39, 18, 8, 29, 19, 43, 5, 44, 28, 23, 35, 26], 168312708],
        [179, [24, 6, 48, 27, 36, 22, 35, 15, 41, 1, 26, 25, 4, 8, 14, 20, 9, 38, 34, 40, 45, 17, 33, 19, 5, 43, 2], 1283414971],
        [250, [8, 47, 13, 24, 25, 31, 32, 35, 3, 19, 40, 48, 1, 4, 17, 38, 22, 30, 33, 15, 44, 46, 36, 9, 20, 49], 3542323427],
        [250, [41, 34, 46, 9, 37, 32, 42, 21, 7, 13, 1, 24, 3, 43, 2, 23, 8, 45, 19, 30, 29, 18, 35, 11], 15685693751],
            ]
    for i in range(len(inputs)):
        result = getWays(inputs[i][0], inputs[i][1])
        isTrue = (result == inputs[i][2])
        print(str(i) + ":" + str(result) + ":" + str(isTrue))
