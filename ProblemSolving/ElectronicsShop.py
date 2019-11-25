#!/bin/python3

import os
import sys

#
# Complete the getMoneySpent function below.
#


def getMoneySpent(keyboards, drives, b):
      minK = min(keyboards)
      minD = min(drives)
      if (minK + minD) > b:
            return -1

      ret = 0

      extractedKs = [i for i in keyboards if i +
                     minD <= b]  # .sort(reversed=True)

      extractedKs.sort(reverse=True)

      for i in range(len(extractedKs)):
            extractedDs = [j for j in drives if extractedKs[i] + j <= b]
            ans = max(extractedDs)

            if ret < extractedKs[i] + ans <= b:
                  ret = extractedKs[i] + ans

      return ret


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = getMoneySpent(keyboards, drives, b)

    fptr.write(str(moneySpent) + '\n')

    fptr.close()
