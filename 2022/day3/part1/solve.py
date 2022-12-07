"""
DAY 3
PART 1
"""
import sys
from functools import reduce
filename = sys.argv[1]
with open(filename, 'r') as file:
    line = file.readline()
    total_priorty = 0
    while line:
        mid_index = int(len(line)/2)
        upper, lower = line[0:mid_index], line[mid_index:]
        intersect = set(upper) & set(lower)
        priority_map = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        priority = reduce(lambda x, y: x + priority_map.index(y) + 1, intersect, 0)
        total_priorty += priority
        line = file.readline()
    print("End of input")
    print("The sum of priorities is = %s" % total_priorty)
