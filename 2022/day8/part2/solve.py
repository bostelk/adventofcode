"""
DAY 8
PART 2
"""
import sys
import re
from functools import reduce
filename = sys.argv[1]
def view_distance(heightmap, x, y, delta_x, delta_y):
    '''returns the number of trees viewable in a given direction'''
    stop = False
    height = heightmap[y][x]
    dist = 0
    while not stop:
        next_x = x + delta_x
        next_y = y + delta_y
        stop_x = next_x >= len(heightmap[0]) or next_x < 0
        stop_y = next_y >= len(heightmap) or next_y < 0
        if stop_x or stop_y:
            break
        next_height = heightmap[next_y][next_x]
        if next_height >= height:
            stop = True
        dist += 1
        x = next_x
        y = next_y
    return dist
def calc_scenic_score(heightmap, x, y):
    dist_1 = view_distance(heightmap, x, y, 1, 0) # look right
    dist_2 = view_distance(heightmap, x, y, -1, 0) # look left
    dist_3 = view_distance(heightmap, x, y, 0, 1) # look down
    dist_4 = view_distance(heightmap, x, y, 0, -1) # look up
    return dist_1 * dist_2 * dist_3 * dist_4
with open(filename, 'r') as file:
    line = file.readline()
    heightmap = []
    while line:
        # Remove newline char.
        if line[len(line) - 1] == '\n':
            line = line[:-1]
        row = [int(c) for c in line]
        heightmap.append(row)
        line = file.readline()
    print("End of input")
    height = len(heightmap)
    width = len(heightmap[0])
    max_scenic_score = 0
    for y in range(0, height):
        for x in range(0, width):
            scenic_score = calc_scenic_score(heightmap, x, y)
            if scenic_score > max_scenic_score:
                max_scenic_score = scenic_score
    print("The maximum scenic score is %s" % max_scenic_score)
