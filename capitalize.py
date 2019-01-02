#!/bin/python3

import math
import os
import random
import re
import sys

def solve(s):
    s = s.capitalize()

    for i in range(len(s)):
        if (s[i] == ' ' and isinstance(s[i + 1], str)):
            s = s[:i + 1] + s[i + 1:i + 2].capitalize() + s[i + 2:]

    return s

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
