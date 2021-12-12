"""
DAY 9
PART 2
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
def find_neighbours(x, y, heightmap, heightmap_dim):
    neighbours = []
    if y - 1 >= 0:
        if heightmap[y - 1][x] < 9:
            neighbours.append((x, y - 1))
    if x + 1 < heightmap_dim:
        if heightmap[y][x + 1] < 9:
            neighbours.append((x + 1, y))
    if y + 1 < len(heightmap):
        if heightmap[y + 1][x] < 9:
            neighbours.append((x, y + 1))
    if x - 1 >= 0:
        if heightmap[y][x - 1] < 9:
            neighbours.append((x - 1, y))
    return neighbours
def find_basin_size(x, y, heightmap, heightmap_dim):
    visited = set()
    visited.add((x,y))
    to_visit = find_neighbours(x, y, heightmap, heightmap_dim)
    while len(to_visit) > 0:
        point = to_visit.pop()
        visited.add(point)
        neighbours = find_neighbours(point[0], point[1], heightmap, heightmap_dim)
        to_visit += set(neighbours).difference(visited)
    return len(visited)
low_points = find_low_points(heightmap, heightmap_dim)
basins = sorted(map(lambda point: find_basin_size(point[0],point[1], heightmap, heightmap_dim), low_points), reverse=True)
print("%s * %s * %s = %s" % (basins[0], basins[1], basins[2], basins[0] * basins[1] * basins[2]))
