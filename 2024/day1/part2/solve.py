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

    occurance_0 = {}
    for location_id in groups[0]:
        if location_id not in occurance_0:
            occurance_0[location_id] = 0
    for location_id in groups[1]:
        if location_id in occurance_0:
            occurance_0[location_id] += 1

    sum = 0
    for location_id in groups[0]:
        occurance = occurance_0[location_id] if location_id in occurance_0 else 1
        sum += location_id * occurance

    print(sum)
    print("End of input")
