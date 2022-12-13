"""
DAY 9
PART 2
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
    num_knots = 9
    knots = []
    for i in range(0, num_knots):
        knots.append(start)
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
            for i in range(0, len(knots)):
                target = (0, 0)
                if i == 0:
                    target = head
                else:
                    target = knots[i - 1]
                knot = knots[i]
                distance_between = dist(target, knot)
                # move knot one step towards the proceeding knot when at least two steps between
                if distance_between >= 2:
                    knot_dir = (0, 0)
                    target_to_knot_delta = sub(target, knot)
                    # knot is diagonal
                    if target_to_knot_delta[0] != 0 and target_to_knot_delta[1] != 0:
                        x = sign(target_to_knot_delta[0])
                        y = sign(target_to_knot_delta[1])
                        knot_dir = (x, y)
                    # knot is directly left, or right
                    elif target_to_knot_delta[0] != 0:
                        x = sign(target_to_knot_delta[0])
                        knot_dir = (x, 0)
                    # knot is directly up, or down
                    elif target_to_knot_delta[1] != 0:
                        y = sign(target_to_knot_delta[1])
                        knot_dir = (0, y)
                    knots[i] = add(knot, knot_dir)
                    if i == len(knots) - 1:
                        visited.add(knots[i])
                print("target %s %s %s %s" % (direction, step, i-1, target))
                print("knot %s %s %s %s" % (direction, step, i, knot))
        line = file.readline()
    print("End of input")
    print(visited)
    print("The number of positions the tail of the rope visits at least once is %s" % len(visited))