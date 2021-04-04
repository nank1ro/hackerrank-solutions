#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#
# Sample Input
# 3
# 11 2 4
# 4 5 6
# 10 8 -12
# Sample Output
# 15

def diagonalDifference(arr):
    # Write your code here
    # [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
    d1 = d2 = 0

    for i in range(len(arr)):
        print(f'd1: {arr[i][i]}')
        print(f'd2: {arr[len(arr)-i-1][i]}')
        d1 += arr[i][i]
        d2 += arr[len(arr)-i-1][i]
    return abs(d1 - d2)

if __name__ == '__main__':

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    print(str(result) + '\n')
