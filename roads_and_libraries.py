#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'roadsAndLibraries' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER c_lib
#  3. INTEGER c_road
#  4. 2D_INTEGER_ARRAY cities
#


def get_max_roads_city(cities, city_list):
    counts = {}
    for item in cities:
        for i in item:
            if i in city_list:
                if i in counts:
                    counts[i] += 1
                else:
                    counts[i] = 1
    import operator

    if counts == {} and city_list != []:
        return city_list[0]
    return max(counts.items(), key=operator.itemgetter(1))[0]


def roadsAndLibraries(n, c_lib, c_road, cities):
    all_cities = [i for i in range(1, n + 1)]
    libraries = []
    roads = []
    while all_cities:
        city = get_max_roads_city(cities, all_cities)
        done = False
        for item in cities:
            city_road = item[:]
            if city in item:
                city_road.remove(city)
                second_city = city_road[0]
                if second_city in libraries:
                    if c_road < c_lib:
                        roads.append(set([city, second_city]))
                    else:
                        libraries.append(city)
                    done = True
                    break
        if not done:
            libraries.append(city)
        all_cities.remove(city)

    total_cost = c_lib * len(libraries) + c_road * len(roads)
    return total_cost


    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        c_lib = int(first_multiple_input[2])

        c_road = int(first_multiple_input[3])

        cities = []

        for _ in range(m):
            cities.append(list(map(int, input().rstrip().split())))

        result = roadsAndLibraries(n, c_lib, c_road, cities)

        fptr.write(str(result) + '\n')

    fptr.close()
