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

def display_old( n ):
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
      ch = 'X'
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

def display( n, goal ):
  print
  for y in range( HEIGHT ):
    r = ''
    for x in range( WIDTH ):
      if False and x == 0 and y == 0:
        r += 'O'
      else:
        r += getChar( n, (x,y), goal )

    print r

# -=-=- INIT -=-=-

nodes = [[ -1 for x in range(WIDTH)] for y in range(HEIGHT)]
maxX = 0
maxY = 0
emptyX = 0
emptyY = 0
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

  if used == 0:
    emptyX = x
    emptyY = y

  nodes[y][x] = [ used, size ]

file.close()

sizeMean = sizeTotal / float(count)
loOutlier = sizeMean * 0.25
hiOutlier = sizeMean * 1.75

work = deque()
seen = dict()

# -=-=- DO IT -=-=-

curX = maxX
curY = 0
moves = 0
display( nodes, (curX, curY) )

key = getKey( nodes, (curX, curY) )
work.append( key )
seen[key] = 1

def move( fromX, fromY, toX, toY ):
  global moves
  if toX < 0 or toX > WIDTH-1 or toY < 0 or toY > HEIGHT:
    print "OUT OF BOUNDS (%d,%d) to (%d,%d)" % (fromX,fromY,toX,toY)
    exit()

  fromUsed = nodes[fromY][fromX][0]
  fromSize = nodes[fromY][fromX][1]
  toUsed = nodes[toY][toX][0]
  toSize = nodes[toY][toX][1]

  if fromUsed > toSize or toUsed > fromSize:
    return False

  tmpNode = nodes[fromY][fromX]
  nodes[fromY][fromX] = nodes[toY][toX]
  nodes[toY][toX] = tmpNode

  moves += 1

  return True

# move empty space up to the top row
while emptyY > 0:
  if move( emptyX, emptyY, emptyX, emptyY-1 ):
    emptyY -= 1
    display( nodes, (curX, curY) )
  else:
    if move( emptyX, emptyY, emptyX-1, emptyY ):
      emptyX -=1
      display( nodes, (curX, curY) )
    else:
      print "NOW WHAT?"
      exit()

# move empty space right to the goal
while emptyX < curX - 1:
  if not move( emptyX, emptyY, emptyX+1, emptyY ):
    print "UH OH!"
    exit()

  emptyX += 1
  display( nodes, (curX, curY) )

while True:
  if move( emptyX, emptyY, emptyX+1, emptyY ):
    emptyX += 1
    curX -= 1
    display( nodes, (curX, curY) )
    if curX < 1:
      print "Done: ", moves
      exit()
  if move( emptyX, emptyY, emptyX, emptyY+1 ):
    emptyY += 1
    display( nodes, (curX, curY) )
  if move( emptyX, emptyY, emptyX-1, emptyY ):
    emptyX -= 1
    display( nodes, (curX, curY) )
  if move( emptyX, emptyY, emptyX-1, emptyY ):
    emptyX -= 1
    display( nodes, (curX, curY) )
  if move( emptyX, emptyY, emptyX, emptyY-1 ):
    emptyY -= 1
    display( nodes, (curX, curY) )


