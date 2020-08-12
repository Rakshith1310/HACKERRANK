#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    count=0
    previous_h=0
    height=0
    for i in range(0,len(s)):
        if s[i] is 'U':
            height+=1
        elif s[i] is 'D':
            height-=1
        if (height==0) and (previous_h<0):
            count+=1
        previous_h=height
    return(count)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
