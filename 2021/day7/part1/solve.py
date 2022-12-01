"""
DAY 7
PART 1
"""
import sys
crabs = []
filename = sys.argv[1]
with open(filename, 'r') as file:
    line = file.readline()
    while line:
        crabs = map(lambda x: int(x), line.split(','))
        line = file.readline()
    print("End of input")
def find_mode(x):
    x = sorted(x)
    middle = len(x)/2
    return x[middle]
def find_fuel_cost(crabs, p):
    diff = lambda x: abs(x -p)
    return sum(map(diff, crabs))
mode = find_mode(crabs)
min_fuel_cost = find_fuel_cost(crabs, mode)
for i in range(0, len(crabs)):
    print("Move from %s to %s: %s fuel" % (crabs[i], mode, abs(crabs[i] - mode)))
print("Total fuel cost = %s" % min_fuel_cost)
