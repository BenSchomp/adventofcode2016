from copy import deepcopy
from collections import deque


# -=-=- HELPERS -=-=-

version = "examplex"
if version == 'example':
  file = open('day22-example.txt', 'r')
  WIDTH = 3
  HEIGHT = 3
else:
  file = open('day22-input.txt', 'r')
  WIDTH = 38
  HEIGHT = 28

loOutlier = 0
hiOutlier = 0

def display( n ):
  for y in range( HEIGHT ):
    r = ''
    for x in range( WIDTH ):
      if y == 0 and x == WIDTH-1:
        r += '*'
      r += "%d/%d " % (n[y][x][0], n[y][x][1])

    print r

def getChar( n, cur, goal ):
  data = n[cur[1]][cur[0]]
  used = data[0]
  size = data[1]

  if cur == goal:
    ch = 'G'
  else:
    if used < loOutlier:
      ch = '_'
    elif size > hiOutlier:
      ch = '#'
    else:
      ch = '.'

  return ch

def getKey( n, goal ):
  r = ''
  for y in range( HEIGHT ):
    for x in range( WIDTH ):
      r += getChar( n, (x,y), goal )

  return r

def display2( n, goal ):
  for y in range( HEIGHT ):
    r = ''
    for x in range( WIDTH ):
      r += getChar( n, (x,y), goal )

    print r

# -=-=- INIT -=-=-

nodes = [[ -1 for x in range(WIDTH)] for y in range(HEIGHT)]
maxX = 0
maxY = 0
sizeTotal = 0
count = 0
for line in file:
  count += 1
  line = line.rstrip()
  parts = line.split()

  location = parts[0].split( '-' )
  x = int( location[1][1:] )
  y = int( location[2][1:] )

  if x > maxX:
    maxX = x
  if y > maxY:
    maxY = y

  used = int( parts[2][:-1] )
  size = int( parts[1][:-1] )
  sizeTotal += size

  nodes[y][x] = [ used, size ]

file.close()

sizeMean = sizeTotal / float(count)
loOutlier = sizeMean * 0.25
hiOutlier = sizeMean * 1.75

work = deque()
seen = dict()

# -=-=- DO IT -=-=-

cur = (maxX, 0 )
display2( nodes, cur )

key = getKey( nodes, cur )
work.append( key )
seen[key] = 1


