#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the extraLongFactorials function below.
def extraLongFactorials(n):
    ret = 1
    for i in range(n):
        ret *= (i + 1)

    print(ret)

if __name__ == '__main__':
    for i in range(100):
        extraLongFactorials(i + 1)