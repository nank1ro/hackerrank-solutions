#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'changeBits' function below.
#
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#  3. STRING_ARRAY queries
#

def changeBits(a, b, queries):
    # Write your code here
    result = ''
    for query in queries:
        query_data = query.split(' ')
        if (query_data[0] == 'set_a'):
            index = len(a) - 1 - int(query_data[1])
            a = a[:index] + query_data[2] + a[index+1:]
        elif (query_data[0] == 'set_b'):
            index = len(b) - 1 - int(query_data[1])
            b = b[:index] + query_data[2] + a[index+1:]
        else:
            int_sum_value = int(a, 2) + int(b, 2)
            binary_sum = bin(int_sum_value)[2:]
            index = len(binary_sum) - 1 - int(query_data[1])
            if (index < 0):
                result += '0'
            else: 
                result += str(binary_sum[index])
    print(result)
        

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    ab_size = int(first_multiple_input[0])

    queries_size = int(first_multiple_input[1])

    a = input()

    b = input()

    queries = []

    for _ in range(queries_size):
        queries_item = input()
        queries.append(queries_item)

    changeBits(a, b, queries)

# 
# Let a and b be binary numbers of length n (MSB to the left). The following commands may be performed:
# 
# set_a idx x: Set  to , where  and  is  least significant bit of .
# set_b idx x: Set  to , where  and  is  least significant bit of .
# get_c idx: Print , where  and .
# Given , and a list of commands, create a string made of the results of each  call, the only command that produces output. For example,  and  so the length of the numbers is . Print an answer string that contains the results of all commands on one line. A series of commands and their results follow:
# 
# Starting
# ans = '' (empty string)
# a b
# 000 111
# set_a 1 1
# 010 111
# set_b 0 1
# 010 111
# get_c 3
# a + b = 1001
# ans = '1'
# 010 111
# get_c 4
# a + b = 01001
# ans = '10'
# 
# Note: When the command is get_c 4,  had to be padded to the left with a  to be long enough to return a value.
# 
# Function Description
# 
# Complete the changeBits function in the editor below. For each get_c command, it should print either a 0 or a 1 without a newline until all commands have been processed. At that point, add a newline.
# 
# changeBits has the following parameters:
# - a, b: two integers represented as binary strings
# - queries[queries[0]-queries[n-1]]: an array of query strings in the format described
# 
# Input Format
# 
# The first line of input contains two space-separated integers,  and , the length of the binary representations of  and , and the number of commands, respectively.
# The second and third lines each contain a string representation of  and .
# The following  lines each contain a command string  as described above.
# 
# Constraints
# 
# 
# 
# Output Format
# 
# For each query of the type , output a single digit 0 or 1. Output must be placed on a single line.
# 
# Sample Input 0
# 
# 5 5
# 00000
# 11111
# set_a 0 1
# get_c 5
# get_c 1
# set_b 2 0
# get_c 5
# Sample Output 0
# 
# 100
# Explanation 0
# 
# set_a 0 1 sets 00000 to 00001
# C = A + B = 00001 + 11111 = 100000, so get_c[5] = 1
# from the above computation get_c[1] = 0
# set_b 2 0 sets 11111 to 11011
# C = A + B = 00001 + 11011 = 011100, so get_c[5] = 0
# The output is hence concatenation of 1, 0 and 0 = 100