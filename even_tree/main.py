#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the evenForest function below.
from collections import defaultdict
def evenForest(t_nodes, t_edges, t_from, t_to):
    def dfs(u,parent_node):
        ans=1
        for v in d[u]:
            if v!=parent_node:
                ans+=dfs(v,u)
        count[u-1]=ans
        return ans
    def helper(u,parent_node):
        ans=0
        for v in d[u]:
            if v!=parent_node:
                if count[v-1]%2==0:
                    ans+=1
                ans+=helper(v,u)
        return ans

    count=[1]*t_nodes
    d=defaultdict(list)
    for i in range(len(t_from)):
        d[t_from[i]].append(t_to[i])
        d[t_to[i]].append(t_from[i])
    print(d)
    root=1
    dfs(root,None)
    return helper(root,None)


if __name__ == '__main__':
    with open('data-sample1') as f:
        t_nodes, t_edges = map(int, f.readline().rstrip().split())
        t_from = [0] * t_edges
        t_to = [0] * t_edges
        for i in range(t_edges):
            t_from[i], t_to[i] = map(int, f.readline().rstrip().split())
        res = evenForest(t_nodes, t_edges, t_from, t_to)
        print(res)


    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # t_nodes, t_edges = map(int, input().rstrip().split())
    # t_from = [0] * t_edges
    # t_to = [0] * t_edges
    # for i in range(t_edges):
    #     t_from[i], t_to[i] = map(int, input().rstrip().split())
    # res = evenForest(t_nodes, t_edges, t_from, t_to)
    # fptr.write(str(res) + '\n')
    # fptr.close()
