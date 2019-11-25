#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
      if s[0].isalpha():
            s = s[0].upper() + s[1:]
      for i in range(len(s)):
            past = s[:i + 1]
            pre = s[i:i + 1]
            present = s[i + 1:i + 2]
            future = s[i + 2:]

            if pre == " " and present.isalpha():
                  s = past + present.upper() + future
      return s

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
