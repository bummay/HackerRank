#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sherlockAndAnagrams function below.


def sherlockAndAnagrams(s):
    cnt = 0
    length = len(s)
    for l in range(length - 1): #アナグラム文字の長さ
        for m in range(length - l - 1): #アナグラム文字の開始位置
            word = ''.join(sorted(s[m: m + 1 + l]))
            for n in range(length - l - m - 1):
                searched = ''.join(sorted(s[n + m + 1:n + m + 2 + l]))
                if searched == word:
                    cnt += 1

    return cnt

if __name__ == '__main__':
    word_list = ["abba", "abcd", "ifailuhkqq", "kkkk"]
    for word in word_list:
        print(sherlockAndAnagrams(word))
