#!/bin/python3

import math
import os
import random
import re
import sys

## Input
# 5
# 1 1 0 -1 -1

# Complete the plusMinus function below.
def plusMinus(arr):
    # Sample Input:
    # arr = [1, 1, 0, -1, .1]
    # Sample Output:
    # 0.40000
    # 0.40000
    # 0.20000
    
    # p = positive
    # z = zero
    # n = negative

    p = z = n = 0

    for i in range(len(arr)):
        if (arr[i] == 0):
            z += 1
        elif (arr[i] > 0):
            p += 1
        else:
            n += 1 
    print("{:.6f}".format(p/len(arr)))
    print("{:.6f}".format(n/len(arr)))
    print("{:.6f}".format(z/len(arr)))
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
