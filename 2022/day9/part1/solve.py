"""
DAY 9
PART 1
"""
import sys
import re
from functools import reduce
filename = sys.argv[1]
def parse_direction(char):
    '''returns a direction from a  charater'''
    map = {
        'R': (1, 0),
        'L': (-1, 0),
        'U': (0, 1),
        'D': (0, -1)
    }
    return map[char]
def add(a, b):
    return (a[0] + b[0], a[1] + b[1])
def sub(a, b):
    return (a[0] - b[0], a[1] - b[1])
def dist(a, b):
    return max(abs(a[0] - b[0]), abs(a[1] - b[1]))
def sign(x):
    if x > 0:
        return 1
    if x < 0:
        return -1
    if x == 0:
        return 0
with open(filename, 'r') as file:
    line = file.readline()
    start = (0, 0)
    # head and tail start overlapped
    head = start
    tail = start
    visited = set()
    visited.add(start)
    while line:
        # Remove newline char.
        if line[len(line) - 1] == '\n':
            line = line[:-1]
        print(line)
        direction, steps = line.split(" ")
        steps = int(steps)
        for step in range(0, steps):
            head_dir = parse_direction(direction)
            head = add(head, head_dir)
            distance_between = dist(head, tail)
            # move tail one step towards head when at least two steps between
            if distance_between >= 2:
                tail_dir = (0, 0)
                head_to_tail_delta = sub(head, tail)
                # head is diagonal
                if head_to_tail_delta[0] != 0 and head_to_tail_delta[1] != 0:
                    x = sign(head_to_tail_delta[0])
                    y = sign(head_to_tail_delta[1])
                    tail_dir = (x, y)
                # head is directly left, or right
                elif head_to_tail_delta[0] != 0:
                    x = sign(head_to_tail_delta[0])
                    tail_dir = (x, 0)
                # head is directly up, or down
                elif head_to_tail_delta[1] != 0:
                    y = sign(head_to_tail_delta[1])
                    tail_dir = (0, y)
                tail = add(tail, tail_dir)
                visited.add(tail)
            print("head %s %s %s" % (direction, step, head))
            print("tail %s %s %s" % (direction, step, tail))
        line = file.readline()
    print("End of input")
    print(visited)
    print("The number of positions the tail of the rope visits at least once is %s" % len(visited))