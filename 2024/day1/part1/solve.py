"""
DAY 1
PART 1
"""
import sys
from functools import reduce
import operator

filename = sys.argv[1]

def parse_line(line):
    parts = line.split()
    if len(parts) == 2:
        return [int(parts[0]), int(parts[1])]
    return [None, None]

with open(filename, 'r') as file:
    line = file.readline()

    groups = [[],[]]

    while line:
        # Remove newline char.
        if line[len(line) - 1] == '\n':
            line = line[:-1]

        location_ids = parse_line(line)
        groups[0].append(location_ids[0])
        groups[1].append(location_ids[1])

        line = file.readline()

    groups[0] = sorted(groups[0])
    groups[1] = sorted(groups[1])

    output = []
    for pair in zip(groups[0], groups[1]):
        output.append(abs(pair[0] - pair[1]))

    sum = reduce(operator.add, output, 0)
    print(sum)
    print("End of input")
