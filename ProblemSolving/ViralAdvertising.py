#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the viralAdvertising function below.


def viralAdvertising(n):
    start = 5
    liked = start // 2
    cnt = liked
    for i in range(n - 1):
        shared = liked * 3
        liked += liked // 2
        cnt += liked
    return cnt


if __name__ == '__main__':
    lst = [3]

    for i in range(len(lst)):
        result = viralAdvertising(lst[i])
        print(result)
