"""
DAY 1
PART 1
"""
import sys
filename = sys.argv[1]
with open(filename, 'r') as file:
    line = file.readline()
    depth = [None, None]
    inc_total = 0
    while line:
        depth[1] = depth[0]
        depth[0] = int(line)
        if depth[1] is not None:
            if (depth[0] > depth[1]):
                inc_total += 1
                print("%s (increased)" % depth[0])
            elif (depth[0] == depth[1]):
                print("%s (no change)" % depth[0])
            else:
                print("%s (decreased)" % depth[0])
        else:
            print("%s (N/A - no previous measurement)" % depth[0])
        line = file.readline()
    print("End of input")
    print("Increasing depth: %s" % inc_total)
