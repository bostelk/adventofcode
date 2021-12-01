"""
DAY 1
PART 2
"""
import sys
filename = sys.argv[1]
with open(filename, 'r') as file:
    line = file.readline()
    depth = [None, None, None]
    depth_sum = [None, None]
    inc_total = 0
    while line:
        depth[2] = depth[1]
        depth[1] = depth[0]
        depth[0] = int(line)
        if depth[2] is not None:
            if depth[1] is not None:
                depth_sum[1] = depth_sum[0]
                depth_sum[0] = depth[2] + depth[1] + depth[0]
                if depth_sum[1] is not None:
                    if (depth_sum[0] > depth_sum[1]):
                        inc_total += 1
                        print("%s (increased)" % depth_sum[0])
                    elif (depth_sum[0] == depth_sum[1]):
                        print("%s (no change)" % depth_sum[0])
                    else:
                        print("%s (decreased)" % depth_sum[0])
                else:
                    print("%s (N/A - no previous measurement)" % depth_sum[0])
        line = file.readline()
    print("End of input")
    print("Increasing depth: %s" % inc_total)
