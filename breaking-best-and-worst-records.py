#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    best = worst = scores[0]

    result = [0, 0]

    for score in scores:
        if (score > best):
            best = score
            result[0] += 1
        elif (score < worst):
            worst = score
            result[1] += 1

    return result

if __name__ == '__main__':
    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    print(' '.join(map(str, result)))
