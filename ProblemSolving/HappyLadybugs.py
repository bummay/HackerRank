#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the happyLadybugs function below.
def isLadybugsAreHappy(str_list):
    for i in range(len(str_list)):
        if i == 0:
            prev = ''
        else:
            prev = str_list[i - 1]

        if i == len(str_list) - 1:
            next = ''
        else:
            next = str_list[i + 1]

        if str_list[i] != prev and str_list[i] != next:
            return False
    return True

def happyLadybugs(b):

    # '_'の数が0
    #   → すべての文字列が一つ前or一つ後のどちらかと一致したらTrueしなかったらFalse
    # '_'の数 > 0
    #   → すべて'_'ならTrue
    #       → '_'以外の文字列をソートしてもう一度前後の文字列を比較。
    emptyCells = b.count('_')
    if emptyCells == len(b):
        return 'YES'

    if emptyCells > 0:
        b = b.replace('_', '')
        str_list = list(b)
        str_list.sort()
    else:
        str_list = list(b)

    if isLadybugsAreHappy(str_list):
        return 'YES'
    else:
        return 'NO'


if __name__ == '__main__':
    inputs = [
        'RBY_YBR',
        'X_Y__X',
        '__',
        'B_RRBR',
        'AABBC',
        'AABBC_C',
        '_',
        'DD__FQ_QQF',
        'AABCBC',
        'BBAACC'
        ]

    for word in inputs:
        result = happyLadybugs(word)
        print(result)
