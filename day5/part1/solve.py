"""
DAY 5
PART 1
"""
import sys
import re
line_horizontal = lambda p0,p1: p0[0] == p1[0]
line_vertical = lambda p0,p1: p0[1] == p1[1]
line_segment_expression = re.compile(r"^((\d+),(\d+)) -> ((\d+),(\d+))$")
def parse_line_segment(text):
    match = line_segment_expression.match(text)
    if match:
        subgroup_to_int = lambda x: int(match.groups()[x])
        x0 = subgroup_to_int(1)
        y0 = subgroup_to_int(2)
        x1 = subgroup_to_int(4)
        y1 = subgroup_to_int(5)
        return (x0,y0), (x1,y1)
    return None
def from_to_points(p0, p1):
    points = [p0]
    point = p0
    while point != p1:
        if line_horizontal(point, p1):
            delta = 1 if p1[1] > point[1] else -1
            point = (point[0], point[1]+delta)
        elif line_vertical(point, p1):
            delta = 1 if p1[0] > point[0] else -1
            point = (point[0]+delta, point[1])
        else:
            exit("fail")
        points.append(point)
    return points
point_to_count = {}
def insert_point(p):
    if p in point_to_count:
        point_to_count[p] += 1
    else:
        point_to_count[p] = 1
filename = sys.argv[1]
with open(filename, 'r') as file:
    line = file.readline()
    while line:
        p1, p2 = parse_line_segment(line)
        if p1 or p2:
            if line_horizontal(p1, p2) or line_vertical(p1, p2):
                points = from_to_points(p1, p2)
                map(insert_point, points)
        line = file.readline()
    print("End of input")
min_overlap_count = 2
filter_count = lambda kvp: kvp[1] >= min_overlap_count
overlap_points = filter(filter_count, point_to_count.items())
number_of_overlap_points = len(overlap_points)
print("There are %s points that overlap at least %s times." % (number_of_overlap_points, min_overlap_count))
