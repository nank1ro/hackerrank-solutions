#!/bin/python3

import math
import os
import random
import re
import sys

def increment_if_included(s, t, value):
    return 1 if (value >= s and value <= t) else 0

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    total_apples = 0
    total_oranges = 0

    for apple in apples:
        total_apples += increment_if_included(s, t, apple + a)

    for orange in oranges:
        total_oranges += increment_if_included(s, t, orange + b)

    print(f'{total_apples}\n{total_oranges}')

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
