"""
DAY 1
PART 1
"""
import sys
from functools import reduce
filename = sys.argv[1]
with open(filename, 'r') as file:
    line = file.readline()
    elves = []
    calories = []
    index = 0
    while line:
        if (line == '\n'):
            total_calories = reduce(lambda x, y: x+y, calories)
            elves.append({"index": index, "calories": calories, "total_calories": total_calories})
            calories = []
            index += 1
        else:
            calories.append(int(line))
        line = file.readline()
    total_calories = reduce(lambda x, y: x + y, calories)
    elves.append({"index": index, "calories": calories, "total_calories": total_calories})
    elves = sorted(elves, key=lambda x: x['total_calories'], reverse=True)
    for i in range(0, len(elves)):
        print("Elf %s" % elves[i]['index'])
        print("Calories=%s" % elves[i]['calories'])
        print("Total calories=%s" % elves[i]['total_calories'])
        if i+1 < len(elves):
            print()
    top_three_calories = elves[0]['total_calories'] + elves[1]['total_calories'] + elves[2]['total_calories']
    print()
    print("Top three elves carry calories=%s" % top_three_calories)
    print("End of input")
