#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the appendAndDelete function below.


def appendAndDelete(s, t, k):

    # 1. tと前方一致するまでsの末尾をdelete
    # 2. tと完全一致するまでsの末尾にappend
    # 1と2の合計がkと一致すればTrue。kより小さければFalse。
    # 1と2の合計 > k の場合は、次のどちらかで回数を稼げればOK
    #   a. sをすべてdelete -> ブランクになってもdelete -> tになるまでappend
    #   b. 「sの末尾をdelete -> sの末尾にappend」の繰り返し

    ret = False

    matched = 0
    while s[matched] == t[matched]:
        matched += 1
        if matched == min(len(s), len(t)):
            break

    deleted = len(s) - matched
    appended = len(t) - matched
    operation = deleted + appended
    gap = k - operation

    if gap == 0:
        ret = True
    elif gap < 0:
        ret = False
    elif gap % 2 == 0 or gap >= 2 * matched:
        ret = True
    else:
        ret = False

    if ret:
        return 'Yes'
    else:
        return 'No'

if __name__ == '__main__':
    list_s = ['hackerhappy', 'aba', 'ashley', 'qwerasdf',
              'asdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcv']
    list_t = ['hackerrank', 'aba', 'ash', 'qwerbsdf',
              'bsdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcv']
    list_k = [9, 7, 2, 6, 100]

    for i in range(len(list_s)):
        print(appendAndDelete(list_s[i], list_t[i], list_k[i]))
