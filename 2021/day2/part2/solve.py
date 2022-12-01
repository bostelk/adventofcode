"""
DAY 2
PART 2
"""
import sys
filename = sys.argv[1]
with open(filename, 'r') as file:
    line = file.readline()
    depth = 0
    horizontal = 0
    aim = 0
    while line:
        parts = line.split(" ")
        if parts[0] == "forward":
            horizontal += int(parts[1])
            depth += aim * int(parts[1])
        elif parts[0] == "up":
            aim -= int(parts[1])
        elif parts[0] == "down":
            aim += int(parts[1])
        line = file.readline()
    print("End of input")
    product = horizontal * depth
    print("%s * %s = %s" % (horizontal, depth, product))
