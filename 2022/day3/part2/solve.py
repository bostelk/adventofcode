"""
DAY 3
PART 2
"""
import sys
from functools import reduce
filename = sys.argv[1]
def sum_priority(items):
    priority_map = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return reduce(lambda x, y: x + priority_map.index(y) + 1, items, 0)
with open(filename, 'r') as file:
    line = file.readline()
    total_priorty = 0
    items = None
    elf_index = 0
    while line:
        # New group of eleves.
        if elf_index == 3:
            total_priorty += sum_priority(items)
            items = None
            elf_index = 0
        # Remove newline char.
        if line[len(line) - 1] == '\n':
            line = line[:-1]
        if items is None:
            items = set(line)
        else:
            items &= set(line) # intersection
        elf_index += 1
        line = file.readline()
    total_priorty += sum_priority(items)
    print("End of input")
    print("The sum of priorities is = %s" % total_priorty)
