#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'journeyToMoon' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY astronaut
#

def get_astronaut_groups(astronaut):
    astronaut_groups = []
    for i in astronaut:
        temp = i
        for j in astronaut:
            if i != j:
                if temp.intersection(j):
                    temp = temp | j
        if temp not in astronaut_groups:
            astronaut_groups.append(temp)
    return astronaut_groups


def journeyToMoon(n, astronaut):
    from itertools import product
    l = []
    astronaut_groups = get_astronaut_groups(astronaut)

    all_possible_pairs = product(range(n), range(n))
    valid_pairs = []
    for pair in all_possible_pairs:
        pair_set = set(pair)
        if pair[0] != pair[1]:
            sub = False
            for ag in astronaut_groups:
                if pair_set.issubset(ag):
                    sub = True
                    break
            if not sub:
                if pair_set not in valid_pairs:
                    valid_pairs.append(pair_set)
    return len(valid_pairs)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    p = int(first_multiple_input[1])

    astronaut = []

    for _ in range(p):
        astronaut.append(set(list(map(int, input().rstrip().split()))))

    result = journeyToMoon(n, astronaut)

    fptr.write(str(result) + '\n')

    fptr.close()
