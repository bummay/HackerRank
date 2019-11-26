#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    distinct_scores = list(set(scores))
    distinct_scores.sort(reverse = True)
    ret = []
    for alice_score in alice:
        position = sum(x > alice_score for x in distinct_scores) + 1
        ret.append(position)

    return ret

if __name__ == '__main__':
    scores = [[100,100,50,40,40,20,10],[100,90,90,80,75,60]]
    alice = [[5,25,50,120],[50,65,77,90,102]]
    for i in range(2):
        print(climbingLeaderboard(scores[i], alice[i]))
