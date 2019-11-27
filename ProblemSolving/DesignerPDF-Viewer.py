#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the designerPdfViewer function below.


def designerPdfViewer(h, word):
    list_alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                    "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    list_height = []
    for letter in word:
        idx = list_alphabet.index(letter)
        list_height.append(h[idx])

    return max(list_height) * len(word)


if __name__ == '__main__':
    h = [
        [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
        [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 7]
        ]
    word = ["abc", "zaba"]
    for i in range(2):
        result = designerPdfViewer(h[i], word[i])
        print(result)

