"""
DAY 7
PART 2
"""
import sys
import re
from functools import reduce
filename = sys.argv[1]
with open(filename, 'r') as file:
    line = file.readline()
    pwd = None
    map = {}
    while line:
        # Remove newline char.
        if line[len(line) - 1] == '\n':
            line = line[:-1]
        print(line)
        # Command
        m = re.match(r"\$ (?P<command>\w\w) ?(?P<dirname>[\w|..|/]+)?", line)
        if m:
            command = m.groupdict()['command']
            dirname = m.groupdict()['dirname']
            if command == "cd":
                if pwd == None:
                    pwd = dirname
                # Absolute dir
                elif dirname[0] == "/":
                    pwd = dirname
                # Pop directory
                elif dirname == "..":
                    last_sep_index = pwd.rfind("/")
                    if last_sep_index == 0: # root
                        pwd = "/"
                    else:
                        pwd = pwd[:last_sep_index]
                else:
                    if pwd == "/": # root
                        pwd = pwd + dirname
                    else:
                        pwd = pwd + "/" + dirname
                print("pwd=%s" %pwd)
            elif command == "ls":
                line = file.readline()
                total_sizebytes = 0 #exclusive dir sizebytes
                contents = []
                while line and line[0] != "$":
                    # Remove newline char.
                    if line[len(line) - 1] == '\n':
                        line = line[:-1]
                    parts = line.split(" ")
                    kind = None
                    sizebytes = 0
                    filename = parts[1]
                    if parts[0] == "dir":
                        kind = "dir"
                    else:
                        kind = "file"
                        sizebytes = int(parts[0])
                    print("kind=%s, sizebytes=%s, filename=%s" % (kind, sizebytes, filename))
                    contents.append((kind, sizebytes, filename))
                    total_sizebytes += sizebytes
                    line = file.readline()
                print("total_sizebytes=%s" % total_sizebytes)
                map[pwd] = {
                    'contents': contents,
                    'total_sizebytes': total_sizebytes
                }
                continue
            else:
                print("unknown command=%s" % command)
        line = file.readline()
    print("End of input")
    # sum inclusive dir sizebytes
    keys = map.keys()
    keys = sorted(keys, reverse=True) # walk diretories from bottom up
    for key in keys:
        total_sizebytes = map[key]['total_sizebytes']
        for kind, sizebytes, filename in map[key]['contents']:
            if kind == "dir":
                if key == "/": # root
                    path = key + filename
                else:
                    path = key + "/" + filename
                total_sizebytes += map[path]['total_sizebytes_inc']
        map[key]['total_sizebytes_inc'] = total_sizebytes
    sizebytes_capacity = 70000000
    sizebytes_required = 30000000
    sizebytes_avail = sizebytes_capacity - map["/"]['total_sizebytes_inc']
    sizebytes_to_delete = sizebytes_required - sizebytes_avail
    candidates = []
    for key in map.keys():
        print(key + " " + str(map[key]['total_sizebytes_inc']))
        if map[key]['total_sizebytes_inc'] >= sizebytes_to_delete:
            candidates.append((key, map[key]['total_sizebytes_inc']))
    candidates = sorted(candidates, key=lambda x: x[1])  # sort by sizebytes ascending
    print("The smallest directory to delete=%s %s" % candidates[0])