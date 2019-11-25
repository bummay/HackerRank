#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())
    yes = "Weird"
    no = "Not Weird"

    if (n % 2 != 0) :
      print (yes)
    elif (2 <= n <= 5) :
      print(no)
    elif (6 <= n <= 20) :
      print(yes)
    elif (n > 20) :
      print(no)
