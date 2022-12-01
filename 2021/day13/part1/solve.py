"""
DAY 13
PART 1
"""
import sys
import re
fold_pattern = re.compile('^fold along (x|y)=(\d+)$')
points = set()
folds = []
filename = sys.argv[1]
with open(filename, 'r') as file:
    line = file.readline()
    while line:
        fold_match = fold_pattern.match(line)
        if fold_match:
            folds.append((fold_match.groups()[0], int(fold_match.groups()[1])))
        else:
            parts = line.strip().split(',')
            if len(parts) > 1:
                points.add((int(parts[0]),int(parts[1])))
        line = file.readline()
    print("End of input")
def reflect(axis, on, points):
    reflected = set()
    for point in points:
        if axis == 'x':
            if point[0] >= on:
                new_point = (on - abs(on - point[0]), point[1])
                reflected.add(new_point)
            elif point[0] == on:
                pass # never appear on fold line
            else:
                reflected.add(point)
        elif axis == 'y':
            if point[1] > on:
                new_point = (point[0], on - abs(on - point[1]))
                reflected.add(new_point)
            elif point[1] == on:
                pass # never appear on fold line
            else:
                reflected.add(point)
    return reflected
for i in range(0, len(folds)):
    fold = folds[i]
    points = reflect(fold[0], fold[1], points)
    print("fold along %s=%s. points = %s" % (fold[0], fold[1], len(points)))
    break # stop after first fold.
