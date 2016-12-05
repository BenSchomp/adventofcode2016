#commands = [ "R2", "L3" ] # 2
#commands = [ "R2", "R2", "R2" ] # 5
#commands = [ "R5", "L5", "R5", "R3" ] # 12
commands = [ "R5","R4","R2","L3","R1","R1","L4","L5","R3","L1","L1","R4","L2","R1","R4","R4","L2","L2","R4","L4","R1","R3","L3","L1","L2","R1","R5","L5","L1","L1","R3","R5","L1","R4","L5","R5","R1","L185","R4","L1","R51","R3","L2","R78","R1","L4","R188","R1","L5","R5","R2","R3","L5","R3","R4","L1","R2","R2","L4","L4","L5","R5","R4","L4","R2","L5","R2","L1","L4","R4","L4","R2","L3","L4","R2","L3","R3","R2","L2","L3","R4","R3","R1","L4","L2","L5","R4","R4","L1","R1","L5","L1","R3","R1","L2","R1","R1","R3","L4","L1","L3","R2","R4","R2","L2","R1","L5","R3","L3","R3","L1","R4","L3","L3","R4","L2","L1","L3","R2","R3","L2","L1","R4","L3","L5","L2","L4","R1","L4","L4","R3","R5","L4","L1","L1","R4","L2","R5","R1","R1","R2","R1","R5","L1","L3","L5","R2" ]
#commands = [ "R8", "R4", "R4", "R8" ] # 8 & 4

def getNewPosition( x, y, heading, distance ):
  dx = 0
  dy = 0

  if heading == 0:
    dy = 1
  elif heading == 1:
    dx = 1
  elif heading == 2:
    dy = -1
  else:
    dx = -1

  # part 2 counts each step as a visit, so have to loop here and mark
  #  each location as visited
  for i in range( 0, distance ):
    x += dx
    y += dy
    visitLocation( x, y )

  return ( x, y )

def getDistance( x1, y1, x2, y2 ):
  return abs(x1 - x2) + abs(y1 - y2)

bunnyX = 0
bunnyY = 0
foundBunny = False
visited = set()

def visitLocation( x, y ):
  global bunnyX, bunnyY, foundBunny, visited
  if not foundBunny:
    key = "%d,%d" % (x, y)
    if key in visited:
      bunnyX = x
      bunnyY = y
      foundBunny = True
      #print " * foundBunny: %d, %d" % (x, y)
    else:
      visited.add(key)

x = 0
y = 0
heading = 0

visitLocation( 0, 0 )

for command in commands:
  rotate = command[0]
  distance = int( command[1:] )
  if command[0] == 'R':
    heading = 0 if heading == 3 else heading + 1
  else:
    heading = 3 if heading == 0 else heading - 1

  ( x, y ) = getNewPosition( x, y, heading, distance )

print "distance from end to start: %d blocks" % getDistance( x, y, 0, 0 )
print "distance from start to bunny: %d blocks" % getDistance( 0, 0, bunnyX, bunnyY )
