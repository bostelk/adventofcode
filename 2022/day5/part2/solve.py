"""
DAY 5
PART 2
"""
import sys
import re
from functools import reduce
filename = sys.argv[1]
with open(filename, 'r') as file:
    line = file.readline()
    parse_mode = "CRANE"
    crates = {}
    while line:
        # Remove newline char.
        if line[len(line) - 1] == '\n':
            line = line[:-1]
        if len(line) == 0:
            print(crates)
            parse_mode = "PROCEDURE"
            line = file.readline()
            continue
        if parse_mode == "CRANE":
            for i in range(0, len(line)):
                c = line[i]
                if line[i] == "[" and line[i+2] == "]":
                    stack_index = int(i / 4) + 1
                    if stack_index in crates:
                        crates[stack_index].append(line[i+1])
                    else:
                        crates[stack_index] = [line[i+1]]
                    i+=2
        elif parse_mode == "PROCEDURE":
            print("PROCEDURE %s" % line)
            m = re.match(r"move (?P<quantity>\d+) from (?P<from>\d+) to (?P<to>\d+)", line)
            if m:
                proc = m.groupdict()
                if int(proc['quantity']) == 1:
                    crate = crates[int(proc['from'])].pop(0)
                    crates[int(proc['to'])].insert(0, crate)
                else:
                    crates[int(proc['to'])] = crates[int(proc['from'])][0:int(proc['quantity'])] + crates[int(proc['to'])]
                    del crates[int(proc['from'])][0:int(proc['quantity'])]
                print(crates)
        line = file.readline()
    print("End of input")
    keys = crates.keys()
    keys = sorted(keys)
    message = ""
    for key in keys:
        message += crates[key][0]
    print(message)
