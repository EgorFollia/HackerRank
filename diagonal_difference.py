#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the diagonalDifference function below.
def diagonalDifference(arr):
    normal_diag = reverse_diag = 0
    for i in range(len(arr)):
	    normal_diag += arr[i][i]
	    reverse_diag += arr[i][(n - 1) - i]
    return abs(normal_diag - reverse_diag)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
