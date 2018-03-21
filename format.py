import re
import sys
import yaml

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
    print('Usage: python ./format.py [filename] [output]')
    sys.exit()
f = open(sys.argv[1], 'r+')
colors = yaml.load(f)
f.close()

result = {}
for k in colors:
    if (not is_hex(colors[k])):
        result[k] = colors[k]
        continue
    rgb = hex_to_int_color(colors[k])
    rgb = [ x / 255 for x in rgb ]
    result[k] = {'hex': colors[k], 'r': rgb[0], 'g': rgb[1], 'b': rgb[2]}

with open(sys.argv[2], 'w+') as f:
    f.write(yaml.dump(result))
