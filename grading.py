#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def next_multiple(num):
    for i in range(1,6):
        if (num + i) % 5 == 0:
            return num + i


def gradingStudents(grades):
    # Write your code here
    result = []
    for grade in grades:
        if (grade < 38):
            result.append(grade)
        else:
            next_m = next_multiple(grade)
            if (next_m - grade) < 3:
                result.append(next_m)
            else:
                result.append(grade)

    return result
if __name__ == '__main__':
    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    print('\n'.join(map(str, result)))
