#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    k = 1
    if (n > 0):
        for i in range(n - 1):
            print((' ' * (n - 2)), '#' * k)
            n -= 1
            k += 1
    print('#' * k)
    

if __name__ == '__main__':
    n = int(input())

    staircase(n)
