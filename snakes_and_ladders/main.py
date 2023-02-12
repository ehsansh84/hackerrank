#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'quickestWayUp' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY ladders
#  2. 2D_INTEGER_ARRAY snakes
#


def quickestWayUp(l, s):
    ladders = {i[0]: i[1] for i in l}
    snakes = {i[0]: i[1] for i in s}
    board = [False] * 100

    def roll(current):
        # print(current)
        board[current - 1] = True
        ans = 1
        if current == 100:
            return 0
        next_dests = next(current)
        if next_dests == []:
            return -1
        answers = [roll(dest) for dest in next_dests if board[dest - 1] == False]
        if answers == []:
            return -1
        if min(answers) == -1:
            return -1
        return min(answers) + ans if 0 not in answers else ans

    def next(current):
        last = min(current + 7, 101)
        blocks = [i for i in range(current + 1, last)]
        dests = []
        last_block = -1
        for b in blocks:
            if b in ladders:
                # print(f'ladders[b] {ladders[b]} blocks[-1] {blocks[-1]}')
                if ladders[b] > blocks[-1]:
                    dests.append(ladders[b])
            elif b in snakes:

                dests.append(snakes[b])
            else:
                last_block = b
        if last_block != -1:
            dests.append(last_block)
        # print(dests)
        return dests

    return roll(1)


if __name__ == '__main__':
    # with open('data-sample1') as f:
    with open('data-tc2') as f:
        t = int(f.readline().strip())
        for t_itr in range(t):
            # print(1)
            n = int(f.readline().strip())
            ladders = []
            for _ in range(n):
                ladders.append(list(map(int, f.readline().rstrip().split())))
            m = int(f.readline().strip())
            snakes = []
            for _ in range(m):
                snakes.append(list(map(int, f.readline().rstrip().split())))
            result = quickestWayUp(ladders, snakes)
            # print(snakes)
            # print(ladders)
            print(result)
