"""
DAY 6
PART 2
"""
import sys
import re
from functools import reduce
filename = sys.argv[1]
with open(filename, 'r') as file:
    line = file.readline()
    window = []
    distinct_characters = 14
    packet_marker_index = 0
    while line:
        # Remove newline char.
        if line[len(line) - 1] == '\n':
            line = line[:-1]
        print(line)
        for i in range(0, len(line)):
            c = line[i]
            window.append(c)
            if len(window) == distinct_characters:
                #print(window)
                if len(set(window)) == distinct_characters:
                    print(window)
                    packet_marker_index = i + 1
                    break
                del window[0]

        line = file.readline()
    print("End of input")
    print("Packet marker index = %s" % packet_marker_index)
