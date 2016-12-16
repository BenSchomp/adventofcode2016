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
    self.parentId = self.key() # id( orig )
    self.distance = orig.distance + 1

  def key_old( self ):
    result = ''
    for floor in self.floors:
      result += ''.join( floor ) + '|'
    result += '-' + str( self.elevator )
    return result

  # the key is not a hash - multiple states can map to the same key
  # since pairs are interchangeable, just mark the position of pairs & singles
  def key( self ):
    result = ''
    for floor in self.floors:
      floorResult = ''
      i = 0
      iMax = len(floor)
      while i < iMax:
        cur = floor[i]
        if i+1 < iMax:
          if floor[i][0] == floor[i+1][0]:
            # we've got a pair
            floorResult += 'P'
            i += 1
          else:
            floorResult += 'S'
        else:
          floorResult += 'S'

        i += 1

      result = result + ''.join(sorted(floorResult)) + ','

    result += str(self.elevator)
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
      return False

    if self.isFried():
      return False

    self.nodes[ self.key() ] = self
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
      i = self
      step = self.distance
      while i.parentId != -1:
        i.display( 'step ' + str(step) )
        i = self.nodes[i.parentId]
        step -= 1
      i.display( 'step ' + str(step) )

      print "\n** solved: %d steps **" % self.distance
      exit()

    return self.markSeen()

  def display( self, text = '' ):
    print
    if text != '':
      print text
    for i in range( 3, -1, -1 ):
      print 'f%d:' % (i+1),
      print '*' if self.elevator == i else ' ',
      print ' '.join( self.floors[i] )

file = open('day11-input2.txt', 'r')

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

# do it
level = 0
while len( work ) > 0:
  parent = work.popleft()
  if parent.distance + 1 > level:
    level = parent.distance + 1
    print "++ Level: %d, Work Queue: %d" % ( level, len( work ) )

  curElevator = parent.elevator
  curFloor = parent.floors[ curElevator ]
  numItems = len( curFloor )

  # once you clear the lower floors, no need to move anything down there
  floorMin = 0
  if( len( parent.floors[0] ) == 0 ):
    floorMin = 1
    if( len( parent.floors[1] ) == 0 ):
      floorMin = 2

  # try moving pieces in pairs
  for i in range( 0, numItems ):
    for j in range( i+1, numItems ):
      # up
      if curElevator < 3:
        newNode = Node( parent )
        if newNode.move( [ curFloor[i], curFloor[j] ], curElevator + 1 ):
          work.append( newNode )

      #down
      if curElevator > floorMin:
        newNode = Node( parent )
        if newNode.move( [ curFloor[i], curFloor[j] ], curElevator - 1 ):
          work.append( newNode )

  # ... now run through the singles
  for i in range( 0, numItems ):
    # up
    if curElevator < 3:
      newNode = Node( parent )
      if newNode.move( [ curFloor[i] ], curElevator + 1 ):
        work.append( newNode )

    #down
    if curElevator > floorMin:
      newNode = Node( parent )
      if newNode.move( [ curFloor[i] ], curElevator - 1 ):
        work.append( newNode )


