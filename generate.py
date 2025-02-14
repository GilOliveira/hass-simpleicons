import os

ICON_SIZE = 1024

def make_file(directory, name, out):
    out.write('<ha-iconset-svg name="{}" size="{}"><svg><defs>\n'.format(name, ICON_SIZE))
    for f in os.listdir(directory):
        if not f.endswith('.svg'):
            continue
        with open(os.path.join(directory, f), 'r') as fp:
            name = os.path.splitext(f)[0]
            data = fp.read()
            size_start = data.find('viewBox="')+len('viewBox="')
            size_end = data[size_start:].find('"')
            size = data[size_start:size_start+size_end].split(' ')
            print (size)
            width = float(size[2])
            height = float(size[3])
            scale = max(width, height)/ICON_SIZE
            start = data.find('<path')
            out.write('<g id="{0}" transform="scale({1} {1})">'.format(name, 1/scale) + data[start:-6] + '</g>\n')
    out.write('</defs></svg></ha-iconset-svg>')


# Run this in /simple-icons
with open("hass-simple-icons.html", 'w') as out:
    make_file('icons', 'si', out)
