"""
DAY 8
PART 1
"""
import sys
import re
from functools import reduce
filename = sys.argv[1]
def visible(heightmap, visiblemap, x, y, delta_x, delta_y):
    '''scan in a given direction and count visible trees'''
    stop = False
    visiblemap[y][x] = 1
    line_of_sight = [heightmap[y][x]] # perimeter is visible
    vis_x = -1
    vis_y = -1
    while not stop:
        next_x = x + delta_x
        next_y = y + delta_y
        stop_x = next_x >= len(heightmap[0]) - 1 or next_x < 1
        stop_y = next_y >= len(heightmap) - 1 or next_y < 1
        if stop_x or stop_y:  # stop outside interior
            break
        next_height = heightmap[next_y][next_x]
        visible = True
        for height in line_of_sight:
            if height >= next_height:
                visible = False
        if visible:
            vis_x = next_x
            vis_y = next_y
            visiblemap[vis_y][vis_x] = 1
        line_of_sight.append(next_height)
        x = next_x
        y = next_y
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
    visiblemap = [[0] * width for i in range(height)]
    #  # perimeter is visible (corners are not scanned)
    visiblemap[0][0] = 1
    visiblemap[0][width-1] = 1
    visiblemap[height-1][0] = 1
    visiblemap[height-1][width-1] = 1
    # interior tree visiblity;
    for y in range(1, len(heightmap) - 1):
        visible(heightmap, visiblemap, 0, y, 1, 0) # left edge to right
        visible(heightmap, visiblemap, len(heightmap[0]) - 1, y, -1, 0) # right edge to left
    # interior tree visiblity;
    for x in range(1, len(heightmap[0]) - 1):
        visible(heightmap, visiblemap, x, 0, 0, 1) # top edge to bottom
        visible(heightmap, visiblemap, x, len(heightmap) - 1, 0, -1) # bottom edge to top
    total = 0
    for y in range(0, len(visiblemap)):
        row = ""
        for x in range(0, len(visiblemap[0])):
            row += str(visiblemap[y][x])
            if (visiblemap[y][x]) == 1:
                total += 1
        print(row)
    print("The number of trees visible is %s" % total)
