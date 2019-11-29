#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the angryProfessor function below.


def angryProfessor(k, a):
    a.sort()
    i = 0
    while i < len(a):
        if a[i] < 1:
            i += 1
        else:
            break

    if i < k:
        return "YES"
    else:
        return "NO"



if __name__ == '__main__':
    lst = [[3,[-1,-3,4,2]],[2,[0,-1,2,1]]]

    for i in range(len(lst)):
        result = angryProfessor(lst[i][0],lst[i][1])
        print(result)
