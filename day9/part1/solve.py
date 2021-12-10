"""
DAY 9
PART 1
"""
import sys
heightmap = []
heightmap_dim = 0
filename = sys.argv[1]
with open(filename, 'r') as file:
    line = file.readline()
    while line:
        row = map(lambda x: int(x), line.strip())
        heightmap.append(row)
        heightmap_dim = max(heightmap_dim, len(row))
        line = file.readline()
    print("End of input")

def find_low_points(heightmap, heightmap_dim):
    low_points = []
    for y in range(0, len(heightmap)):
        for x in range(0, heightmap_dim):
            point = heightmap[y][x]
            top = float('inf')
            right = float('inf')
            bottom = float('inf')
            left = float('inf')
            if y - 1 >= 0:
                top = heightmap[y-1][x]
            if x + 1 < heightmap_dim:
                right = heightmap[y][x+1]
            if y + 1 < len(heightmap):
                bottom = heightmap[y+1][x]
            if x - 1 >= 0:
                left = heightmap[y][x-1]
            if point < min(top, right, bottom, left):
                low_points.append((x,y,point))
    return low_points
low_points = find_low_points(heightmap, heightmap_dim)
risk = sum(map(lambda x: x[2] + 1, low_points))
print("Risk level: %s" % risk)
