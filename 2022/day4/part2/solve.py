"""
DAY 4
PART 2
"""
import sys
from functools import reduce
filename = sys.argv[1]
class Intervals:
    def __init__(self):
        self.items = []
    def insert(self, value):
        print("insert %s" % value)
        for i in self.items:
            # 5-7,7-9
            # 2-8,3-7
            if (value[0] >= i[0] and value[0] <= i[1]) or (value[1] >= i[0] and value[1] <= i[1]):
                print("overlap by %s" % i)
                return #
            elif (i[0] >= value[0] and i[0] <= value[1]) or (i[1] >= value[0] and i[1] <= value[1]):
                print("overlap by %s" % value)
                return #
        self.items.append(value)
        print("result %s" % self.items)
    def size(self):
        return len(self.items)
with open(filename, 'r') as file:
    line = file.readline()
    fully_cover = 0
    while line:
        intervals = Intervals()
        # Remove newline char.
        if line[len(line) - 1] == '\n':
            line = line[:-1]
        elves = line.split(",")
        for e in elves:
            start, end = e.split("-")
            interval = [int(start), int(end)]
            intervals.insert(interval)
        if intervals.size() == 1:
            fully_cover += 1
        line = file.readline()
    print("End of input")
    print("The number of pairs where assignment is fully covered: %s" % fully_cover)
