#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#


def pickingNumbers(a):
    minA = min(a)
    maxA = max(a)

    list_cnt = []
    list_seq = []
    for i in range(maxA + 1):
        list_cnt.append(a.count(i))

    for i in range(len(list_cnt) - 1):
        if list_cnt[i] + list_cnt[i + 1] > 0:
            list_seq.append(list_cnt[i] + list_cnt[i + 1])

    return max(list_seq)

if __name__ == '__main__':
    s1 = [4,6,5,3,3,1]
    s2 = [1,2,2,3,1,2]
    s3 = [66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66]
    print(pickingNumbers(s1))
    print(pickingNumbers(s2))
    print(pickingNumbers(s3))