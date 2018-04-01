import re
import sys
import yaml
import subprocess
from functools import reduce

def hex_to_int_color(v):
    if v[0] == '#':
        v = v[1:]
    return int(v[:2], 16), int(v[2:4], 16), int(v[4:6], 16)

def is_hex(v):
    if len(v) != 6:
        return False
    pattern = r"[0-9a-fA-F]+"
    return re.match(pattern, v)

if len(sys.argv) != 3:
    print('Usage: python ./template-generator.py [colorfile] [input]')
    sys.exit()
f = open(sys.argv[1], 'r+')
colors = yaml.load(f)
f.close()

cmd = ['perl', '-p', '-e']
op = ""
for k in colors:
    if (not is_hex(colors[k])):
        continue
    op += f's/{colors[k]}/{{{{{k}}}}}/gi;'
cmd.append(op) 
cmd.append(sys.argv[2])
subprocess.call(cmd)
