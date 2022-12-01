"""
DAY 6
PART 1
"""
import sys
fish = None
filename = sys.argv[1]
with open(filename, 'r') as file:
    line = file.readline()
    while line:
        fish = map(lambda x: int(x), line.split(','))
        line = file.readline()
    print("End of input")
print("Initial state: %s" % fish)
num_days = 80
for i in range(0, num_days):
    for j in range(0, len(fish)):
        fish[j] -= 1
        # spawn new fish.
        if fish[j] < 0:
            fish[j] = 6
            fish.append(8)
    print("After %s days: %s" % (i+1, fish))
print("After %s days there are %s fish." % (i+1, len(fish)))

