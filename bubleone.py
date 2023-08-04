#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    num_swaps = 0;
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if a[i] > a[j]:
                temp = a[i]
                a[i] = a[j]
                a[j] = temp
                num_swaps += 1
    print("Array is sorted in", num_swaps,"swaps.")
    print("First Element:", a[0])
    print("Last Element:",a[len(a)-1])
if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
