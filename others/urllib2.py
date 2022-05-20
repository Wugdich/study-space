# !python3 urllib2.py
# Reading binary files

import urllib.request, urllib.parse, urllib.error

img = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg')
fhand = open('cover3.jpg', 'wb')

# To avoid runnig out of memory.
size = 0
while True:
    info = img.read(1000)
    if len(info) < 1: break
    size += len(info)
    fhand.write(info)
fhand.close()

print(f'{size} characters copied.')
print('Image downloaded and saved.')
