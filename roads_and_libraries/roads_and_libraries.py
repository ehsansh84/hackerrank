#!/bin/python3

import math
import os
import random
import re
import sys
import time
import operator


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


def city_road_count(cities, city_list):
    counts = {}

    for item in cities:
        for i in item:
            if i in city_list:
                counts[i] = 1 if i not in counts else counts[i] + 1

    x = {city: 0 for city in city_list if city not in counts}
    counts = {**counts, **x}
    print(f'city_road_couns: {counts}')
    return counts


def get_city_with_most_roads(city_roads):
    return max(city_roads.items(), key=operator.itemgetter(1))[0]


def roadsAndLibraries(n, c_lib, c_road, cities):
    # print(f'n is: {n}')
    all_cities = {i for i in range(1, n + 1)}
    print(f'All cities: {all_cities}')
    libraries = []
    roads = []
    c_r_count = city_road_count(cities, all_cities)
    # print(c_r_count)
    while all_cities:
        # print(f'cities: {cities}')
        print(f'All cities {all_cities}')

        city = get_city_with_most_roads(c_r_count)
        print(f'{city} is the biggest from {c_r_count}')
        del c_r_count[city]
        # if c_r_count == {} and len(all_cities) != 0:
        #     city = all_cities.pop()
        # else:
        #     city = max(c_r_count.items(), key=operator.itemgetter(1))[0]

        print(f'MAX CITY {city}')
        done = False
        for item in cities:
            print(f'item is: {item}')
            print(city)
            city_road = set.copy(item)
            # print(id(city_road))
            # print(id(item))
            if city in item:
                print(city_road)
                city_road.remove(city)
                print(city_road)
                second_city = city_road.pop()
                if second_city in libraries:
                    if c_road < c_lib:
                        road = {city, second_city}
                        if road not in roads:
                            roads.append(road)
                    else:
                        libraries.append(city)
                    done = True
                    break
        if not done:
            libraries.append(city)
        print(f'fuck {all_cities}')
        print(f'fuck {city}')
        all_cities.remove(city)

    print('=======')
    print(libraries)
    print(roads)
    total_cost = c_lib * len(libraries) + c_road * len(roads)
    return total_cost


if __name__ == '__main__':
    start = time.time_ns()
    with open('data', 'r') as f:
        q = int(f.readline().strip())

        for q_itr in range(q):
            first_multiple_input = f.readline().rstrip().split()

            n = int(first_multiple_input[0])

            m = int(first_multiple_input[1])

            c_lib = int(first_multiple_input[2])

            c_road = int(first_multiple_input[3])

            cities = []

            for _ in range(m):
                cities.append(set(list(map(int, f.readline().rstrip().split()))))
            result = roadsAndLibraries(n, c_lib, c_road, cities)
            print(result)
            # break
    end = time.time_ns()
    print(f'Time taken: {(end-start) / 1000000} ms')






# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#     q = int(input().strip())
#
#     for q_itr in range(q):
#         first_multiple_input = input().rstrip().split()
#
#         n = int(first_multiple_input[0])
#
#         m = int(first_multiple_input[1])
#
#         c_lib = int(first_multiple_input[2])
#
#         c_road = int(first_multiple_input[3])
#
#         cities = []
#
#         for _ in range(m):
#             cities.append(set(list(map(int, input().rstrip().split()))))
#
#         result = roadsAndLibraries(n, c_lib, c_road, cities)
#
#         fptr.write(str(result) + '\n')
#
#     fptr.close()
