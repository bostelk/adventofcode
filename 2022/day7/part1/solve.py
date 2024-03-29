"""
DAY 7
PART 1
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
                print(path + " " + str(map[path]['total_sizebytes_inc']))
                total_sizebytes += map[path]['total_sizebytes_inc']
        map[key]['total_sizebytes_inc'] = total_sizebytes
    # find directories at most a total size
    threshold_sizebytes = 100000
    sum_total_size = 0
    dirs = []
    for key in map.keys():
        if map[key]['total_sizebytes_inc'] <= threshold_sizebytes:
            dirs.append(key)
            sum_total_size += map[key]['total_sizebytes_inc']
    dirs = sorted(dirs)
    for dir in dirs:
        print(dir + " " + str(map[dir]['total_sizebytes']) + " " + str(map[dir]['total_sizebytes_inc']))
    print("Sum total size of directories at most sizebytes=%s" % (sum_total_size)) # 2572996,1286498 is too high