#!/bin/python3

import math
import os
import random
import re
import sys

from collections import deque
import time
# Complete the minimumBribes function below.


def minimumBribes(q):
    moves = 0
    for pos, val in enumerate(q):
        if(val - 1) - pos > 2:
            moves = -1
            break
        # 本来の位置or後ろにいる場合、一つ後ろの人が2回bribeした可能性がある
        # →本来の一つ前～今の位置の間に自分より後ろにいた人をカウントする。
        for j in range(max(0,val -2),pos):
            if q[j] > val:
                moves += 1

    if moves >= 0:
        print(moves)
    else:
        print("Too chaotic")

if __name__ == '__main__':
    # t = int(input())

    # for t_itr in range(t):
    #     n = int(input())

    #     q = list(map(int, input().rstrip().split()))

    #     minimumBribes(q)
    minimumBribes([2,5,1,3,4])
