#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.


def minimumBribes(q):
    ret = 0
    for i in (range(len(q))):
        # value = i のインデックス(=pos)を取得
        pos = q.index(i + 1)
        gap = i - pos
        # posとvalue - 1の差 > 2 なら"Too chaotic"
        if gap > 2:
          ret = -1
          print("Too chaotic")
          break
        # posとvalue - 1の差が 1 or 2ならlistを入れ替え & retに加算
        elif gap == 2:
          ret += gap
          q[pos], q[pos+ 1],q[pos + 2] = q[pos + 1], q[pos + 2], q[pos]
        elif gap == 1:
          ret += gap
          q[pos], q[pos + 1] = q[pos + 1], q[pos]
    if ret >= 0:
        print(ret)

if __name__ == '__main__':
    # t = int(input())

    # for t_itr in range(t):
    #     n = int(input())

    #     q = list(map(int, input().rstrip().split()))

    #     minimumBribes(q)
    minimumBribes([1,2,5,3,7,8,6,4])
