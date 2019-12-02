#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the findDigits function below.


def findDigits(n):
    ret = 0
    numToStr = str(n)
    for i in range(len(numToStr)):
        digit = int(numToStr[i: i+1])
        if digit > 0 and n % digit == 0:
            ret += 1

    return ret


if __name__ == '__main__':
    lst = [12, 1012, 29]
    for num in lst:
        result = findDigits(num)
        print(result)