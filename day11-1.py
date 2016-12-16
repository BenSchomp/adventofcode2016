from copy import deepcopy
from collections import deque
  
class Node:
  nodes = dict()

  def __init__( self, orig=None ):
    self.floors = []
    self.elevator = 0

    self.parentId = -1
    self.distance = 0
    self.color = 0

    if( orig != None ):
      self.copy_ctor( orig )

  def copy_ctor( self, orig ):
    self.floors = deepcopy( orig.floors )
    self.elevator = orig.elevator
    self.parentId = id( orig )
    self.distance = orig.distance + 1

  def key( self ):
    result = ''
    for floor in self.floors:
      result += ''.join( floor ) + '|'
    result += '-' + str( self.elevator )
    return result

  def isSolved( self ):
    return len( self.floors[0] ) + len( self.floors[1] ) + len( self.floors[2] ) == 0

  def isFried( self ):
    i = 0
    genPresent = False
    floor = self.floors[ self.elevator ] 
    numItems = len( floor )

    while i < numItems:
      cur = floor[i] # 'HM'
      if cur[1] == 'M':
        chipType = cur[0] # 'H'
        chipMatched = False
        j = 0
        while j < numItems:
          if j == i:
            j += 1
            continue
          cur = floor[j] # 'HG'
          if cur[1] == 'G':
            genPresent = True
            genType = cur[0] # 'H'
            if chipType == genType:
              chipMatched = True
              break
          j += 1

        if genPresent and not chipMatched:
          return True
      i += 1

    return False

  def setFloors( self, newFloors ):
    self.floors = newFloors
    for i in self.floors:
      i.sort()

    self.markSeen()

  # returns False if it was previously seen, or fries chips
  def markSeen( self ):
    if self.key() in self.nodes:
      #print ' ! already seen it !'
      return False
    self.nodes[ self.key() ] = 1

    if self.isFried():
      return False

    #self.nodes[id(self)] = self
    return True

  # returns False if the new position is invalid
  def move( self, items, to ):
    if abs( self.elevator - to ) != 1:
      print ' ! illegal move!'
      return False

    for i in items:
      self.floors[self.elevator].remove( i )
      self.floors[to].append( i )

    self.floors[to].sort()
    self.elevator = to

    # check solved
    if self.isSolved():
      print "** solved: %d steps **" % self.distance
      exit()
      i = self
      step = self.distance
      while i.parentId != -1:
        #print 'step %d:' % step #, i.key()
        i.display()
        i = self.nodes[i.parentId]
        step -= 1
      i.display()
      #print 'step %d:' % step #, i.key()
      exit()

    return self.markSeen()

  def display( self, text = '' ):
    print
    if text != '':
      print text
    #print "Id: %d, Key: %s" % (id(self), self.key())
    for i in range( 3, -1, -1 ):
      print 'f%d:' % (i+1),
      print '*' if self.elevator == i else ' ',
      print ' '.join( self.floors[i] )

file = open('day11-example.txt', 'r')

# initial setup
floors =[ [] for i in range(0, 4) ]
i = 0
for line in file:
  line = line.rstrip()

  parts = line.split( ' a ' )
  for part in parts[1:]:
    subParts = part.split()
    if subParts[1][0:9] == 'generator':
      code = subParts[0][0] + 'g'
    elif subParts[1][0:9] == 'microchip':
      code = subParts[0][0] + 'm'

    floors[i].append( code.upper() )
    floors[i].sort()
  i += 1

file.close()

work = deque() # queue to hold all current level of working nodes

# create root node
root = Node()
root.setFloors( floors )
work.append( root )
print "\n---- ROOT (id: %d, #work: %d, dist: %d) ----" \
  % ( id(root), len( work ), 0 )
root.display()

# do it
curLevel = 0
while len( work ) > 0:
  parent = work.popleft()
  #print "\n---- New Parent (id: %d, #work: %d, dist: %d) ----" \
    #% ( id(parent), len( work ), parent.distance + 1 )
  if parent.distance + 1 > curLevel:
    curLevel = parent.distance + 1
    print "++ New Level: %d, Size of Work: %d" % ( curLevel, len( work ) )

  curElevator = parent.elevator
  curFloor = parent.floors[ curElevator ]
  numItems = len( curFloor )
  floorMin = 0

  if( len( parent.floors[0] ) == 0 ):
    floorMin = 1
    if( len( parent.floors[1] ) == 0 ):
      floorMin = 2

  twoUp = False
  twoDown = False

  # try moving pieces in pairs
  for i in range( 0, numItems ):
    for j in range( i+1, numItems ):
      # up
      if curElevator < 3:
        newNode = Node( parent )
        if newNode.move( [ curFloor[i], curFloor[j] ], curElevator + 1 ):
          work.append( newNode )
          twoUp = True

      #down
      if curElevator > floorMin:
        newNode = Node( parent )
        if newNode.move( [ curFloor[i], curFloor[j] ], curElevator - 1 ):
          work.append( newNode )
          twoDown = True

  # if that's not possible, try singles
  for i in range( 0, numItems ):
    # up
    if not twoUp and curElevator < 3:
      newNode = Node( parent )
      if newNode.move( [ curFloor[i] ], curElevator + 1 ):
        work.append( newNode )

    #down
    if not twoDown and curElevator > floorMin:
      newNode = Node( parent )
      if newNode.move( [ curFloor[i] ], curElevator - 1 ):
        work.append( newNode )


