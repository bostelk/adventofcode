"""
DAY 6
PART 2
"""
import sys
fish_bucket = [0] * 9
filename = sys.argv[1]
with open(filename, 'r') as file:
    line = file.readline()
    while line:
        fish = map(lambda x: int(x), line.split(','))
        for i in range(0,len(fish)):
            fish_bucket[fish[i]] +=1
        line = file.readline()
    print("End of input")
print("Initial state: %s" % fish)
num_days = 256
for i in range(0, num_days):
    new_fish_bucket = [0] * 9
    new_fish_bucket[6] = fish_bucket[0]
    new_fish_bucket[8] = fish_bucket[0]
    for j in reversed(range(1, len(fish_bucket))):
        k = j-1 if j > 0 else 8
        new_fish_bucket[k] += fish_bucket[j]
    fish_bucket = new_fish_bucket
    print("After %s days: %s" % (i+1, fish_bucket))
print("After %s days there are %s fish." % (i+1, sum(fish_bucket)))

