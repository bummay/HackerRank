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
    ret = 0

    # print(time.time())
    for i in (range(len(q))):
      if q[i] - i > 3:
        ret = -1
        break
      # if i % 1000 == 0:
      #   print(time.time())
      val = q[i]
      numSmaller = len([j for j in q if val > j and q.index(j) > i])
      ret += numSmaller

    if ret >= 0:
        print(ret)
    else:
        print("Too chaotic")

if __name__ == '__main__':
    # t = int(input())

    # for t_itr in range(t):
    #     n = int(input())

    #     q = list(map(int, input().rstrip().split()))

    #     minimumBribes(q)
    minimumBribes([1,2,5,3,7,8,6,4])
