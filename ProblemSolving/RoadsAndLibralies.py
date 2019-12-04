#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited

def roadsAndLibraries(n, c_lib, c_road, cities):
    total_cost = 0
    if c_road >= c_lib or len(cities) == 0:
        return n*c_lib
    else:  # here be real shits
        city_graph = defaultdict(set)

        connected_cities = set()  # might make this into a set
        for i in cities:
            city_graph[i[0]].add(i[1])
            city_graph[i[1]].add(i[0])
            connected_cities.add(i[0])
            connected_cities.add(i[1])

        isolated_cities = set([i+1 for i in range(n)]) - connected_cities

        while len(connected_cities) > 0:  # have list of all n cities, use dfs, remove cities travelled, add to total sum, then keep doint till empty

            temp = connected_cities.pop()
            component = dfs(city_graph, temp)
            total_cost += (len(component)-1)*c_road + c_lib
            connected_cities -= component

        return total_cost + len(isolated_cities)*c_lib


if __name__ == '__main__':
    inputs = [
                [5, 6, 1,
                 [
                     [1, 2],
                     [1, 3],
                     [1, 4]
                 ]
                ],
                [3, 2, 1,
                 [
                     [1, 2],
                     [3, 1],
                     [2, 3]
                 ]
                ],
                [7, 2, 1,
                    [
                     [1, 3],
                     [3, 4],
                     [2, 4],
                     [1, 2],
                     [2, 3],
                     [3, 5],
                     [6, 7]
                    ]
                 ]
    ]
    for input in inputs:
        print(roadsAndLibraries(input[0], input[1], input[2], input[3]))
