"""
DAY 7
PART 2
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
def find_fuel_cost(crabs, p):
    cost = lambda x: sum(range(1, abs(x - p) + 1))
    return sum(map(cost, crabs))
min_fuel_cost = float('inf')
for i in range(0, max(crabs)):
    fuel_cost = find_fuel_cost(crabs, i)
    min_fuel_cost = min(fuel_cost, min_fuel_cost)
print("Total fuel cost = %s" % min_fuel_cost)
